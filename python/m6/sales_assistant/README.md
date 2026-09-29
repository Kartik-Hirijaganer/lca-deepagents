# Chinook Sales Assistant (Managed Deep Agents)

The managed counterpart to `python/m5/sales_assistant/`. Same job, different
infrastructure: MDA supplies the backend, store, and checkpointer, and the
Chinook database is downloaded into a per-thread sandbox instead of being read
from the repo.

> **Public beta.** MDA runs on LangSmith Cloud in the **US region only**. You
> need beta access and a LangSmith API key.

## What's here

| Path | What it does |
|---|---|
| `agent.py` | The agent definition: name, model, and the `email_report` tool |
| `instructions.md` | The system prompt. Editable live in Context Hub |
| `sandbox/__init__.py` | `define_sandbox(scope="thread")` |
| `sandbox/setup.sh` | Installs pandas and matplotlib, downloads `chinook.db`, creates `artifacts/` |
| `skills/weekly-newsletter/SKILL.md` | The newsletter playbook. Also editable in Context Hub |
| `identity.py` | Who can call the deployment |
| `channels/slack.py` | Lets people `@mention` the agent in Slack. Needs your own Slack app; delete to deploy without it |
| `pyproject.toml` | Dependencies |

## Setup

```bash
cd python/m6/sales_assistant
cp .env.example .env     # then fill in your keys
```

Install the SDK and CLI per the instructions in
[managed-deepagents-sdk](https://github.com/langchain-ai/managed-deepagents-sdk).

## Run it locally

```bash
mda dev
```

## Deploy it

```bash
mda deploy .
```

That prints an Agent Server URL and a LangSmith dashboard URL.

`channels/slack.py` is the one piece that needs setup outside MDA: create a
Slack app at api.slack.com/apps, give its bot `app_mentions:read`,
`channels:history`, `chat:write`, `groups:history`, `im:history`, subscribe to
`app_mention` under Event Subscriptions, and put `SLACK_SIGNING_SECRET` and
`SLACK_BOT_TOKEN` in `.env`. Delete the file to deploy without Slack.

## Try these

- "What were our top 5 genres by revenue?"
- "Which of Jane's customers spent the most last year?"
- "Draft the weekly newsletter."

Then edit `instructions.md` in Context Hub, add a persona, and ask the same
question again in the same chat. The tone changes with no redeploy.

## Tear down

```bash
mda delete .
```

Removes the deployment, its tracing project, its Context Hub repo, and any
sandboxes it created. Memory and thread history are not recoverable afterward.

## Caveat

`define_deep_agent`, `define_sandbox`, `define_identity`, and
`auth.langsmith_api_key()` were checked against the SDK shipped in an `mda`
build and match. `channels.slack()` was corrected after a deploy failed: it
takes runtime options only, not `name`/`description`.

The rest of the project still hasn't been run end to end, so an agent turn,
the sandbox setup, or the skill may need adjusting on first contact.
