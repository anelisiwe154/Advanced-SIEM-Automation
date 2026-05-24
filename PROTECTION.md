# Branch Protection Rules

The rule is configured on the main branch to enforce collaboration, code quality, and repository integrity.

## Rules Applied
- Require pull request reviews (at least 1)
  Every change must be reviewed by at least one team member before merging. This ensures peer validation, knowledge sharing, and accountability. As i am the only one responsible for the project i will do all the reviews.

- Require status checks to pass (CI Pipeline)
  The CI workflow runs automated tests and checks before code is merged. The tests are currently failing now, this rule acts as a quality gate to prevent unverified code from entering main.

- Disable direct pushes  
  All collaborators cannot push directly to main. All changes must go through pull requests, ensuring traceability, review, and a clean commit history.

## Why These Rules Matter
- Collaboration: Reviews encourage discussion and reduce the risk of errors slipping through.  
- Quality Assurance: Status checks enforce automated validation, keeping the branch stable.  
- Integrity: Restricting direct pushes ensures main remains production‑ready and prevents accidental overwrites.  
- Traceability: Pull requests provide a clear audit trail of what was changed, why, and by whom.

## Conclusion
These rules align with industry best practices for secure and maintainable software development. They protect the stability of the `main` branch, enforce accountability, and guarantee that all contributions meet agreed‑upon standards before being integrated.