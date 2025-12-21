# app/approvals/router.py

from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import require_role, get_db
from app.approvals.schema import ApprovalRequest
from app.approvals.service import approve_expense
from app.expenses.service import get_expense

router = APIRouter(
    prefix="/approvals",
    tags=["Approvals"]
)

@router.post("/expenses/{expense_id}/approve")
def approve(
    expense_id: int,
    data: ApprovalRequest,
    user = Depends(require_role(["MANAGER", "ADMIN"])),
    db=Depends(get_db)
):
    expense = get_expense(db, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    approve_expense(db, expense, user, data.decision, data.remarks)
    return {"message": "Action recorded"}
