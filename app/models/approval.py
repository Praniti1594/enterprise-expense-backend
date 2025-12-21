# app/models/approval.py
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from app.models.base import Base
from datetime import datetime
import enum

class DecisionEnum(str, enum.Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Approval(Base):
    __tablename__ = "approvals"

    id = Column(Integer, primary_key=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"))
    approved_by = Column(Integer, ForeignKey("users.id"))
    role = Column(String(20))
    decision = Column(Enum(DecisionEnum))
    remarks = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
