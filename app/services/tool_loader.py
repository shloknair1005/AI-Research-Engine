from app.models.tool_master import ToolMaster
from app.db.session import SessionLocal
from app.models.agent_tool_mapping import AgentToolMapping

def load_tools_for_agent(agent_id):
    try:
        db = SessionLocal()

        tools = (
            db.query(ToolMaster)
            .join(AgentToolMapping)
            .filter(AgentToolMapping.agent_id == agent_id)
            .all()
        )
        return tools
    except Exception as e:
        print(f"Error loading tools for agent {agent_id}: {e}")
        return []
        
