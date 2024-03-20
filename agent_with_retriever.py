from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from dotenv import load_dotenv

load_dotenv()

chat_llm = ChatOpenAI()

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

plot_retriever = RetrievalQA.from_llm(
    llm=chat_llm,
    retriever=movie_plot_vector.as_retriever()
)

result = plot_retriever.invoke(
    {"query": "A movie where a mission to the moon goes wrong"}
)

print(result)