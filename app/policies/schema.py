from pydantic import BaseModel
from enum import Enum

class TimeWindow(str, Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"

class PolicyCreate(BaseModel):
    category: str
    max_amount: int
    max_claims: int
    time_window: TimeWindow
