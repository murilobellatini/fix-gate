# DESIGN: fix-gate (v15)

This file tells the builder what to do next. It is never given to the fixing agent.

## Current state

The minimal app exists.

- FastAPI backend in `app/main.py`.
- Browser UI in `app/static/index.html`.
- Tasks are stored in memory.
- `make install` installs dependencies and Chromium.
- `make run` starts the app at `http://127.0.0.1:8000`.
- `make test` runs tests in `tests/`.

## Next work

Build in this order:

1. Create `tests/visible/logic/test_app.py` with tests for add, complete, delete, empty title, and deleting the correct task.
2. Create `cases/bug-1/` with:
   - `bug.patch`: makes delete remove the wrong item.
   - `known-good.patch`: the correct fix.
   - `rubric.md`: one line saying that delete must remove only the task with the given ID.
3. Create `quality_gate/run_gate.py`.
4. The gate must support G0 to G3 only.

## Gate levels

| Level | Rule |
|---|---|
| G0 | Patch applies and the app starts. |
| G1 | All visible logic and Playwright tests pass. |
| G2 | All hidden logic and Playwright tests also pass. |
| G3 | G2, plus reject any patch that edits `SPEC.md` or anything under `tests/`. |

Do not implement G4.

## Rules

- The fixing agent receives only `SPEC.md`, the failing test output, and one relevant source file.
- It never receives `DESIGN.md`, `cases/`, `quality_gate/`, or anything under `tests/hidden/`.
- Every run must be logged.
- The results table must be generated from the log.
- Each result row must contain 18 attempts: 6 bugs times 3 attempts.
- Rubrics, bug patches, and hidden tests must be committed before the first agent run.
- Do not change them after the first run.

## Done for this milestone

- `make install` works.
- `make run` starts the app.
- The UI can add, complete, and delete tasks.
- Empty or whitespace-only titles are rejected.
- The next commit adds visible logic tests and `cases/bug-1`.
