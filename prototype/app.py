"""Text interface layer for the DataMan prototype (entry point).

Run from the prototype folder:
    python app.py

This file only reads input, calls dataman.logic, and prints output.
It does not decide whether an answer is correct, count attempts, or
store data.
"""

from dataman import logic
from dataman.store import InMemoryStore

SET_ID = "addition-1"

# Every feedback line starts with a word label so meaning never depends
# on color (NFR-2). The prototype prints no color at all.
MESSAGES = {
    logic.CORRECT: "CORRECT - Nice work.",
    logic.INCORRECT_TRY_AGAIN: "INCORRECT - Try again. Attempts remaining: {remaining}",
    logic.INCORRECT_REVEALED: ("INCORRECT - No attempts remain. "
                               "The correct answer is {answer}."),
    logic.INVALID_INPUT: ("NOT A NUMBER - Please type a whole number. "
                          "This did not use an attempt. Attempts remaining: {remaining}"),
}


def format_feedback(feedback):
    return MESSAGES[feedback.outcome].format(
        remaining=feedback.attempts_remaining,
        answer=feedback.correct_answer,
    )


def format_results(results):
    lines = ["", "=== Practice set results ===",
             f"Correct: {results.correct_count} of {results.total_problems}"]
    for problem_id, attempts, solved in results.attempts_by_problem:
        status = "correct" if solved else "answer revealed"
        lines.append(f"  {problem_id}: {attempts} attempt(s) - {status}")
    return "\n".join(lines)


def run(input_fn=input, output_fn=print, store=None):
    store = store or InMemoryStore()
    session = logic.start_session(SET_ID, store.get_practice_set(SET_ID))
    store.save_session("local", session)   # STUB: in-memory only

    output_fn(f"DataMan practice: {SET_ID} ({len(session.problems)} problems)")
    output_fn("Type your answer and press Enter. Type q to quit.")

    while not logic.is_set_finished(session):
        problem = logic.current_problem(session)
        output_fn("")
        output_fn(f"Problem: {problem.prompt} = ?")
        output_fn(f"Attempts remaining: {logic.attempts_remaining(session)}")

        while not session.states[problem.problem_id].finished:
            try:
                raw = input_fn("> ")
            except EOFError:
                raw = "q"
            if raw.strip().lower() == "q":
                # FR-1 / US-04 is deferred: quitting loses progress.
                output_fn("Practice stopped. Progress is not saved in this prototype.")
                return session
            feedback = logic.submit_answer(session, raw)
            output_fn(format_feedback(feedback))

        logic.advance(session)

    output_fn(format_results(logic.get_results(session)))
    return session


if __name__ == "__main__":
    run()
