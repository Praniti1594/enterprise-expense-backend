from fastapi import APIRouter, Depends, Query
from app.core.dependencies import get_db, require_role
from app.analytics.service import (
    team_expense_summary,
    monthly_trend,
    violation_rate
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/team-summary")
def get_team_summary(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    user=Depends(require_role("MANAGER")),
    db=Depends(get_db)
):
    return team_expense_summary(db, user.id, limit, offset)



@router.get("/monthly-trend")
def get_monthly_trend(
    user=Depends(require_role("MANAGER")),
    db=Depends(get_db)
):
    return monthly_trend(db)


@router.get("/violation-rate")
def get_violation_rate(
    user=Depends(require_role("ADMIN")),
    db=Depends(get_db)
):
    return violation_rate(db)
