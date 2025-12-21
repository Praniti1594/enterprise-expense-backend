# app/policies/router.py
from fastapi import APIRouter, Depends
from app.policies.schema import PolicyCreate
from app.models.policy import Policy
from app.core.dependencies import require_role
from app.db.session import get_db

router = APIRouter(prefix="/policies")

@router.post("")
def create_policy(
    data: PolicyCreate,
    user = Depends(require_role(["ADMIN"])),
    db=Depends(get_db)
):
    policy = Policy(
        category=data.category,
        max_amount=data.max_amount,
        max_claims=data.max_claims,
        time_window=data.time_window,
        created_by = user.id  # 👈 THIS IS THE FIX
    )
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return policy
