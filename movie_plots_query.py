from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from dotenv import load_dotenv

load_dotenv()

embedding_provider = OpenAIEmbeddings()

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://34.230.44.73:7687",
    username="neo4j",
    password="medicines-jewel-components",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

result = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.", k=1)
for doc in result:
    print(doc.metadata["title"], "-", doc.page_content)