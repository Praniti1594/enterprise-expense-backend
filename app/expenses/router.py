# app/expenses/router.py
from fastapi import APIRouter, Depends
from app.expenses.schemas import ExpenseCreate
from app.expenses.service import create_expense
from app.core.dependencies import get_db, require_role

router = APIRouter(prefix="/expenses")

@router.post("")
def submit_expense(
    data: ExpenseCreate,
    user = Depends(require_role(["EMPLOYEE"])),
    db=Depends(get_db)
):
    return create_expense(db, user, data)
