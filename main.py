# After running app by performing this command "python -m uvicorn main:app --reload"
# You will have a database and an API based on a model ==> watch on localhost:8000/api/v1/banks
# For access to documentation and Swagger UI ==> run
# Only post and get request performed here

from fastapi import FastAPI
from typing import List
from models import Bank

app = FastAPI()

db: List[Bank] = [
    Bank(
    country_name="Aruba",
    country_code="ABW",
    indicator_name=50,
    indicator_code="SP.RUR.TOTL.ZS",
    years=[49.224, 49.239, 49.254, 90.89],
    ),
    Bank(
    country_name="Afghanistan",
    country_code="AFG",
    indicator_name=60,
    indicator_code="SP.RUR.TOTL.ZS",
    years=[91.779, 91.492, 91.195, 90.89],
    )
]

@app.get("/")
async def root(): return {"Hello Saeed"}

@app.get("/api/v1/banks")
async def fetch_banks(): return db

@app.post("/api/v1/banks")
async def post_bank(bank: Bank): 
    db.append(bank)
    return {"id": bank.id}