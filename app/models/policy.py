# app/models/policy.py
from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from app.models.base import Base
import enum

class TimeWindow(str, enum.Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True)
    category = Column(String(50))
    max_amount = Column(Integer)
    max_claims = Column(Integer)
    time_window = Column(Enum(TimeWindow))
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, ForeignKey("users.id"))
