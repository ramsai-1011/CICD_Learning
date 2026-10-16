# Basic MLOps CI/CD Learning Project

This project is a small Python example for learning CI/CD in an MLOps workflow.

## What it does

- creates a synthetic dataset
- trains a small machine learning model
- checks model quality with a unit test
- saves the trained model as a file
- runs in GitHub Actions as a CI pipeline

## Structure

- `mlops_project/` contains the training logic
- `tests/` contains automated tests
- `.github/workflows/ci.yml` runs the CI pipeline

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .venv\Scripts\activate  # Windows
pip install -r requirements.txt
python -m mlops_project.train
pytest
```

## CI/CD idea

This is a simple example of how a real MLOps workflow usually works:

1. Code is pushed to a branch
2. CI checks install + tests + lint
3. The model is trained in a controlled environment
4. Artifacts are saved for review or deployment
5. Deployment can be triggered after successful validation
