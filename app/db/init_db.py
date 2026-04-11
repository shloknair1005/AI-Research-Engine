from app.db.session import engine
from app.db.base import Base

# register models
from app.models.users import User
from app.models.agent_master import AgentMaster
from app.models.tool_master import ToolMaster
from app.models.agent_tool_mapping import AgentToolMapping


def init_db():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()