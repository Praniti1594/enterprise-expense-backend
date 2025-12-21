# app/approvals/schemas.py
from pydantic import BaseModel

class ApprovalRequest(BaseModel):
    decision: str  # APPROVED or REJECTED
    remarks: str | None = None
