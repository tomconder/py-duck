import duckdb


def init():
    con = duckdb.connect("file.db")

    try:
        with open('init-data.sql', 'r') as file:
            sql_query = file.read()

        con.execute(sql_query)

        print("Database initialized successfully")

    except FileNotFoundError:
        print("Error: init-data.sql file not found")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        con.close()


def main():
    con = duckdb.connect("file.db")

    try:
        con.sql("SELECT id, name FROM t_employee").show()
        con.sql("SELECT name, location FROM t_department").show()
    except Exception as e:
        print(f"Error executing queries: {e}")
    finally:
        con.close()


if __name__ == "__main__":
    init()
    main()
