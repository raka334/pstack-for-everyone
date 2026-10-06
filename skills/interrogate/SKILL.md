---
name: interrogate
description: "Adversarially review a diff for correctness, security, regressions, and missing coverage. Use for `interrogate`, multi-agent review, challenge-this, or requests to find blind spots."
---

# Interrogate

The deliverable is a synthesized review verdict. Do not auto-apply changes.

## Step 1. Determine scope

Use the caller's files or diff. Otherwise inspect the current working diff against its base branch and gather only the context needed to review it.

## Step 2. State intent

Derive the intended behavior from the user's request, any PR description, and the code. State the intended behavior in one paragraph. If it is genuinely ambiguous, identify the ambiguity and its impact.

## Step 3. Review independently

Read `references/reviewer-prompt.md`, `references/rubric.md`, and `references/code-quality-review.md`. Give the same intent, patch, context, and rubric to independent read-only agents when the host supports delegation. Ask reviewers to report only actionable findings with file and line references, trigger conditions, impact, and evidence. Use a configured comment-focused reviewer only when one is available.

When several configured agent profiles use distinct models, use them for model diversity. Otherwise treat the results as independent passes from the same model. If delegation is unavailable, do separate review passes yourself and disclose the limitation.

Do not ask reviewers to change files. Do not widen the review beyond the supplied change and its necessary context.

## Step 4. Synthesize

Deduplicate findings, distinguish consensus from single-reviewer findings, and inspect every cited path yourself. Categorize each finding as Act on, Consider, Noted, or Dismissed. Give a one-line evidence-based reason for the disposition.

## Output

Return Intent, Reviewers, Act On, Consider, Noted, Dismissed, and Agreement Map. Each finding includes exact location, impact, trigger, and disposition. If there are no findings, say what scope you reviewed and what the review could not establish.
