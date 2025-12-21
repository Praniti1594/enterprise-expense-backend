# app/approvals/state.py

from app.models.expense import ExpenseStatus

VALID_TRANSITIONS = {
    ExpenseStatus.SUBMITTED: [ExpenseStatus.MANAGER_APPROVED, ExpenseStatus.REJECTED],
    ExpenseStatus.MANAGER_APPROVED: [ExpenseStatus.FINANCE_APPROVED, ExpenseStatus.REJECTED],
    ExpenseStatus.FINANCE_APPROVED: [ExpenseStatus.PAID],
}
