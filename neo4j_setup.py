from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="bolt://34.230.44.73:7687",
    username="neo4j",
    password="medicines-jewel-components"
)

result = graph.query("""
MATCH (m:Movie{title: 'Toy Story'}) 
RETURN m.title, m.plot, m.poster
""")

# print(result)

print(graph.schema)