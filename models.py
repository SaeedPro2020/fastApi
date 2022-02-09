from typing import List
from pydantic import BaseModel

class Bank(BaseModel):
    country_name: str
    country_code: str
    indicator_name: int
    indicator_code: str
    years: List[float]