# app/expenses/service.py

from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.models.expense import Expense
from app.models.policy_violation import PolicyViolation
from app.policies.engine import evaluate_policy


def create_expense(db, user, data):
    expense = Expense(
        employee_id=user.id,
        category=data.category,
        amount=data.amount,
        expense_date=data.expense_date,
        receipt_url=data.receipt_url
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)

    policy, violation_reason = evaluate_policy(db, expense)

    if violation_reason:
        violation = PolicyViolation(
            expense_id=expense.id,
            policy_id=policy.id,
            reason=violation_reason
        )
        db.add(violation)
        db.commit()

    return expense


def get_expense(db: Session, expense_id: int) -> Expense | None:
    return db.query(Expense).filter(Expense.id == expense_id).first()