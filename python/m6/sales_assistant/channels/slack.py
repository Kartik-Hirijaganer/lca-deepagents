# python/m6/sales_assistant/channels/slack.py
"""Puts the agent in Slack.

MDA provisions the Slack app itself during `mda deploy .` and walks you through
authorizing it for a workspace. There is no app to create and no token to copy.

Delete this file if you want to deploy without Slack.
"""

from managed_deepagents import channels

channel = channels.slack(
    name="chinook-sales-assistant",
    description="Answers questions about Chinook sales and drafts the weekly newsletter",
)
