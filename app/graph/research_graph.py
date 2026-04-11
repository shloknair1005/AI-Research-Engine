from langgraph.graph import START, StateGraph
from app.services.agent_loader import load_agents
from app.services.tool_loader import load_tools_for_agent

def build_graph():
    graph = StateGraph(dict)
    agents = load_agents()
    first_agent = None

    for agent in agents:
        tools = load_tools_for_agent(agent.id)

        def agent_node(state):
             print(f"Running {agent.agent_name}\nTools: {tools}")
             return state
        
        graph.add_node(agent.agent_name, agent_node)

        if not first_agent:
            first_agent = agent.agent_name
    
    graph.add_edge(START, first_agent)
    
    return graph.compile()