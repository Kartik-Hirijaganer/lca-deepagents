# python/m6/sales_assistant/identity.py
"""Who is allowed to call this deployment.

Optional on its own. It becomes necessary once a channel needs to attribute an
inbound message to someone, which is why identity.py and channels/ go together.

auth.langsmith_api_key() verifies a caller's LangSmith workspace API key.
Everyone holding that key shares the same threads.
"""

from managed_deepagents import auth, define_identity

identity = define_identity(auth=auth.langsmith_api_key())
