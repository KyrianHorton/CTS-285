"""Tests that run the business rules with no text interface.

Run from the prototype folder:
    python -m unittest discover tests
"""

import unittest

from dataman import logic
from dataman.logic import Problem
from dataman.store import InMemoryStore

PROBLEMS = [Problem("P1", "2 + 2", 4), Problem("P2", "3 + 3", 6)]


def new_session(max_attempts=3):
    return logic.start_session("test", PROBLEMS, max_attempts=max_attempts)


class US01CorrectnessFeedback(unittest.TestCase):
    def test_correct_answer_reports_correct(self):
        fb = logic.submit_answer(new_session(), "4")
        self.assertEqual(fb.outcome, logic.CORRECT)

    def test_incorrect_answer_reports_incorrect(self):
        fb = logic.submit_answer(new_session(), "5")
        self.assertEqual(fb.outcome, logic.INCORRECT_TRY_AGAIN)


class US02RemainingAttempts(unittest.TestCase):
    def test_attempts_visible_before_first_answer(self):
        self.assertEqual(logic.attempts_remaining(new_session()), 3)

    def test_incorrect_answer_decreases_attempts_by_one(self):
        s = new_session()
        fb = logic.submit_answer(s, "5")
        self.assertEqual(fb.attempts_remaining, 2)
        self.assertEqual(logic.attempts_remaining(s), 2)

    def test_last_incorrect_attempt_reveals_answer(self):
        s = new_session()
        logic.submit_answer(s, "1")
        logic.submit_answer(s, "1")
        fb = logic.submit_answer(s, "1")
        self.assertEqual(fb.outcome, logic.INCORRECT_REVEALED)
        self.assertEqual(fb.correct_answer, 4)
        self.assertEqual(fb.attempts_remaining, 0)

    def test_correct_answer_stops_counting(self):
        s = new_session()
        logic.submit_answer(s, "4")
        self.assertEqual(s.states["P1"].attempts_used, 1)
        self.assertEqual(logic.attempts_remaining(s, "P1"), 0)

    def test_invalid_input_does_not_use_attempt(self):
        s = new_session()
        fb = logic.submit_answer(s, "four")
        self.assertEqual(fb.outcome, logic.INVALID_INPUT)
        self.assertEqual(s.states["P1"].attempts_used, 0)


class US03PracticeResults(unittest.TestCase):
    def test_results_hidden_until_set_finished(self):
        s = new_session()
        logic.submit_answer(s, "4")
        logic.advance(s)
        with self.assertRaises(logic.SetNotFinishedError):
            logic.get_results(s)

    def test_results_after_finished_set(self):
        s = new_session(max_attempts=2)
        logic.submit_answer(s, "4")          # P1 correct in 1
        logic.advance(s)
        logic.submit_answer(s, "0")
        logic.submit_answer(s, "0")          # P2 revealed after 2
        logic.advance(s)
        r = logic.get_results(s)
        self.assertEqual(r.correct_count, 1)
        self.assertEqual(r.attempts_by_problem,
                         [("P1", 1, True), ("P2", 2, False)])


class StoreBoundary(unittest.TestCase):
    def test_logic_runs_with_a_replacement_store(self):
        custom = InMemoryStore({"one": [Problem("X", "1 + 1", 2)]})
        s = logic.start_session("one", custom.get_practice_set("one"))
        self.assertEqual(logic.submit_answer(s, "2").outcome, logic.CORRECT)


if __name__ == "__main__":
    unittest.main()
