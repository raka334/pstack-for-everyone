---
name: architect
description: "Settle types, signatures, and module structure before code crosses a function boundary. Use for `architect`, design-this requests, or non-trivial changes where implementation would lock in the wrong shape."
---

# Architect

Produce a concrete design sketch before implementation. Explore alternatives when the design is not obvious.

## Steps

1. State the user goal and the boundary being designed.
2. Trace current callers, data shapes, and module ownership. Use `how` when the existing flow needs a walkthrough.
3. Name the proposed types, signatures, module responsibilities, and caller changes. Identify the invariant each choice protects.
4. If there are multiple credible shapes, use `arena` to compare them when the host supports delegation. Use independent agents only when exploration helps; provide each one the same boundary and evidence. If all configured agents inherit the parent model, disclose that.
5. Read the candidate designs and inspect their cited source. Return the sketch and tradeoffs. Stop before implementation unless the user's request explicitly asks you to continue.

## Output

Include the data shape, signatures, module ownership, caller migration, rejected alternative, and the unresolved decision if one remains.
