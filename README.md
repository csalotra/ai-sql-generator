# AI SQL Query Generator

A full-stack AI-powered demo application that converts natural language into SQL query and executes them on a PostgreSQL database.

Built using:
- FastAPI (Backend)
- React (Frontend)
- PostgreSQL (Database)
- LangChain + Gemini (LLM)

---

## Features

- Natural language → SQL query generation
- Secure SQL execution (only SELECT queries allowed)
- Clean UI to visualize results
- Full-stack architecture (React + FastAPI)

---

## Project Structure

ai-sql-app/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── db.py
│ │ ├── models.py
│ │ ├── services/
│ │ └── utils/
│ │
│ ├── requirements.txt
│ └── .env
│
├── frontend/
│ └── ai-sql-frontend/
│ ├── src/
│ ├── public/
│ ├── package.json
│ └── .env
│
├── .gitignore
└── README.md

## Backend Setup (FastAPI)

### 1. Navigate to backend

cd backend

### 2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate # Mac/Linux

### 3. Install dependencies

pip install -r requirements.txt

### 4. Setup environment variables

Create `.env`:

### 5. Run server

uvicorn app.main:app --reload


API available at: http://127.0.0.1:8000

---

## Frontend Setup (React)

### 1. Navigate to frontend

cd frontend/ai-sql-frontend


### 2. Install dependencies

npm install


### 3. Setup environment variables

Create `.env`:

(for local environment)
REACT_APP_API_URL=http://127.0.0.1:8000 


### 4. Run frontend

npm start

(In local environment)
App available at: http://localhost:3000

---

## How It Works

1. User enters a natural language query  
2. Backend sends prompt to LLM (Gemini via LangChain)  
3. LLM generates SQL query  
4. SQL is validated (only SELECT allowed)  
5. Query is executed on PostgreSQL  
6. Results returned to frontend  


## 🧪 Example Queries

- Show all users  
- Count users with name 'john', ignore case sentivity
- List users created today  