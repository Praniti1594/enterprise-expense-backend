# app/policies/engine.py

from datetime import timedelta
from app.models.policy import Policy, TimeWindow
from app.models.expense import Expense


def get_delta(window: TimeWindow):
    if window == TimeWindow.DAY:
        return timedelta(days=1)
    if window == TimeWindow.WEEK:
        return timedelta(days=7)
    if window == TimeWindow.MONTH:
        return timedelta(days=30)


def evaluate_policy(db, expense):
    policy = db.query(Policy).filter(
        Policy.category == expense.category,
        Policy.is_active == True
    ).first()

    if not policy:
        return None, None

    # 1️⃣ Amount rule
    if expense.amount > policy.max_amount:
        return policy, f"Amount exceeds limit of {policy.max_amount}"

    # 2️⃣ Time-window rule
    start_date = expense.expense_date - get_delta(policy.time_window)

    count = db.query(Expense).filter(
        Expense.employee_id == expense.employee_id,
        Expense.category == expense.category,
        Expense.expense_date >= start_date
    ).count()

    if count > policy.max_claims:
        return policy, "Exceeded max claims in time window"

    return None, None
