# fix-gate

> **Status: results pending.** The experiment is being built. No numbers yet, and none are claimed.

## Your AI says it fixed the bug. Do you merge it?

Picture this. Your AI coding assistant sends you a fix. The tests are green. It looks fine.

You click merge.

Two days later the bug is back. Or a different bug shows up, and nobody connects it to that "fix."

A green test does not mean a correct fix.

**fix-gate is a small experiment that measures how often a wrong AI fix gets through, and which checks actually stop it.**

## The problem

More and more code is fixed by AI with little human review. That only works if something stands between "the AI wrote a patch" and "the patch goes live."

That something is a **gate**: a set of checks every patch must pass. But nobody tells you how good your gate is. Is it catching bad fixes? Is it blocking good ones? You can't tell by looking.

## What I do about it

1. Build a tiny to-do app (add, complete, delete).
2. Plant 6 bugs in it. Each bug is a different kind of trap.
3. Let an AI try to fix each bug 3 times. That is 18 attempts.
4. Check every fix by hand: is it actually right, or does it just look right?
5. Run each fix through 4 levels of checking, from "no gate" to "full gate."

Then count what happened.

## What you get

One table. Two numbers matter most:

- **Wrong fixes that shipped.** The dangerous ones.
- **Good fixes that got blocked.** The annoying ones.

A gate that blocks everything is safe and useless. A gate that blocks nothing is fast and reckless. The interesting question is where each check lands in between.

## Why this is not another benchmark

Other projects ask: can the AI solve the problem? Others ask: can an AI reviewer spot a problem?

This one asks: **should this patch be merged?** That is the decision a real team makes every day.

## How each attempt is judged

Every attempt gets two separate verdicts: is the fix correct (my manual review) and did the gate accept it. Together they put each attempt in one box:

| | Gate accepts | Gate rejects |
|---|---|---|
| **Fix is correct** | Good. Shipped. | False alarm. A good fix blocked. |
| **Fix is wrong** | **Danger. A wrong fix shipped.** | Good. Caught. |

An attempt that does not apply or crashes is counted as Invalid, on its own.

## Results

6 bugs x 3 attempts = 18 attempts per row.

| Gate level | Correct, accepted | Correct, rejected | Wrong, caught | Wrong, shipped | Invalid |
|---|---:|---:|---:|---:|---:|
| G0 No gate | pending | n/a | n/a | pending | pending |
| G1 Visible tests | pending | pending | pending | pending | pending |
| G2 + hidden tests | pending | pending | pending | pending | pending |
| G3 + no test edits | pending | pending | pending | pending | pending |

> 18 attempts is a small snapshot. Differences of 2 or 3 may be noise. This shows a method and an honest result, not a general benchmark.

## The honest part

If a wrong fix slips through, I will report it and explain why. A zero is not the goal. A true number is.

## How to run

```bash
make install
make run
```

Then open: `http://127.0.0.1:8000`

## Security

This app is for a local experiment. It has no login, permissions, or rate limiting.

**Do not deploy it publicly.** Run it only on your own computer.

## Limits

One small app, one model, three attempts per bug. One person wrote the bugs, hidden tests, rubrics and verdicts, so expect bias. Rubrics are committed before the first run to reduce it, not remove it.

Build details live in [DESIGN.md](DESIGN.md).
