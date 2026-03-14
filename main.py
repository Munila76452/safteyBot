from src.rag import build_vector_db
from src.agent import run_agent


def main():

    print("Building vector database...")

    db = build_vector_db()

    print("Safety Bot Ready!")

    while True:

        question = input("\nAsk a question: ")

        if question == "exit":
            break

        answer = run_agent(question, db)

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()