# -composio-research
# Composio App Research Agent

Research agent that analyzes 100 apps for AI agent buildability.

## Stack
- Composio SDK (composio-core) for toolkit initialization
- Groq API (Llama 3.3 70B) as the LLM research brain
- Python 3.12 required (composio-core incompatible with Python 3.13)

## How to run

1. Install dependencies:
   py -3.12 -m pip install composio-core groq

2. Add your API keys in research_agent_final.py:
   GROQ_API_KEY = "your_groq_key"
   COMPOSIO_API_KEY = "your_composio_key"

3. Run:
   py -3.12 research_agent_final.py

4. Output saved to results.json and results.csv

## Results
Live report: https://nals15.github.io/-composio-research

## Findings
- 82/100 apps ready to build today
- OAuth2 dominates auth across all categories
- Developer Infra is the easiest category (10/10 self-serve)
- Finance/Fintech is the hardest (gated access, subscription walls)
- 80% accuracy verified on 15-app human spot-check
