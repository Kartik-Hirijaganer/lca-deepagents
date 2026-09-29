# python/m6/sales_assistant/agent.py
"""Chinook Sales Assistant, Managed Deep Agents version.

The self-hosted counterpart is python/m5/sales_assistant/. This is the managed
equivalent: no backend, store, or checkpointer to wire up, because the runtime
supplies all three. The Chinook database is provisioned into a per-thread
sandbox by sandbox/setup.sh rather than read from the repo.

Run locally with:
    mda dev

Deploy with:
    mda deploy .
"""

from langchain.tools import tool
from managed_deepagents import define_deep_agent


@tool
def email_report(to: str, subject: str, body: str) -> str:
    """Email a report to a stakeholder. This simulates a send, no network call is made."""
    return f"Emailed {to}: {subject}"


agent = define_deep_agent(
    name="chinook-sales-assistant",
    model="anthropic:claude-sonnet-5",
    tools=[email_report],
)
