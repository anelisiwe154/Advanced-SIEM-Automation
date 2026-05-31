# Contributing to Advanced SIEM Automation

I am excited that you want to contribute! This project simulates a real-world SIEM automation platform. Please follow the guidelines below to ensure smooth onboarding and consistent contributions.

---

## Setup Instructions
1. Fork this repository to your GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/anelisiwe154/Advanced-SIEM-Automation.git

Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

Run test locally to confirm setup
pytest

Coding standards
- Use pytest for all tests.
- Ensure CI pipeline passes before submitting a PR.
- Commit messages should be descriptive

## Current Bugs to Work On

Contributors can choose one of the following open bugs:

1. Improve User deactivation error handling

- Label: bug
- Status: Open (#46)
- Description: Deactivating a non-existent user does not return the correct 404 Not Found.
- Goal: Update api/users.py to improve error handling.

2. Fix Rule validation bug

- Label: bug
- Status: Open (#45)
- Description: Rule creation does not consistently return 422 Unprocessable Entity when required fields are missing.
- Goal: Strengthen validation in api/rules.py and add unit tests.

PR Checklist

- Code follows style guidelines.
- Tests added or updated.
- CI pipeline passes.
- Documentation updated.
- Linked to an issue (#45 or #46).