---
name: recall
description: "Rebuild recent working context on a topic from the current conversation and user-provided records. Use for catch-me-up, where-did-I-leave-off, or before resuming a task."
---

# Recall

Reconstruct only what the current conversation, visible project state, or user-provided records support. Do not assume a private transcript path or search other workspaces' conversation logs.

1. If the user names a specific prior task, use the session-pickup playbook rather than guessing from broad history.
2. Search the current repository for task notes, decision logs, relevant commits, branches, and open diffs.
3. Use prior conversation context only when it is available in the current session. If a transcript is needed and not visible, ask the user for its path or contents.
4. Separate completed work, current state, decisions, open risks, and next actions. Link local evidence.
5. Do not turn a context summary into permission for external writes or other actions.
