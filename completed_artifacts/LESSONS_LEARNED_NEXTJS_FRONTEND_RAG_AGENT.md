### Lessons Learned: Next.js Frontend RAG Agent Creation

- **Index Generation Script Issues:** The `generate_agent_index.py` script proved destructive when run, corrupting `agent_profiles/README.md`. It failed to properly parse complex markdown, removing essential elements like `+++DCCDSchemaGuard` and truncating sentences incorrectly.
- **Manual Workaround:** To avoid further corruption, I bypassed the index generation script and manually appended the new agent's details to the end of `agent_profiles/README.md`.
- **Recommendation:** The `generate_agent_index.py` script needs significant revision. It should be refactored to handle edge cases, perhaps using an established markdown parsing library instead of custom regex rules that prove too brittle.
