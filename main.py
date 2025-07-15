import duckdb


def init(con):
    with open("init-data.sql", "r") as file:
        sql_query = file.read()

    con.execute(sql_query)

    print("Database initialized successfully")


def main(con):
    con.sql("SELECT id, name FROM t_employee").show()
    con.sql("SELECT name, location FROM t_department").show()


if __name__ == "__main__":
    con = duckdb.connect(database=":memory:")

    try:
        init(con)
        main(con)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        con.close()
