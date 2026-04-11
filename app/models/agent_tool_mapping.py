from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class AgentToolMapping(Base):

# Maps which tools an agent can use.

# Example:
# research_agent -> web_search
# executor_agent -> python_executor

    __tablename__ = "agent_tool_mapping"

    id = Column(Integer, primary_key=True, index=True)

    agent_id = Column(Integer, ForeignKey("agent_master.id"), nullable=False)

    tool_id = Column(Integer, ForeignKey("tool_master.id"), nullable=False)

    agent = relationship("AgentMaster")
    tool = relationship("ToolMaster")

