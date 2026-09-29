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
| `channels/slack.py` | Puts the agent in Slack. Delete to deploy without it |
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

That prints an Agent Server URL and a LangSmith dashboard URL. With
`channels/slack.py` present, the deploy also walks you through authorizing the
Slack app.

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

This project was written to match Module 6's lessons, which are a conceptual
tour rather than a tested lab. The MDA API surface here has not been executed
against a real install, so treat the first `mda dev` as a test of the lesson
code as much as of the project. The package name in `pyproject.toml` and the
`managed_deepagents` import paths are the most likely things to need
correcting; check them against the SDK repo.
