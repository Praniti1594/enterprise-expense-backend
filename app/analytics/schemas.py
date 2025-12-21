# app/analytics/schemas.py
from pydantic import BaseModel

class TeamSummaryResponse(BaseModel):
    category: str
    total_spent: float
    expense_count: int
