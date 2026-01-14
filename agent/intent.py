def detect_intent(message: str):
    msg = message.lower()

    # HIGH INTENT FIRST (important)
    if any(word in msg for word in ["want to", "try", "sign up", "get started"]):
        return "high_intent"

    # Greeting
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "greeting"

    # Product / pricing
    if any(word in msg for word in ["price", "pricing", "plan", "cost", "features"]):
        return "product_query"

    return "unknown"
