# app/approvals/service.py
from fastapi import HTTPException
from app.models.approval import Approval
from app.approvals.state import VALID_TRANSITIONS

def approve_expense(db, expense, user, decision, remarks):
    current = expense.status

    if decision == "REJECTED":
        expense.status = "REJECTED"
    else:
        allowed = VALID_TRANSITIONS.get(current, [])
        next_state = (
            "MANAGER_APPROVED" if user.role == "MANAGER"
            else "FINANCE_APPROVED"
        )

        if next_state not in allowed:
            raise HTTPException(400, "Invalid state transition")

        expense.status = next_state

    approval = Approval(
        expense_id=expense.id,
        approved_by=user.id,
        role=user.role,
        decision=decision,
        remarks=remarks
    )

    db.add(approval)
    db.commit()
