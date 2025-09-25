# COMP 163 - Assignment 4: College Life Adventure Game

## Author
Christopher Arnold - COMP 163, Fall 2025

## Description
This is an interactive, text-based College Life Adventure Game that simulates a semester in college. Players make decisions about course loads and study focus, which impact their GPA, study hours, social points, and stress levels. The game demonstrates branching logic, decision-making, and the use of multiple Python operators.

## Game Concept
Players start with a set of initial stats: GPA, study hours, social points, and stress level. They then make two main choices:

1. **Course Load Decision:** Choose a Light, Standard, or Heavy course load. This affects study hours and stress levels based on current GPA.
2. **Study Strategy Decision:** Pick a subject to focus on (Programming, Math, English, or History). Different choices produce different outcomes and adjust player stats. Invalid choices are handled gracefully.

Finally, the game performs a **Final Semester Assessment**, providing different endings based on the player's accumulated stats, including nested conditions and identity checks.

## Branching Logic Usage
The game demonstrates several Python concepts:

- **Comparison Operators:** Used to adjust outcomes based on GPA, study hours, or stress levels.
- **Logical Operators (`and`, `or`, `not`):** Implemented to create complex conditions for study outcomes.
- **Membership Operators (`in`, `not in`):** Used to validate the player’s subject choice.
- **Identity Operators (`is`, `is not`):** Used for type checking in the final assessment.
- **Nested If Statements:** Applied in the final semester assessment to produce multiple endings.
- **If/Elif/Else Statements:** Used for course load decisions and study strategy branching.

## How to Run
1. Clone or download the repository.
2. Open the Python file: `carnold_assignment_3.py`.
3. Run the program using a Python interpreter (Python 3.x recommended):

```bash
python carnold_assignment_3.py
