# python/m6/dvd_rental_analyst/channels/slack.py
"""Lets people @mention the agent in Slack.

`channels.slack()` takes MDA runtime options only, no name or description. The
defaults are what you want for a first deploy, so the bare call is enough.

You do not build the Slack app yourself. With this file present, `mda deploy`
prints an authorization link near the end; approve it against your workspace
and LangSmith creates the app, installs it, and points its Events endpoint at
the deployment. The bot token is stored as a workspace connection
(`mda connections list`), so nothing goes in .env.

Press Enter at that prompt to skip it; the deploy finishes with Slack events
disabled and you can authorize on a later deploy.
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
