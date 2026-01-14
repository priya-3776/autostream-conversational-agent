import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from agent.graph import run_agent

state = {
    "message": "",
    "name": None,
    "email": None,
    "platform": None,
    "expecting": None,
    "reply": None
}

while True:
    user_input = input("User: ")

    if state["expecting"] == "name":
        state["name"] = user_input
        state["expecting"] = None
    elif state["expecting"] == "email":
        state["email"] = user_input
        state["expecting"] = None
    elif state["expecting"] == "platform":
        state["platform"] = user_input
        state["expecting"] = None
    else:
        state["message"] = user_input

    state = run_agent(state)
    print("Agent:", state["reply"])
