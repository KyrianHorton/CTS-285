# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

**Why this release slice was defensible:**
I chose ST-01, ST-02, ST-03, and ST-04, which use 10 out of the 13 points. All four are high value and ready to work on. ST-01 needs to be done first because the other three depend on it. Together, they allow students to create tasks, mark them as complete, recover missed tasks, and use the keyboard to enter tasks. I left 3 points unused because the other options didn't really help meet the release goal.

**One intentional deferral and why:**
I deferred ST-07, AI study recommendations. It needs refinement because its data needs and recommendation rules are unresolved. It also costs 5 points, which does not fit the remaining capacity. It would add an extra feature the release goal says to avoid.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- None

### Added after complication
- None

**What changed and why:**
The capacity dropped from 13 to 10 points, and the accessibility fix is now required. I kept the same four stories, but ST-04 is now something that must be completed instead of just an extra feature. Since all 10 points are being used, there is no room for ST-05 through ST-08.

**Tradeoff accepted:**
Using all 10 points means there is no room for extra features like the weekly progress summary (ST-05). I chose to keep the four stories because they meet the main goal of letting students plan, complete, and recover tasks while also meeting the accessibility requirement.

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.
