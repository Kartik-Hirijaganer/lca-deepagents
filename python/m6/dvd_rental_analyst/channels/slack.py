# python/m6/dvd_rental_analyst/channels/slack.py
"""Lets people @mention the agent in Slack.

`channels.slack()` takes MDA runtime options only, no name or description. The
defaults are what you want for a first deploy, so the bare call is enough.

This is a bring-your-own-app channel: it needs a Slack app of your own. After
deploying, `mda channel add slack` generates a Slack app manifest for the
deployment, which you create the app from at api.slack.com/apps. Then put
SLACK_SIGNING_SECRET and SLACK_BOT_TOKEN in .env so the next deploy forwards
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
