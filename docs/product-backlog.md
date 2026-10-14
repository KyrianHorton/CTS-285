# DataMan Product Backlog

## Sources

This backlog uses these files from my repository:

- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

## Priority Order

1. US-01
2. US-02
3. US-03
4. US-04

## Stories

### US-01 — Immediate correctness feedback

**Requirement ID:** FR-2, NFR-1, NFR-2, NFR-3

**User Story:** As a student practicing independently, I want to know right away whether my answer is correct so that I can learn from each problem without waiting for an adult to check my work.

**Acceptance Criteria:**

- Given a learner is viewing a math problem, when the learner submits an answer, then the system shows whether the answer is correct or incorrect before the next problem is presented.
- Given a learner submits a correct answer, when feedback is shown, then the feedback states that the answer is correct.
- Given a learner submits an incorrect answer, when feedback is shown, then the feedback states that the answer is incorrect.
- Given a learner is using only a keyboard, when the learner submits an answer, then the learner can reach and read the correctness feedback without using a mouse.
- Given incorrect-answer feedback is shown, when it is viewed without color, then its meaning is still clear from text or another non-color cue.

**Relative Effort:** S — This is one of the smallest stories in the backlog because it covers a single answer-and-response interaction with no stored data.

**Dependency / Constraint:** None. NFR-1 and NFR-2 apply as constraints on how feedback is presented.

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** Highest value and lowest risk in the backlog. Stakeholders named immediate feedback as core DataMan behavior (E3, E5), and the instructor stakeholder stated it is required for the first usable release. It has no dependency, and US-02 and US-03 build on it.

---

### US-02 — Show remaining attempts

**Requirement ID:** FR-3, NFR-3

**User Story:** As a student practicing independently, I want to see how many attempts I have left on a problem so that I understand when the correct answer will be revealed and do not get confused or discouraged.

**Acceptance Criteria:**

- Given a learner begins a new problem, when the problem is shown, then the number of attempts remaining is visible to the learner.
- Given a learner submits an incorrect answer and attempts remain, when feedback is shown, then the number of attempts remaining decreases by one and the learner can try again.
- Given a learner submits an incorrect answer on the last remaining attempt, when feedback is shown, then the system reveals the correct answer and states that no attempts remain.
- Given a learner submits a correct answer, when feedback is shown, then no further attempts are counted for that problem.

**Relative Effort:** S — Similar in size to US-01 because it extends the same answer interaction with a counter and a reveal rule.

**Dependency / Constraint:** Depends on US-01 (the answer-checking flow). The original attempt limit must be kept (E5; Assumptions in `docs/requirements.md`).

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** High value and low risk. Observation showed learners did not know when the answer would be revealed and could disengage after repeated incorrect answers (E4). The effort is small and its only dependency, US-01, is ranked first, so both can move forward together. It also supports independent use (NFR-3).

---

### US-03 — Practice set results

**Requirement ID:** FR-4

**User Story:** As a student, I want to see my correct answers and attempts after I finish a practice set so that I can tell how well I did.

**Acceptance Criteria:**

- Given a learner completes every problem in a practice set, when the set ends, then the system shows the number of problems answered correctly.
- Given a learner completes a practice set, when results are shown, then the system shows the number of attempts used on each problem in the set.
- Given a learner has not finished a practice set, when the learner is still working, then the set results are not shown.

**Relative Effort:** M — Larger than US-01 and US-02 because it must collect results across a whole set, but smaller than US-04 because it does not require saving data between sessions.

**Dependency / Constraint:** Depends on US-01 (correctness results) and US-02 (attempt counts). Results are reported within the current session only and do not depend on learner identity.

**Priority:** 3

**Readiness:** Move Forward

**Priority Rationale:** Medium-to-high value because stakeholders named seeing progress as important (E3) and original DataMan reported results after a set. It ranks below US-01 and US-02 because it depends on both and has more effort. Keeping it within a single session avoids the identity uncertainty that blocks US-04.

---

### US-04 — Preserve practice state between sessions

**Requirement ID:** FR-1

**User Story:** As a student who sometimes has to stop practicing, I want my practice state saved when I leave so that I can continue where I left off when I return.

**Acceptance Criteria:**

- Given a learner has answered some problems in a practice set, when the session is interrupted and the same learner returns, then the learner's saved practice state is available.
- Given a learner returns to a saved practice set, when practice resumes, then problems already answered and remaining attempts match what they were before the interruption.

**Relative Effort:** L — The largest story in the backlog because it requires recognizing the same learner across sessions and storing practice state.

**Dependency / Constraint:** Depends on a decision about how a learner is recognized across sessions (Open Question 3). The account/session approach is not ready.

**Priority:** 4

**Readiness:** Defer

**Priority Rationale:** Value is high (E1), but effort is large, risk is medium, and its key dependency is unresolved. Building it before the identity approach is decided would likely cause rework. It is deferred, not dropped, and should return to refinement once Open Question 3 is answered.

---

## Open Questions Carried Forward

- **Q1 (device and browser compatibility):** No story waits on this directly, but it affects how US-01 through US-04 will be tested. No device-specific story is created until compatibility requirements are confirmed.
- **Q2 (how progress is measured and presented):** US-03 covers only the confirmed need to report correct answers and attempts after a set. No broader progress, parent/teacher summary, or analytics story is created until this question is answered.
- **Q3 (learner accounts or authentication):** US-04 waits on this question and is marked Defer.

## Revisions After Triage and Release Planning

- US-04 — Readiness changed from Refine to Defer — Backlog triage record: the account/session approach is not ready, so work that assumes persistent identity carries added uncertainty.
- US-01 — Kept as priority 1 and Move Forward — Backlog triage record: the instructor stakeholder stated immediate answer feedback is required for the first usable release.
- US-02 — Kept as Move Forward — Backlog triage record: retry after an incorrect response depends only on the answer-checking flow and does not need learner identity.
- No parent/teacher summary, theme selector, or analytics story was added — Backlog triage record: these were deferred, and none traces to a validated requirement in `docs/requirements.md`.
