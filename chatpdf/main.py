from .models.agent import LangChainAgent
import os

def main():
    path = input("Enter a path: ")
    base_path = os.path.dirname(os.path.abspath(__file__)) + path

    if not os.path.exists(base_path):
        print("Path do not exists")

        return

    if os.path.isdir(base_path) or not path.endswith('.pdf'):
        print("Path is not a pdf file")

        return

    agent = LangChainAgent(base_path)

    agent.load()

    while True:
        query = input("Enter a query (if you want to exit type 'exit'): ")

        if query == "exit":
            break

        output = agent.query(query)

        print(output)
