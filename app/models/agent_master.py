from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from datetime import datetime

from app.db.base import Base

class AgentMaster(Base):

# Defines AI agents available in the system.
# Each agent represents a specialized AI worker
# (planner, researcher, executor, validator, etc.)


    __tablename__ = "agent_master"

    id = Column(Integer, primary_key=True, index=True)

    agent_name = Column(String(100), unique=True, nullable=False)
    agent_type = Column(String(50), nullable=False)

    description = Column(String(500))

    model_name = Column(String(100), nullable=False)

    temperature = Column(Float, default=0.7)
    max_tokens = Column(Integer, default=1000)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AgentMaster(agent_name='{self.agent_name}')>"

