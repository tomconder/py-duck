"""Checks on the seed data and schema."""

import datetime
import unittest

import duckdb

from main import load


class SeedDataTest(unittest.TestCase):
    """Fails if a schema, seed data, or duckdb change breaks the data."""

    def setUp(self):
        self.con = duckdb.connect(database=":memory:")
        load(self.con)

    def tearDown(self):
        self.con.close()

    def test_headcount_per_department(self):
        rows = self.con.sql(
            "SELECT d.name, count(*) FROM t_employee e "
            "JOIN t_department d ON d.id = e.department_id "
            "GROUP BY d.name ORDER BY d.name"
        ).fetchall()
        self.assertEqual(rows, [("Finance", 2), ("Tech", 2)])

    def test_hire_date_is_date(self):
        sql = "SELECT hire_date FROM t_employee WHERE id = 2"
        [(hired,)] = self.con.sql(sql).fetchall()
        self.assertEqual(hired, datetime.date(2021, 6, 1))

    def test_rejects_unknown_department(self):
        with self.assertRaises(duckdb.ConstraintException):
            self.con.execute(
                "INSERT INTO t_employee VALUES (9, 'X', 'x', null, '2020-01-01', 1, 99)"
            )

    def test_rejects_unknown_manager(self):
        with self.assertRaises(duckdb.ConstraintException):
            self.con.execute(
                "INSERT INTO t_employee VALUES (9, 'X', 'x', 99, '2020-01-01', 1, 1)"
            )

    def test_reload_is_idempotent(self):
        load(self.con)
        [(count,)] = self.con.sql("SELECT count(*) FROM t_employee").fetchall()
        self.assertEqual(count, 4)


if __name__ == "__main__":
    unittest.main()
