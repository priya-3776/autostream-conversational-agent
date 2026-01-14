from agent.intent import detect_intent
from agent.rag import get_rag_answer
from agent.tools import mock_lead_capture

def run_agent(state: dict):
    message = state["message"]
    intent = detect_intent(message)

    # Greeting
    if intent == "greeting":
        state["reply"] = "Hi! How can I help you today?"
        return state

    # Product / pricing query
    if intent == "product_query":
        state["reply"] = get_rag_answer(message)
        return state

    # High intent flow
    if intent == "high_intent":
        if state["name"] is None:
            state["reply"] = "Great! What's your name?"
            state["expecting"] = "name"
            return state

        if state["email"] is None:
            state["reply"] = "Thanks! Please share your email."
            state["expecting"] = "email"
            return state

        if state["platform"] is None:
            state["reply"] = "Which platform do you create content on?"
            state["expecting"] = "platform"
            return state

        mock_lead_capture(state["name"], state["email"], state["platform"])
        state["reply"] = "✅ You're all set! Our team will contact you."
        return state

    state["reply"] = "Could you please clarify?"
    return state
