#!/usr/bin/env bash
# Provisions the sandbox before its first use. MDA runs this once per sandbox.
set -euo pipefail

# The agent's analysis libraries. matplotlib is available but instructions.md
# tells the agent to answer in text, so it is here for when you want charts.
pip install --quiet --break-system-packages pandas matplotlib

# The Chinook sample database: the digital media store Jane Peacock sells against.
curl -sSL -o /tmp/chinook.db \
  https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite
mv /tmp/chinook.db chinook.db

# Where the agent writes finished deliverables.
mkdir -p artifacts
