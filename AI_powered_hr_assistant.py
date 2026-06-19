"""
Docstring for Nestle_AI_powered_HR_assistant

"""
# 1 Imports Libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough
import gradio as gr


load_dotenv()

# 2 Load ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
     api_key="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", 
     temperature=0
)
# 3 Load PDF
loader = PyPDFLoader("the_nestle_hr_policy_pdf_2012.pdf")
documents = loader.load()
# print(documents[0].page_content)
# print(len(documents))
# print(documents[0].metadata)
# print(type(documents[0].page_content))


# 4 Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,     # characters per chunk
    chunk_overlap=200    # overlap between chunks
)

# 5 Split documents
split_docs = text_splitter.split_documents(documents)

# Check output
# print(len(split_docs))
# print(split_docs[1].page_content)
# print(split_docs[1].metadata)

# 6 Create embeddings
# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-large"  )
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# 7 Create Vectorstore
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    persist_directory="./chroma_hr_policy"
)

vectorstore.persist()

# 8 Create Retriever
# ===============================
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)
# 10 Format Retrieved Docs
def format_docs(docs):
    return "\n\n".join(
        f"[Page {d.metadata.get('page', 'N/A')}]\n{d.page_content}"
        for d in docs
    )

# 9 Create Prompt Template
# ===============================
prompt_template = """
You are an HR policy assistant for Nestlé.

Use the information provided in the context to answer the question.If the context is partially relevant, summarize the closest matching information.
If no relevant information is found, say:
"Sorry, the requested information is not available in the HR policy document."

Answer in clear, professional and simple language.

Context:
{context}

Question:
{question}

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)


# 11 LCEL RAG Chain 
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | PROMPT
    | model
    | StrOutputParser()
)

# 12 Ask Questions (Chatbot)

# while True:
#     query = input("\nAsk a question (or type 'exit'): ")

#     if query.lower() == "exit":
#         break

#     response =  rag_chain.invoke(query)

#     print("\nANSWER:")
#     print(response)

    # print("\nSOURCE PAGES:")
    # for doc in response["source_documents"]:
    #     print(doc.metadata)
# 12 Chat function
def chat_fn(message, history):
    response = rag_chain.invoke(message)
    return response

#13 Create Chat UI

custom_css = """
h1 {
    font-size: 42px !important;
    text-align: center;
}
p {
    font-size: 18px !important;
}
"""
with gr.Blocks(css=custom_css) as demo:
    gr.ChatInterface(
        fn=chat_fn,
        title="Nestlé HR Policy Chatbot",
        description="Chat with the Nestlé HR Policy PDF (RAG-based chatbot)"
    )

demo.launch()
