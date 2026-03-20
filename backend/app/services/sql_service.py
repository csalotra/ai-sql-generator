from sqlalchemy import text
from app.db import engine
from app.utils.validator import validate_sql

def execute_sql(query: str):
    validate_sql(query)

    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.mappings().all()
        return [dict(row) for row in rows]
