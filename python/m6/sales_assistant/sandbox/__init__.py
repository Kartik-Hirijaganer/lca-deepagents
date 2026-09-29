# python/m6/sales_assistant/sandbox/__init__.py
"""Sandbox declaration.

scope="thread" gives each conversation its own sandbox, created on the first
run and reused by follow-up turns, so later questions build on earlier work.
setup.sh runs once, before the sandbox's first use.
"""

from managed_deepagents import define_sandbox

sandbox = define_sandbox(scope="thread")
