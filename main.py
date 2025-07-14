import duckdb


def main():
    print("Hello from py-duck!")

    con = duckdb.connect("file.db")
    con.sql("SELECT id, name FROM t_employee").show()
    con.sql("SELECT name, location FROM t_department").show()


if __name__ == "__main__":
    main()
