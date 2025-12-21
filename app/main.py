from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.expenses.router import router as expense_router
from app.policies.router import router as policy_router
from app.approvals.router import router as approval_router
from app.analytics.router import router as analytics_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS
    allow_headers=["*"],  # allow Authorization header
)


app.include_router(auth_router)
app.include_router(expense_router)
app.include_router(policy_router)
app.include_router(approval_router)
app.include_router(analytics_router)