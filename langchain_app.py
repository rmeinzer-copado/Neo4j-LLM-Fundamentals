from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

# llm = OpenAI(
#     model="gpt-3.5-turbo-instruct",
#     temperature=0
# )

# response = llm.invoke("What is Neo4j?")

# print(response)

from langchain.prompts import PromptTemplate

# template = PromptTemplate(template="""
# You are a cockney fruit and vegetable seller.
# Your role is to assist your customer with their fruit and vegetable needs.
# Respond using cockney rhyming slang.

# Tell me about the following fruit: {fruit}
# """, input_variables=["fruit"])

# response = llm.invoke(template.format(fruit="apple"))

# print(response)

from langchain.chains import LLMChain
from langchain.schema import StrOutputParser
from langchain.output_parsers.json import SimpleJsonOutputParser

template = PromptTemplate.from_template("""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Output JSON as {{"description": "your response here"}}

Tell me about the following fruit: {fruit}
""")

llm_chain = LLMChain(
    llm=llm,
    prompt=template,
    # output_parser=StrOutputParser()
    output_parser=SimpleJsonOutputParser()
)

response = llm_chain.invoke({"fruit": "apple"})

print(response)