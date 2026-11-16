"""Business logic layer for the DataMan practice loop.

Traces to:
- US-01 / FR-2  immediate correctness feedback
- US-02 / FR-3  attempts remaining, reveal on last incorrect attempt
- US-03 / FR-4  results after a completed practice set

Rules here do not print, read input, or know where data is stored.
They take plain values and return plain values, so any interface
(text now, Flask later) can call them.
"""

from dataclasses import dataclass, field

# The 1977 manual (E5) confirms an attempt limit exists but the evidence
# does not state the number. 3 is a prototype value, not a confirmed
# requirement. See README "Unresolved".
DEFAULT_MAX_ATTEMPTS = 3

# Outcome codes returned to the interface. The interface decides the
# wording; the logic decides the meaning.
CORRECT = "correct"
INCORRECT_TRY_AGAIN = "incorrect_try_again"
INCORRECT_REVEALED = "incorrect_revealed"
INVALID_INPUT = "invalid_input"


@dataclass(frozen=True)
class Problem:
    problem_id: str
    prompt: str
    answer: int


@dataclass
class ProblemState:
    """State for one problem. Kept per problem so results (US-03) and a
    future resume feature (US-04) can read it without re-running the set."""
    problem_id: str
    attempts_used: int = 0
    solved: bool = False
    revealed: bool = False

    @property
    def finished(self) -> bool:
        return self.solved or self.revealed


@dataclass
class PracticeSession:
    """All state the selected slice needs. Nothing else holds state."""
    set_id: str
    problems: list
    max_attempts: int = DEFAULT_MAX_ATTEMPTS
    current_index: int = 0
    states: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Feedback:
    outcome: str
    attempts_remaining: int
    correct_answer: int | None = None   # only set when revealed


@dataclass(frozen=True)
class SetResults:
    total_problems: int
    correct_count: int
    attempts_by_problem: list           # list of (problem_id, attempts_used, solved)


class SetNotFinishedError(Exception):
    """Raised when results are requested before the set is complete (US-03 AC3)."""


def start_session(set_id, problems, max_attempts=DEFAULT_MAX_ATTEMPTS):
    if not problems:
        raise ValueError("A practice set needs at least one problem.")
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1.")
    session = PracticeSession(set_id=set_id, problems=list(problems),
                              max_attempts=max_attempts)
    # State exists before the first answer so attempts remaining can be
    # shown when a problem first appears (US-02 AC1).
    for p in session.problems:
        session.states[p.problem_id] = ProblemState(problem_id=p.problem_id)
    return session


def current_problem(session):
    if is_set_finished(session):
        return None
    return session.problems[session.current_index]


def attempts_remaining(session, problem_id=None):
    if problem_id is None:
        problem = current_problem(session)
        if problem is None:
            return 0
        problem_id = problem.problem_id
    state = session.states[problem_id]
    if state.finished:
        return 0
    return session.max_attempts - state.attempts_used


def parse_answer(raw):
    """Return an int, or None if the text is not a whole number."""
    text = str(raw).strip()
    try:
        return int(text)
    except ValueError:
        return None


def submit_answer(session, raw_answer):
    """Check one answer for the current problem and update its state.

    Revision found by running the prototype: non-numeric input does NOT
    use an attempt. See README "Revisions caused by testing".
    """
    problem = current_problem(session)
    if problem is None:
        raise SetNotFinishedError("The practice set is already finished.")

    state = session.states[problem.problem_id]
    value = parse_answer(raw_answer)

    if value is None:
        return Feedback(INVALID_INPUT, attempts_remaining(session))

    state.attempts_used += 1

    if value == problem.answer:
        state.solved = True                     # US-02 AC4: stop counting
        return Feedback(CORRECT, 0)

    if state.attempts_used >= session.max_attempts:
        state.revealed = True                   # US-02 AC3: reveal
        return Feedback(INCORRECT_REVEALED, 0, correct_answer=problem.answer)

    return Feedback(INCORRECT_TRY_AGAIN,        # US-02 AC2: one fewer
                    session.max_attempts - state.attempts_used)


def advance(session):
    """Move to the next problem once the current one is finished."""
    problem = current_problem(session)
    if problem is not None and session.states[problem.problem_id].finished:
        session.current_index += 1


def is_set_finished(session):
    return session.current_index >= len(session.problems)


def get_results(session):
    """US-03: results only after every problem is finished."""
    if not is_set_finished(session):
        raise SetNotFinishedError("Results are shown only after the set is complete.")
    rows = []
    for p in session.problems:
        s = session.states[p.problem_id]
        rows.append((p.problem_id, s.attempts_used, s.solved))
    correct = sum(1 for _, _, solved in rows if solved)
    return SetResults(total_problems=len(rows), correct_count=correct,
                      attempts_by_problem=rows)
