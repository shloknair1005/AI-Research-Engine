from app.db.session import SessionLocal
from app.models.agent_master import AgentMaster

def load_agents():
    try:
        db = SessionLocal()
        agents = db.query(AgentMaster).all()
        return agents
    except Exception as e:
        print(f"Error loading agents: {e}")
        return []