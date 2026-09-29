# python/m6/sales_assistant/channels/slack.py
"""Puts the agent in Slack.

`channels.slack()` takes MDA runtime options only, no name or description. The
defaults are what you want for a first deploy, so the bare call is enough.

This is a bring-your-own-app channel. Before it will work you need a Slack app
of your own (api.slack.com/apps) with these bot scopes:

    app_mentions:read, channels:history, chat:write, groups:history, im:history

then subscribe to the bot events you care about under Event Subscriptions, and
set SLACK_SIGNING_SECRET and SLACK_BOT_TOKEN in .env so the deploy forwards
them.

Delete this file to deploy without Slack.
"""

from managed_deepagents import channels

channel = channels.slack()

# Available options, all optional:
#
#   channels.slack(
#       auto_reply=True,                  # post the agent's reply back to Slack
#       mention_behavior="strip",         # or "preserve": keep the @mention in the text
#       conversation={
#           "app_mention": "thread",      # "thread" | "conversation" | "message"
#           "direct_message": "conversation",
#       },
#       filters={
#           "allow_shared_conversations": False,
#           # "include_conversations": [...], "exclude_users": [...], etc.
#       },
#   )
