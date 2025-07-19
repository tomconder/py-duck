"""
This module demonstrates duckdb
"""

import duckdb


def init(con):
    """Initialize database"""
    with open("init-data.sql", "r", encoding="utf-8") as file:
        sql_query = file.read()

    con.execute(sql_query)

    print("Database initialized successfully")


def main(con):
    """Main function"""
    con.sql("SELECT id, name FROM t_employee").show()
    con.sql("SELECT name, location FROM t_department").show()


if __name__ == "__main__":
    conn = duckdb.connect(database=":memory:")

    try:
        init(conn)
        main(conn)
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error: {e}")
    finally:
        conn.close()
