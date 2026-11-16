# Software Engineering Laboratory Submissions

A consolidated repository containing the Software Engineering Laboratory assignments, implementations, reports, documentation, test cases, and supporting evidence completed as part of the B.Tech Computer Science and Engineering programme at PES University.

## Student Information

| Field | Details |
|---|---|
| Name | Yashas Sadananda |
| SRN | PES2UG24CS610 |
| University | PES University |
| Programme | B.Tech Computer Science and Engineering |
| Semester | 5th Semester |
| Section | 5-J |

---

## Laboratory Index

| Lab | Title | Description | Submission |
|---|---|---|---|
| Lab 1 | To be updated | Laboratory assignment and supporting materials | [Lab 1](./Lab-1/) |
| Lab 2 | To be updated | Laboratory assignment and supporting materials | [Lab 2](./Lab-2/) |
| Lab 3 | Component Modelling & Architectural Pattern Selection | UML component modelling and architectural design for an Incident Escalation & On-Call Rotation Engine | [Lab 3](./Lab-3/) |
| Lab 4 | Whack-a-Mole Game | Game development, debugging, collision detection, game-over handling, replay functionality and sound effects using Python and Pygame | [Lab 4](./Lab-4/) |
| Lab 5 | Static Code Analysis | Code quality and security analysis using Pylint, Bandit and Flake8 | [Lab 5](./Lab-5/) |
| Lab 6 | Code and Branch Coverage Analysis | Statement and branch coverage testing using Pytest and Coverage.py | [Lab 6](./Lab-6/) |
| Lab 7 | Fuzz Testing for Input Validation Bugs | Property-based fuzz testing and input validation using Hypothesis and Pytest | [Lab 7](./Lab-7/) |

---

## Lab Details

### Lab 1
Contains the Lab 1 assignment submission and associated supporting materials.

### Lab 2
Contains the Lab 2 assignment submission and associated supporting materials.

### Lab 3 — Component Modelling & Architectural Pattern Selection

**System:** Incident Escalation & On-Call Rotation Engine  
**Architecture:** Microservices

This laboratory focuses on identifying system components, defining their responsibilities and interfaces, and selecting an appropriate architectural pattern.

**Deliverables:**
- UML Component Diagram (PNG)
- UML Component Diagram (PDF)
- Editable Draw.io Diagram
- Written Architectural Justification (DOCX and PDF)
- Student Handout

### Lab 4 — Whack-a-Mole Game

A Python-based interactive game developed using Pygame.

The laboratory focuses on debugging and improving an existing implementation through iterative development and AI-assisted programming.

**Implemented improvements:**
- Refined collision detection.
- Game-over screen with final score.
- Replay functionality with difficulty selection.
- Sound effects for successful hits, missed clicks and game completion.

**Deliverables:**
- Python source code.
- Game modules and dependencies.
- Before-fix gameplay recording.
- After-fix gameplay recording.
- AI chat-history documentation.

### Lab 5 — Static Code Analysis

Static code analysis performed on a Python-based Gym Membership System.

**Tools used:**
- Pylint
- Bandit
- Flake8

**Key improvements:**
- Improved code quality and maintainability.
- Addressed security vulnerabilities.
- Improved naming and exception handling.
- Corrected formatting and style violations.

**Recorded results:**

| Tool | Before | After |
|---|---:|---:|
| Pylint | 4.81/10 | 10.00/10 |
| Bandit | 6 findings | 0 findings |
| Flake8 | 9 violations | 0 violations |

**Deliverables:**
- Corrected Python application.
- Before-and-after analysis reports.
- Issue documentation.
- Reflection document.

### Lab 6 — Code and Branch Coverage Analysis

Testing and coverage analysis of a Python-based Daycare Fees application.

**Tools used:**
- Python
- Pytest
- Coverage.py

**Testing results:**

| Test Suite | Result |
|---|---|
| Statement Coverage | 21 tests passed, 100% statement coverage |
| Branch Coverage | 30 tests passed, 100% branch coverage |

**Deliverables:**
- Daycare Fees application.
- Statement coverage test suite.
- Branch coverage test suite.
- Laboratory report.
- Coverage screenshots.

### Lab 7 — Fuzz Testing for Input Validation Bugs

Property-based fuzz testing using Python's Hypothesis library to identify input-validation bugs in a Daycare Fees application.

**Functions tested:**
- `parse_enrolment()`
- `hours_average()`
- `payable_fee()`

**Technologies used:**
- Python 3.12
- Hypothesis
- Pytest

**Testing results:**
- Three fuzz tests.
- Three functional tests.
- Six tests passed.

**Deliverables:**
- Fixed application source code.
- Hypothesis-based test suite.
- Fuzz-testing evidence PDF.

---

## Technologies and Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Testing Frameworks | Pytest, Hypothesis |
| Static Analysis | Pylint, Bandit, Flake8 |
| Coverage Analysis | Coverage.py |
| Game Development | Pygame |
| Diagramming | Draw.io |
| Version Control | Git, GitHub |

---

## Repository Structure

```text
SE-LABS/
│
├── README.md
│
├── Lab-1/
│
├── Lab-2/
│
├── Lab-3/
│   ├── component-diagram.drawio
│   ├── component-diagram.drawio.pdf
│   ├── component-diagram.drawio.png
│   ├── Lab3_Architecture_Student_handout.pdf
│   ├── PES2UG24CS610_SE_Lab3.docx
│   └── PES2UG24CS610_SE_Lab3.pdf
│
├── Lab-4/
│   ├── main.py
│   ├── requirements.txt
│   ├── game/
│   └── Lab-4/
│       ├── before_fix.mp4
│       ├── after_fix.mp4
│       └── PES2UG24CS610_SELab4_AI_ChatHistory.pdf
│
├── Lab-5/
│   ├── gym_membership_system.py
│   ├── issues.md
│   ├── reflection.md
│   ├── pylint_report_before.txt
│   ├── pylint_report_after.txt
│   ├── bandit_report_before.txt
│   ├── bandit_report_after.txt
│   ├── flake8_report_before.txt
│   └── flake8_report_after.txt
│
├── Lab-6/
│   ├── daycare_fees.py
│   ├── CodeCoverageTest_610_daycare_fees.py
│   ├── BranchCoverageTest_610_daycare_fees.py
│   ├── Lab_6_SE_PES2UG24CS610.docx
│   └── screenshots/
│
└── Lab-7/
    ├── daycare_fees.py
    ├── test_daycare_fees.py
    ├── README.md
    └── Lab7_FuzzTesting_Evidence.pdf
```

---

## Purpose

This repository serves as a centralised collection of Software Engineering Laboratory submissions, providing organised access to implementation files, testing materials, technical documentation, reports and supporting evidence.

Each laboratory is maintained in its own directory to ensure clarity, accessibility and ease of navigation.

---

**PES University | B.Tech Computer Science and Engineering | Semester 5**