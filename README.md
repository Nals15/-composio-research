# -composio-research
# Composio App Research Agent

Research agent that analyzes 100 apps for AI agent buildability using Groq API.

## What it does
Automatically researches auth methods, API surface, self-serve vs gated access, and buildability verdict for 100 apps across 10 categories.

## How to run

1. Install dependencies:
   pip install groq

2. Add your API keys in research_agent_v4.py:
   GROQ_API_KEY = "your_groq_key"
   COMPOSIO_API_KEY = "your_composio_key"

3. Run:
   python research_agent_v4.py

4. Output saved to results.json and results.csv

## Results
Live report: https://nals15.github.io/-composio-research

## Stack
- Groq API (Llama 3.3 70B)
- Python 3.13
- 100 apps, ~5 min runtime, 80% verified accuracy
