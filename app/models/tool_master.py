from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.base import Base

class ToolMaster(Base):

# Defines tools that AI agents can use.

# Examples:
# - web_search
# - calculator
# - database_query
# - python_executor


    __tablename__ = "tool_master"

    id = Column(Integer, primary_key=True, index=True)

    tool_name = Column(String(100), unique=True, nullable=False)

    description = Column(String(500))

    tool_type = Column(String(50))

    endpoint = Column(String(200))

    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ToolMaster(tool_name='{self.tool_name}')>"

