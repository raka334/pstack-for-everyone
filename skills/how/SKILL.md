---
name: how
description: "Explain how a subsystem works, trace runtime flow, or identify package ownership and layering. Use for how-does-it-work questions and code walkthroughs before a change."
---

# How

Explain the real implementation from evidence. Do not invent intended behavior from names or comments.

## Steps

1. Identify the user's question and the smallest useful scope.
2. Inspect the entry point, the data flow, and the owning modules. Follow calls only as far as needed to answer.
3. For a simple question, trace and explain directly. For a complex subsystem, delegate distinct read-only exploration angles to agents when the host supports it. Give each a bounded question and ask for file and symbol evidence. If delegation is unavailable, inspect the angles sequentially.
4. Read the referenced files yourself before relying on a delegate's report. Resolve disagreements against the code.
5. Explain the subsystem in the sections below that apply. Keep the path concrete and distinguish observed behavior from inference.

## Output format

Use these sections as needed: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
