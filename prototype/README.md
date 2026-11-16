# DataMan Text-Only Prototype (Module 4)

## What this prototype tests

**Product slice:** the first-release practice loop from `docs/product-backlog.md`:
answer a problem → get immediate feedback → retry with a visible attempt count →
see the correct answer after the last attempt → see results after the set.

| Story | Requirement | Covered here |
|---|---|---|
| US-01 Immediate correctness feedback | FR-2, NFR-1, NFR-2 | Yes |
| US-02 Show remaining attempts | FR-3, NFR-3 | Yes |
| US-03 Practice set results | FR-4 | Yes |
| US-04 Preserve state between sessions | FR-1 | Stubbed only (Deferred in backlog) |

**Design question:** Can the attempt rule (count, reveal, stop counting) and its
per-problem state live entirely in the business logic, so the interface only
displays results and the data layer only supplies problems and holds a session?
If so, the same logic can move to Flask in Module 5 without being rebuilt.

## Where things are

| Layer | File | Responsibility |
|---|---|---|
| Text interface | `app.py` | Reads input, prints prompts, feedback, and results. Holds all wording. |
| Business logic | `dataman/logic.py` | Checks answers, counts attempts, decides reveal, builds results. No input/print. |
| Stubbed data | `dataman/store.py` | Supplies a fixed practice set and holds the session in memory. |
| Logic tests | `tests/test_logic.py` | Runs the rules with no interface. |

## How to run

From this `prototype` folder:

```
python app.py
python -m unittest discover tests
```

## State the slice needs

All state is in one `PracticeSession` object (`logic.py`):

- `current_index`: which problem the learner is on
- `max_attempts`: the attempt limit for the set
- one `ProblemState` per problem: `attempts_used`, `solved`, `revealed`

Per-problem state is created when the session starts, not on the first answer,
so attempts remaining can be shown as soon as a problem appears (US-02 AC1).
Keeping attempts per problem (not one running counter) is what lets US-03
report attempts for each problem.

## Acceptance criteria demonstrated

Sample run (`12`, `abc`, `14`, `13`, `10`, `16`):

```
Problem: 7 + 5 = ?
Attempts remaining: 3
> CORRECT - Nice work.

Problem: 9 + 6 = ?
Attempts remaining: 3
> NOT A NUMBER - Please type a whole number. This did not use an attempt. Attempts remaining: 3
> INCORRECT - Try again. Attempts remaining: 2
> INCORRECT - Try again. Attempts remaining: 1
> INCORRECT - No attempts remain. The correct answer is 15.

Problem: 8 + 8 = ?
Attempts remaining: 3
> CORRECT - Nice work.

=== Practice set results ===
Correct: 2 of 3
  A1: 1 attempt(s) - correct
  A2: 3 attempt(s) - answer revealed
  A3: 1 attempt(s) - correct
```

- **US-01 AC1–AC3:** feedback appears before the next problem and states correct or incorrect.
- **US-01 AC5 (NFR-2):** every feedback line starts with a word label (CORRECT / INCORRECT). No color is used.
- **US-02 AC1–AC4:** attempts shown at the start, drop by one on each wrong answer, answer revealed on the last attempt, counting stops after a correct answer.
- **US-03 AC1–AC2:** results show the number correct and attempts per problem.
- **US-03 AC3:** `get_results()` raises `SetNotFinishedError` if the set is not done (tested in `tests/test_logic.py`).

The tests in `tests/test_logic.py` check the same criteria without using `app.py`.

## What the prototype confirmed

- The attempt rule fits completely in `logic.py`. `app.py` never compares answers or changes counts; it only maps outcome codes (`correct`, `incorrect_try_again`, `incorrect_revealed`, `invalid_input`) to text.
- The store can be swapped. A test builds a session from a different `InMemoryStore` and the logic works unchanged.
- US-01 and US-02 share the same state. Once attempts are counted, correctness feedback is no longer "no stored data" as written in US-01's effort note. The state is session-only, so the S estimate still holds.

## Revisions caused by testing

1. **Non-numeric input does not use an attempt.** Making the prototype run forced a decision the requirements do not cover: what happens when the learner types something that is not a number (like `abc`)? Counting it as a wrong answer is the simplest rule. A typo using up an attempt would recreate the confusion seen in E4 (learner not knowing why attempts were gone), so I added an `invalid_input` outcome that leaves attempts unchanged. This needs stakeholder confirmation.
2. **Outcome codes instead of messages in logic.** Logic returns a code and the numbers; `app.py` writes the wording. This keeps the NFR-2 text label decision in the interface, where Flask will need to make it again.

## Intentionally stubbed

- **Practice problems:** one fixed set of three addition problems in `store.py`. No problem generation.
- **Session state storage (US-04 / FR-1):** `save_session` / `load_session` exist but only keep data in memory. Typing `q` mid-set prints "Progress is not saved in this prototype." This is the deferred FR-1 gap, not a bug.
- **Learner identity:** the session key is the fixed string `"local"`. There are no accounts (Open Question 3).

## Unresolved

- **Attempt limit value:** E5 confirms a limit exists but no evidence gives the number. `DEFAULT_MAX_ATTEMPTS = 3` is a prototype value.
- **Invalid input rule:** see Revision 1; needs confirmation.
- **Keyboard access (NFR-1):** a text interface is keyboard-only, so this prototype cannot really test NFR-1. It must be tested again in the Flask version (focus order, feedback reachable without a mouse).
- **Saving state (FR-1):** still waits on Open Question 3 (how a learner is recognized).

## Handoff to Module 5

- **Carry forward unchanged:** `dataman/logic.py` and its tests. Flask routes should call `start_session`, `submit_answer`, `advance`, and `get_results` the same way `app.py` does.
- **Replace:** `app.py` with Flask routes/templates, keeping the text labels for NFR-2.
- **Next implementation question:** Where does `PracticeSession` live between web requests (Flask session, server memory, or a store), and does that choice need learner identity (Open Question 3) before US-04 can move forward?
