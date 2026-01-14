def get_rag_answer(query: str):
    query = query.lower()

    with open("data/knowledge_base.md", "r", encoding="utf-8") as f:
        content = f.read().lower()

    # Pricing related
    if "price" in query or "pricing" in query or "plan" in query:
        start = content.find("## pricing")
        end = content.find("## policies")
        return content[start:end].strip()

    # Policy related
    if "refund" in query or "support" in query or "policy" in query:
        start = content.find("## policies")
        return content[start:].strip()

    return "I can help you with pricing, plans, or policies. What would you like to know?"
