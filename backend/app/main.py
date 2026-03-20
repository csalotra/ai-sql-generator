from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User
from app.services.llm_service import generate_sql
from app.services.sql_service import execute_sql
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Health Check
@app.get("/")
def home():
    return {"message": "API is working"}


# Get all users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]


# Create user
@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    try:
        new_user = User(name=name, email=email)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    

# AI-powered query endpoint
@app.post("/query")
def run_ai_query(question: str):
    try:
        # Step 1: Generate SQL using LLM
        sql_query = generate_sql(question)

        # Step 2: Execute SQL safely
        result = execute_sql(sql_query)

        return {
            "question": question,
            "generated_sql": sql_query,
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))