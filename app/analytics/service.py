from sqlalchemy import func
from app.models.expense import Expense
from app.models.user import User
from app.models.policy_violation import PolicyViolation


def team_expense_summary(db, manager_id, limit=10, offset=0):
    rows = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_spent"),
            func.count(Expense.id).label("expense_count")
        )
        .join(User, User.id == Expense.employee_id)
        .filter(User.manager_id == manager_id)
        .group_by(Expense.category)
        .limit(limit)
        .offset(offset)
        .all()
    )

    return [
        {
            "category": row.category,
            "total_spent": float(row.total_spent),
            "expense_count": row.expense_count
        }
        for row in rows
    ]


def monthly_trend(db):
    rows = (
        db.query(
            func.month(Expense.expense_date).label("month"),
            func.sum(Expense.amount).label("total_spent")
        )
        .group_by(func.month(Expense.expense_date))
        .order_by(func.month(Expense.expense_date))
        .all()
    )

    return [
        {
            "month": row.month,
            "total_spent": float(row.total_spent)
        }
        for row in rows
    ]


def violation_rate(db):
    total = db.query(Expense).count()
    violations = db.query(PolicyViolation).count()

    return {
        "total_expenses": total,
        "violations": violations,
        "rate": round((violations / total) * 100, 2) if total else 0
    }
