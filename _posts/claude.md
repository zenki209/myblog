# Claude Operational Guidelines

## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions).
- If something goes sideways, stop and re-plan immediately — do not keep pushing.
- Use plan mode for verification steps, not just implementation.
- Write detailed specifications upfront to reduce ambiguity.

### 2. Subagent Strategy
- Use subagents liberally to keep the main context window clean.
- Offload research, exploration, and parallel analysis to subagents.
- For complex problems, distribute computation via subagents.
- Assign one task per subagent for focused execution.

### 3. Self-Improvement Loop
- After ANY correction from the user, update `tasks/lessons.md` following the established pattern.
- Write rules to prevent repeating the same mistake.
- Ruthlessly iterate on lessons until the mistake rate drops.
- Review relevant lessons at the start of each session.

### 4. Verification Before Completion
- Never mark a task complete without proving it works.
- Diff behavior between main and changes when relevant.
- Ask: "Would a staff engineer approve this?"
- Run tests, check logs, and demonstrate correctness.

### 5. Demand Elegance (Balanced)
- For non-trivial changes, pause and ask: "Is there a more elegant way?"
- If a fix feels hacky: redesign with full context and implement the elegant solution.
- Skip this for simple, obvious fixes — do not over-engineer.
- Challenge your own work before presenting it.

### 6. Autonomous Bug Fixing
- When given a bug report, fix it without hand-holding.
- Identify logs, errors, and failing tests first — then resolve root causes.
- Require zero context switching from the user.
- Fix failing CI tests proactively.

---

## Task Management

1. **Plan First** — Write a plan in `tasks/todo.md` with checkable items.
2. **Verify Plan** — Confirm before starting implementation.
3. **Track Progress** — Mark items complete incrementally.
4. **Explain Changes** — Provide a high-level summary at each step.
5. **Document Results** — Add a review section to `tasks/todo.md`.
6. **Capture Lessons** — Update `tasks/lessons.md` after corrections.

---

## Core Principles

- **Simplicity First** — Make every change as simple as possible. Minimize code impact.
- **No Laziness** — Address root causes. Avoid temporary fixes. Maintain senior-level standards.
- **Minimal Impact** — Only modify what is necessary. Avoid introducing regressions.
