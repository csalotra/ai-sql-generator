from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
import os
import re

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    max_retries=2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


# Generate SQL
@tool
def generate_sql_tool(question: str) -> str:
    """
    Converts natural language into SQL query for users table.
    """

    prompt = f"""
    You are a PostgreSQL expert.

    Convert the question into SQL.

    Table:
    users(id, name, email, created_at)

    Rules:
    - Only genereate SELECT queries
    - NEVER generate SELECT *
    - Always use columns: id, name, email, created_at
    - DO NOT wrap in ``` or markdown
    - DO NOT add explanation
    - DO NOT add 'sql' keyword
    - Output must start with SELECT

    Question: {question}
    """

    response = model.invoke(prompt)
    return response.content.strip()


def clean_sql_output(text: str) -> str:
    # Remove markdown ```sql ... ```
    text = re.sub(r"```sql|```", "", text, flags=re.IGNORECASE)
    # Remove extra whitespace
    text = text.strip()

    return text


# Simple Agent (Tool Caller)
def generate_sql(question: str) -> str:
    """
    Function that uses tools
    """
    sql_query = generate_sql_tool.invoke(question)
    clean_sql = clean_sql_output(sql_query)

    return clean_sql