# DataMan Requirements Register

## Evidence Notes

### E1 — Stakeholder Elicitation Simulation

Teachers reported that students may pause practice and return later. A learner's saved practice state needs to remain available after leaving and returning to the application.

Source: `docs/decisions/m2-elicitation-decision-record.md`

### E2 — Stakeholder Elicitation Simulation

The primary learner is a student practicing independently, often with a teacher or parent nearby. The exact device and access conditions were initially unconfirmed.

Source: `docs/decisions/m2-elicitation-decision-record.md`

### E3 — Stakeholder Elicitation Simulation

Stakeholders identified immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as important parts of the original DataMan experience.

Source: `docs/decisions/m2-elicitation-decision-record.md`

### E4 — DataMan Elicitation Case

Interview and observation showed that learners may disengage after repeated incorrect answers. The observed learner did not know how many attempts remained before DataMan revealed the correct answer.

Source: M2.3 DataMan Elicitation Case

### E5 — 1977 DataMan Manual / Document Analysis

The original Answer Checker provides immediate correctness feedback and reveals the correct answer after repeated incorrect attempts. The attempt limit is intentional behavior rather than a defect.

Source: 1977 DataMan manual evidence reviewed in the M2.3 DataMan Elicitation Case

### E6 — DataMan Elicitation Case

The case identified an interaction requirement that incorrect-answer feedback must be available through keyboard navigation and must not rely on color alone.

Source: M2.3 DataMan Elicitation Case conclusion

---

## Functional Requirements

### FR-1 — Preserve Practice State

The system must preserve a learner's saved practice state when a session is interrupted so that it is available when the learner returns.

**Source/Rationale:** E1 and the complication recorded in the M2 elicitation decision record. Students may leave and return to practice, and sessions may end unexpectedly.

### FR-2 — Correctness Feedback

The system must allow a learner to submit an answer to a math problem and receive immediate correctness feedback.

**Source/Rationale:** E3 and E5. Immediate answer feedback is identified as an important and intentional part of the DataMan practice experience.

### FR-3 — Remaining Attempts

The system must show the learner how many attempts remain on the current problem before revealing the correct answer.

**Source/Rationale:** E4 and E5. Observation showed that the learner did not understand when the correct answer would be revealed, while document analysis showed that the attempt limit itself is intentional.

### FR-4 — Practice Results

The system must report the learner's correct answers and attempts after a completed practice set.

**Source/Rationale:** Original DataMan behavior reviewed during Module 2 supports reporting correct answers and attempts to the learner after a completed set.

---

## Non-Functional Requirements

### NFR-1 — Keyboard Accessibility

Incorrect-answer feedback must be available through keyboard navigation.

**Source/Rationale:** E6. The DataMan Elicitation Case identified keyboard access as a required interaction quality.

### NFR-2 — Non-Color Feedback

Incorrect-answer feedback must not rely on color alone to communicate its meaning.

**Source/Rationale:** E6. The DataMan Elicitation Case identified this as a required interaction quality.

### NFR-3 — Independent Use

The practice experience must allow the primary learner to proceed through practice without requiring constant assistance from a teacher or parent.

**Source/Rationale:** E2. Stakeholder evidence identifies the primary learner as a student practicing independently, often with a teacher or parent nearby.

---

## Open Questions and Assumptions

### Open Questions

1. What exact device and browser compatibility requirements should be established for Chromebooks, phones, tablets, and home computers?
2. How should learner progress be measured and presented beyond the confirmed need for learners to see their progress?
3. Does the system require learner accounts or authentication to associate saved practice state with a learner?

### Assumptions / Unconfirmed Solutions

- No specific database technology is required by the current evidence.
- No specific color scheme, icon, animation, or visual theme has been confirmed as a requirement.
- An adaptive hint system has not been established as a requirement.
- The evidence does not support removing the original attempt-limit behavior.

---

## Traceability Example

**Evidence:** During the DataMan Elicitation Case, a learner was surprised when the correct answer appeared after repeated incorrect attempts and could not tell whether they had simply answered incorrectly or had run out of attempts.

**Need:** The learner needs to understand where they are in the attempt sequence.

**Requirement:** FR-3 — The system must show the learner how many attempts remain on the current problem before revealing the correct answer.
