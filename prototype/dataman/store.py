"""Stubbed data layer for the DataMan prototype.

STUB: Problems are a fixed in-memory list and session state lives only
in memory for the life of the process. No database is chosen
(requirements.md Assumptions: no database technology is required by
the evidence).

The interface and logic only call the methods below. A later version
(file, SQLite, Flask session, or database) can replace this class
without changing logic.py or app.py, as long as it keeps the same
method names.
"""

from dataman.logic import Problem

# STUB: fixed practice set. Real problem sets / generation are out of
# scope for this slice.
_PRACTICE_SETS = {
    "addition-1": [
        Problem("A1", "7 + 5", 12),
        Problem("A2", "9 + 6", 15),
        Problem("A3", "8 + 8", 16),
    ],
}


class InMemoryStore:
    def __init__(self, practice_sets=None):
        self._sets = dict(practice_sets or _PRACTICE_SETS)
        self._sessions = {}

    def list_practice_sets(self):
        return sorted(self._sets)

    def get_practice_set(self, set_id):
        if set_id not in self._sets:
            raise KeyError(f"Unknown practice set: {set_id}")
        return list(self._sets[set_id])

    # --- Session state -------------------------------------------------
    # STUB for US-04 (Deferred). These methods exist so the boundary is
    # already in place, but nothing survives the program closing, and
    # there is no learner identity (Open Question 3). The key is a
    # plain string the caller supplies.

    def save_session(self, key, session):
        self._sessions[key] = session

    def load_session(self, key):
        return self._sessions.get(key)
