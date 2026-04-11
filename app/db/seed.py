from app.db.session import SessionLocal
from app.models.agent_master import AgentMaster
from app.models.agent_tool_mapping import AgentToolMapping
from app.models.tool_master import ToolMaster


db = SessionLocal()

agent = AgentMaster(agent_name="ResearchAgent", agent_type="Research", model_name="llama3.1 instant", temperature=0.2, max_tokens=1000, is_active=True, description="Finds research papers.")
tool = ToolMaster(tool_name="ArxivSearch", description="Search arxiv papers", tool_type="web_search", endpoint="https://api.arxiv.org/search")
agent_tool_mapping = AgentToolMapping(agent_id=1, tool_id=1)

db.add(agent)
db.add(tool)
db.add(agent_tool_mapping)

db.commit()