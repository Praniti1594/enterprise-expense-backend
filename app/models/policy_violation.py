# app/models/policy_violation.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class PolicyViolation(Base):
    __tablename__ = "policy_violations"

    id = Column(Integer, primary_key=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"))
    policy_id = Column(Integer, ForeignKey("policies.id"))
    reason = Column(String(255))
