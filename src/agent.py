# from src.router import route_question
# from src.rag import retrieve_context
# from src.csv_tools import get_baseline_data
# from src.llm import ask_llm


# def run_agent(question, db):

#     route = route_question(question)

#     txt_context = ""
#     csv_data = ""

#     if route == "TXT":

#         txt_context = retrieve_context(db, question)

#     elif route == "CSV":

#         csv_data = get_baseline_data(question)

#     else:

#         txt_context = retrieve_context(db, question)
#         csv_data = get_baseline_data(question)

#     prompt = f"""
# You are a construction safety assistant.

# User Question:
# {question}

# TXT Context:
# {txt_context}

# CSV Data:
# {csv_data}

# Answer the question using the evidence.
# Always mention sources if possible.
# """

#     answer = ask_llm(prompt)

#     return answer

import re

from src.router import route_question
from src.rag import retrieve_context
from src.csv_tools import get_baseline_data, get_monthly_data
from src.llm import ask_llm


def extract_topic(question):

    topics = [
        "Confined Space",
        "Permit to Work",
        "Work at Height",
        "Excavation",
        "Weekly Safety Inspections"
    ]

    for t in topics:
        if t.lower() in question.lower():
            return t

    return None


def extract_month(question):

    match = re.search(r"\d{4}-\d{2}", question)

    if match:
        return match.group()

    return None


def run_agent(question, db):

    route = route_question(question)

    topic = extract_topic(question)
    month = extract_month(question)

    txt_context = ""
    csv_data = ""

    if route == "TXT":

        txt_context = retrieve_context(db, question)

    elif route == "CSV":

        csv_data = get_baseline_data(topic)

    else:

        txt_context = retrieve_context(db, question)

        if month:
            csv_data = get_monthly_data(topic, month)
        else:
            csv_data = get_baseline_data(topic)

    prompt = f"""
You are a construction safety assistant.

Question:
{question}

Topic:
{topic}

TXT Context:
{txt_context}

CSV Data:
{csv_data}

Answer clearly using the evidence.
Mention topic_id and month if available.
"""

    return ask_llm(prompt)