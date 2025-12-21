# app/models/expense.py
from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Float
from app.models.base import Base
import enum

class ExpenseStatus(str, enum.Enum):
    SUBMITTED = "SUBMITTED"
    MANAGER_APPROVED = "MANAGER_APPROVED"
    FINANCE_APPROVED = "FINANCE_APPROVED"
    REJECTED = "REJECTED"
    PAID = "PAID"

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String(50))
    amount = Column(Float)
    expense_date = Column(Date)
    status = Column(Enum(ExpenseStatus), default=ExpenseStatus.SUBMITTED)
    receipt_url = Column(String(255))
