# py-duck

py-duck is a small demo of DuckDB, an in-process SQL database. It loads a table of departments and a table of employees into an in-memory database, and then it prints two queries.

## How to run it

The project uses uv to manage Python and its dependencies. Run the demo and the tests with these commands:

```sh
uv run python main.py
uv run python -m unittest
```

## Files

* `init-data.sql` creates the two tables, with foreign keys between them, and inserts the seed data.
* `main.py` loads the seed data and prints the queries.
* `test_main.py` checks the schema and the seed data.

The project uses Ruff to lint and format the code, and pre-commit to run Ruff and other checks on each commit.
