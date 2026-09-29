# DVD Rental Analyst (Managed Deep Agents)

A data analyst for a DVD rental chain. It answers business questions by writing
SQL and Python against `sakila.db` in a managed sandbox, and it can produce a
Quarterly Business Review on demand.

This is the project Module 6 deploys. MDA supplies the backend, store, and
checkpointer, and the database is built inside a per-thread sandbox rather than
read from the repo.

> **Public beta.** MDA runs on LangSmith Cloud in the **US region only**. You
> need beta access and a LangSmith API key.

## What's here

| Path | What it does |
|---|---|
| `agent.py` | The agent definition: name, model, and the `email_report` tool |
| `instructions.md` | The system prompt, including the Sakila schema cheat sheet. Editable live in Context Hub |
| `sandbox/__init__.py` | `define_sandbox(scope="thread")` |
| `sandbox/setup.sh` | Installs pandas and matplotlib, then builds `sakila.db` |
| `skills/qbr-report/SKILL.md` | The QBR playbook. Also editable in Context Hub |
| `identity.py` | Who can call the deployment |
| `channels/slack.py` | Lets people `@mention` the agent in Slack. Needs your own Slack app; delete to deploy without it |
| `pyproject.toml` | Dependencies |

`sakila.db` is not in the repo. `sandbox/setup.sh` downloads the Sakila schema
and data from [jOOQ/sakila](https://github.com/jOOQ/sakila) and builds the
database in the sandbox on first use, so there is no 9 MB binary to check in.

## Setup

```bash
cd python/m6/dvd_rental_analyst
cp .env.example .env     # then fill in your keys
```

Install the SDK and CLI per the instructions in
[managed-deepagents-sdk](https://github.com/langchain-ai/managed-deepagents-sdk).

## Deploy it

```bash
mda deploy .
```

That prints an Agent Server URL and a LangSmith dashboard URL. Open the
dashboard URL, click **Connect**, then **Open in Studio** to chat with it.

`channels/slack.py` is the one piece that needs setup outside MDA. Run
`mda channel add slack` to generate a Slack app manifest for the deployment,
create the app from it at api.slack.com/apps, and put `SLACK_SIGNING_SECRET`
and `SLACK_BOT_TOKEN` in `.env`. Delete the file to deploy without Slack.

## Try these

- "What were our top 5 categories by revenue last quarter?"
- "Which store is doing better, and by how much?"
- "Generate the QBR."

Then edit `instructions.md` in Context Hub, add a persona, and ask the same
question again in the same chat. The tone changes with no redeploy.

## About the data

The public Sakila sample only contains English-language films and dates from
2005-2006. `sandbox/setup.sh` shifts all rental and payment dates forward so
"this quarter" resolves sensibly, spreads some films across French, Italian,
and Japanese, and cleans up a few `$0.00` comped payments. The numbers are
therefore not comparable to anyone else's Sakila queries; they are shaped for
a live demo.

## Tear down

```bash
mda delete .
```

Removes the deployment, its tracing project, its Context Hub repo, and any
sandboxes it created. Memory and thread history are not recoverable afterward.

Note that the deployment **name stays reserved for about 7 days** after a
delete. To redeploy sooner, use a different name:

```bash
mda deploy . --name dvd-rental-analyst-2
```

## Caveat

`define_deep_agent`, `define_sandbox`, `define_identity`, and
`auth.langsmith_api_key()` were checked against the SDK shipped in an `mda`
build and match. `channels.slack()` takes runtime options only, not
`name`/`description`.
