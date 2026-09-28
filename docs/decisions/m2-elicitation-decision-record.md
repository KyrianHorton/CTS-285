# M2 Elicitation Decision Record

## Investigation Path
1. What exactly do stakeholders mean by “students shouldn’t lose their work”?
   Evidence revealed: Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.
2. Who will use the system and in what setting?
   Evidence revealed: The primary learner is a student practicing independently, often with a teacher or parent nearby. Exact device and access conditions have not yet been confirmed.
3. Which original DataMan behaviors are considered essential to preserve?
   Evidence revealed: Stakeholders identify immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as central to the original experience.

## Initial Position
**Supported evidence:**
Students may pause practice and return later, so their saved practice state needs to remain available. The primary learner is a student practicing independently, often with a teacher or parent nearby. Immediate feedback, repeated practice after an incorrect answer, and a clear way to see progress are considered important DataMan behaviors.

**Remaining uncertainty:**
The exact devices and access conditions students will use have not been confirmed.

**Likely functional requirement:**
The system must save a learner's practice state so it remains available when the learner leaves and returns.

**Likely non-functional requirement / quality constraint:**
The system should support students practicing independently without requiring constant help from a teacher or parent.

**Assumption or proposed solution I am not treating as confirmed:**
I am not assuming that a specific database technology should be used to save learner progress.

**Why my initial position is defensible:**
The requirements are based on the evidence gathered from stakeholders instead of assumptions about the design or technology. The evidence supports saving practice state and independent student use, while the exact device and access conditions are still uncertain.

## Complication
Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some sessions may be interrupted before intentional sign-out.

**What this affects:**
It affects how learner progress and practice state need to be preserved. Students may use different devices, and their sessions may end unexpectedly before they sign out.

**What I revised, if anything:**
I would revise the functional requirement to state that the system must preserve a learner's saved practice state when a session is interrupted so it is available when the learner returns

**Final decision and reasoning:**
Revise. The new information confirms that students may use different devices and that sessions may be interrupted unexpectedly. The requirement to preserve practice state is still supported, but it should account for interrupted sessions. I would not assume a specific technology for how the system saves the data.

## Next Project Action
Use this evidence to update the DataMan Requirements Register and preserve any unresolved questions as open assumptions or follow-up items.
