from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.models.base import Base
import enum

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(120), unique=True)
    password_hash = Column(String(255))
    role = Column(Enum(RoleEnum))
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
