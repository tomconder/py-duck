# py-duck

py-duck is a small demo of DuckDB, an in-process SQL database. It loads a table of departments and a table of employees into an in-memory database, and then it prints two queries.

## How to run it

The project uses uv to manage Python and its dependencies. Run the demo and the tests with these commands:

```sh
uv run python main.py
uv run python -m unittest
```
