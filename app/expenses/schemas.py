# app/expenses/schemas.py
from pydantic import BaseModel, Field
from datetime import date

class ExpenseCreate(BaseModel):
    category: str
    amount: float = Field(gt=0)
    expense_date: date
    receipt_url: str
