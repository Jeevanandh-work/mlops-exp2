# mlops-exp2

This project demonstrates a simple Python testing workflow with Continuous Integration (CI) using GitHub Actions.

## Experiment Objective

- Build a small Python function.
- Write automated tests using `pytest`.
- Configure GitHub Actions to run tests automatically on every push and pull request.

## Core CI Idea

Continuous Integration (CI) helps developers catch issues early by running tests automatically whenever code is updated.

In this project:

- You push code to GitHub.
- GitHub Actions runs the test workflow.
- You see pass/fail status in the Actions tab.

## Project Structure

```text
mlops-exp2/
|-- your_functions.py
|-- test_cases.py
|-- README.md
`-- .github/
	`-- workflows/
		`-- ci.yml
```

## Files

- `your_functions.py`: contains the `factorial(n)` function.
- `test_cases.py`: contains pytest test cases for factorial behavior.
- `.github/workflows/ci.yml`: GitHub Actions workflow that executes tests.

## Local Run Instructions

1. Install dependencies:

```bash
pip install pytest
```

2. Run tests:

```bash
pytest
```

## GitHub Actions Workflow

The CI workflow is triggered on:

- Push to `main`
- Pull request to `main`

Workflow steps:

1. Checkout repository
2. Set up Python 3.10
3. Install `pytest`
4. Run tests

## Expected Output

- Success: all tests pass.
- Failure: failed assertion details are shown in workflow logs.

## Repository

GitHub: https://github.com/Jeevanandh-work/mlops-exp2