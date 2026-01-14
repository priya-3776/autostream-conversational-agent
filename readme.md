# AutoStream Conversational AI Agent

## Overview
This project implements a conversational AI agent that converts user conversations into qualified leads for AutoStream, a SaaS video editing platform.

## Architecture
LangGraph was chosen for deterministic control over agent flow and clean state management. The agent uses intent detection to route conversations and Retrieval-Augmented Generation (RAG) to fetch accurate pricing and policy information from a local knowledge base. State is maintained across multiple conversation turns to ensure proper lead qualification. Tool execution is gated and triggered only when all required user details are collected.

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Set your OpenAI API key:
   export OPENAI_API_KEY=your_key
3. Run:
   python main.py

## WhatsApp Integration
To integrate with WhatsApp, the agent would be wrapped in a FastAPI service. Incoming WhatsApp messages would be received via Meta Webhooks and passed to the agent. The agent’s response would then be sent back using the WhatsApp Business API. State can be persisted using Redis or a database per user session.

## Demo
The demo video shows pricing inquiry, high-intent detection, user detail collection, and successful lead capture.
