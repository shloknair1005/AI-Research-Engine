from app.graph.research_graph import build_graph

if __name__ == "__main__":
    graph = build_graph()
    graph.invoke({"query": "latest research on AI in healthcare"})