def route_question(question):

    q = question.lower()

    if "risk" in q or "score" in q or "trir" in q:
        return "CSV"

    if "2025" in q or "month" in q:
        return "CSV"

    if "owner" in q or "fields" in q or "focus" in q:
        return "TXT"

    return "HYBRID"