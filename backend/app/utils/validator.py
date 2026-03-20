FORBIDDEN = ["DELETE", "DROP", "UPDATE", "INSERT", "ALTER"]

def validate_sql(query: str):
    q = query.upper()

    if not q.startswith("SELECT"):
        raise ValueError("Only SELECT allowed")

    for word in FORBIDDEN:
        if word in q:
            raise ValueError(f"Forbidden keyword: {word}")

    if "*" in q:
        raise ValueError("SELECT * is not allowed")