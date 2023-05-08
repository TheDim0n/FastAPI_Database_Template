# FastAPI_Database_Template
Template for FastAPI projects with database.

![tests](https://github.com/TheDim0n/FastAPI_Database_Template/actions/workflows/tests.yml/badge.svg)

## Setup
1. Create and activate python virtual environment
2. Install dependencies:
    ```
    python -m pip install -U pip
    pip install -r requirements.txt
    ```
3. Create .env file to configurate application (see [Configuration](#configuration) section)
4. Apply database migrations:
    ```
    python migrate.py
    ```
5. Run application:
    ```
    python run.py
    ```
> API documentation awailable at http://localhost:8000/docs

## Configuration <a name="configuration"></a>
Available environment variables:

```
DB_URL                         # PostgresDsn, required. URL to PostgreSQL database
DB_SCHEMA                      # string, default is 'public'. PostgreSQL schema
                                 name
DEBUG                          # boolean, default is false. If true, enable
                                 server reloading
ROOT_PATH                      # string, default is empty string. Path setting
                                 for proxy.
```