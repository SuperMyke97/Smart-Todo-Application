Project: Smart Todo Application
Build a command-line todo application with advanced features powered by regular expressions for intelligent task parsing and management.

Core Features (Required)
Task Management

Add, update, delete, and list tasks
Mark tasks as complete/incomplete
Persistent storage (JSON file)
Smart Task Parsing with Regex

Parse natural language input: "Buy groceries @shopping #high due:2025-10-20 assigned:alice@example.com"

Extract components using regex:

Task description
Tags (e.g., @shopping, @work, @personal)
Priority (#high, #medium, #low)
Due dates (due:YYYY-MM-DD, due:tomorrow, due:next week)
Email (assigned:alice@example.com)
Validate email addresses for task assignment

Extract time patterns (e.g., "at 3pm", "by 5:30 PM")

Search & Filter with Regex

Search tasks by keyword patterns
Filter by tags using regex patterns
Find tasks with specific date patterns
Search by priority levels
Task Validation

Use regex to validate:

Date formats
Priority levels
Tag naming conventions
Task ID formats
Required Components
1. Requirements:
All mentees fork the organization repository to their personal GitHub account.
All issue tracking, development, and PRs occur in the personal fork.
Each mentee maintains their personal main branch as their stable branch.
All feature development happens in separate branches (feature/*), merged into personal main.
Final submission is made by creating a PR from the personal main → organization <name>/main.
No direct commits to main, or <name>/main in the organization repository.
2. Issue Tracking
GitHub Issues Setup: Create issues for each component:

[FEATURE] Implement regex task parser
[FEATURE] Add task CRUD operations
[FEATURE] Implement search with regex
[FEATURE] Date validation with regex
[FEATURE] Tag extraction system
[BUG] Fix date parsing edge case
[TEST] Add unit tests for regex patterns
Project Board Columns:

Backlog
To Do
In Progress
Code Review
Done
Requirements:

All issues properly labeled and assigned
Use milestones for project phases
Link PRs to relevant issues in your personal fork
3. Modular Code Structure Sample (doesn't have to look exact)
todo-app/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py          # Task data model
│   │   └── todo_list.py     # TodoList collection
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── regex_patterns.py # All regex patterns
│   │   ├── task_parser.py    # Parse task input
│   │   ├── date_parser.py    # Parse dates
│   │   └── validator.py      # Validation logic
│   ├── services/
│   │   ├── __init__.py
│   │   ├── task_service.py   # Business logic
│   │   └── storage_service.py # File operations
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── cli/
│       ├── __init__.py
│       └── interface.py      # CLI interface
├── tests/
│   ├── __init__.py
│   ├── test_task_parser.py
│   ├── test_date_parser.py
│   ├── test_validator.py
│   ├── test_task_service.py
│   └── test_regex_patterns.py
├── docs/
│   └── architecture.md
├── data/
│   └── .gitkeep
├── pyproject.toml
├── README.md
├── .gitignore
└── LICENSE
4. Dependency Management
Poetry Setup:

Required dependencies:

Python 3.10+
pytest (testing)
pytest-cov (coverage)
python-dateutil (date parsing helper)
Development dependencies:

black (formatting)
flake8 (linting)
mypy (type checking)
5. Documentation
README.md must Include:

Project title and description

Features list

Installation instructions

git clone <repo-url>
cd smart-todo-app
poetry install
poetry run python src/main.py
Testing instructions

Example Usage Scenarios
# Add tasks with smart parsing
> add "Complete project @school #high due:2025-10-20 assigned:alice@example.com"
✓ Task added: Complete project
  Tags: school | Priority: high | Due: 2025-10-20

> add "Call doctor tomorrow at 2pm @personal"
✓ Task added: Call doctor
  Tags: personal | Due: 2025-10-13 | Time: 14:00

> add "Review PRs every Monday @work 1h assigned:alex@example.com"
✓ Recurring task added: Review PRs
  Tags: work | Frequency: weekly | Duration: 1h

# Search with regex
> search "@work"
Found 3 tasks with tag 'work'...

> search "due:2025-10-.*"
Found 5 tasks due in October 2025...

# List and filter
> list --priority high
> list --tag @school
> list --due today
Submission Guidelines
Deliverables
Organization Repository Contribution

All work must be linked to the organization’s main repository.

Each mentee has a dedicated branch named <name>/main (e.g., alex/main).

Mentees fork the organization repository to their personal GitHub account.

Within the personal fork:

Perform all issue tracking and project board management.
Create feature branches (feature/*) from your fork’s main.
Open PRs within your fork (feature/* → main) to manage merges and code reviews.
Once your main branch in the personal fork is stable and complete, open a final PR to the organization’s repo:

Base branch: org:<name>/main
Compare branch: <your-username>:main
This final PR is your official project submission.

Project Report (Demo Submission)

Cover Page: Project title, name, date
Introduction: Overview and objectives
Architecture: System design and diagrams
Demo Demonstration of thee application
Testing Strategy: Coverage report and test summary
Challenges & Solutions: What was difficult and how it was handled
Conclusion: Lessons learned and future improvements
