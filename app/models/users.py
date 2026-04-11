"""
User Model

This table stores information about users who interact with the AI platform.

Users may:

Trigger AI agent workflows
Submit tasks
View outputs
Monitor agent runs

This table acts as a reference for multiple transactional tables like:

agent_runs
tasks
workflow_logs
"""

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    role = Column(String(50), default="user")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', role='{self.role}')>"