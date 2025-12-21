from pydantic import BaseModel, EmailStr
from app.models.user import RoleEnum


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum


# ✅ ADD THIS
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
