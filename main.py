"""
This module demonstrates duckdb
"""

from pathlib import Path

import duckdb


def main(con):
    """Load the seed data and show it"""
    con.execute(Path(__file__).with_name("init-data.sql").read_text(encoding="utf-8"))

    con.sql("SELECT id, name FROM t_employee").show()
    con.sql("SELECT name, location FROM t_department").show()


if __name__ == "__main__":
    with duckdb.connect(database=":memory:") as conn:
        main(conn)
