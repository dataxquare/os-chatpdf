from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

class LangChainAgent:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc_search = None
    
    def load(self):
        loader = UnstructuredPDFLoader(self.pdf_path)
        pages = loader.load_and_split()
        embeddings = OpenAIEmbeddings()

        self.doc_search = Chroma.from_documents(pages, embeddings).as_retriever()

    def query(self, query: str):
        docs = self.doc_search.get_relevant_documents(query)

        chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
        
        output = chain.run(input_documents=docs, question=query)
        
        return output