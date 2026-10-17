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

## Check the GitHub Actions connection to Google Cloud

The manual **Check GCP connection** workflow at `.github/workflows/gcp-connection-check.yml`
authenticates with GitHub OIDC and Google Cloud Workload Identity Federation. It does not
use a downloaded service-account key or deploy resources.

Configure this GitHub Actions repository secret:

- `GCP_PROJECT_ID`: the Google Cloud project ID (not its project number).

The workflow has the provider resource name hard-coded as
`projects/716459559070/locations/global/workloadIdentityPools/testing-github-action/providers/github-actions`.
This uses `github-actions` as the provider ID based on the provider's display name. Confirm the
actual **Provider ID** by opening the **GitHub Actions** provider in Google Cloud Console; if its
ID differs, update the hard-coded value in `.github/workflows/gcp-connection-check.yml`.

The principal identifier supplied for this pool,
`principal://iam.googleapis.com/projects/716459559070/locations/global/workloadIdentityPools/testing-github-action/subject/SUBJECT_ATTRIBUTE_VALUE`,
is an IAM member identity, not the provider resource name used by the workflow. Grant the
required project roles to the actual principal in Google Cloud IAM. Replace
`SUBJECT_ATTRIBUTE_VALUE` with the subject value mapped by your provider if it is a placeholder;
the provider's attribute mapping and attribute condition must also permit this GitHub repository
and workflow ref.

Run the workflow from the repository's **Actions** tab using **Check GCP connection > Run
workflow**. A successful run confirms that GitHub exchanged its OIDC token and Google Cloud
accepted the resulting credentials.
