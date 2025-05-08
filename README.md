# AWS Lambda Serverless Examples – S3 → Lambda → DynamoDB

This repo is a **medium‑complexity serverless demo** suitable for your DevOps portfolio.
It showcases an event‑driven architecture built with **AWS Lambda, S3, DynamoDB,
API Gateway HTTP API, and AWS SAM**.

## Scenario 🖼️

| Step | What happens? |
| ---- | -------------- |
| 1 | A user **uploads an image** (or any file) to an S3 bucket. |
| 2 | The **`upload_processor` Lambda** is triggered by the S3 event, reads basic metadata (size, content‑type) and stores it in a DynamoDB table. |
| 3 | A second **`get_metadata` Lambda** is exposed via **API Gateway** at `/images/{object_key}` and returns the stored JSON. |

<img src="docs/architecture.png" width="650">

## Tech stack

* **Python 3.11** Lambda runtimes
* **AWS SAM** for Infrastructure‑as‑Code
* **pytest + moto** for unit tests
* **GitHub Actions** for CI/CD
* **Boto3** AWS SDK (no extra PyPI deps required)

## Repository layout

```text
.
├── src/
│   ├── handlers/
│   │   ├── upload_processor.py    # S3 → DynamoDB
│   │   └── get_metadata.py        # API → DynamoDB
│   └── lib/
│       └── dynamo.py              # Helper for DynamoDB access
├── template.yaml                  # AWS SAM template
├── tests/                         # Unit tests (moto mocks)
├── .github/workflows/ci.yml       # Build‑test‑deploy pipeline
└── README.md
```

## Prerequisites

| Tool | Tested version |
| ---- | -------------- |
| AWS CLI | 2.15+ |
| AWS SAM CLI | 1.108+ |
| Docker Engine | 24+ |
| Python | 3.11 |

```bash
# Verify
aws --version
sam --version
docker --version
```

Ensure your AWS credentials are configured (e.g. `aws configure` or
`~/.aws/credentials`).

## Local development

```bash
# 1) Create and activate venv (optional)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) Run unit tests
pytest -q

# 3) Build artifacts
sam build

# 4) Invoke Lambda locally with a sample event file
sam local invoke UploadProcessor --event events/s3_put.json

# 5) Start local API
sam local start-api
curl http://localhost:3000/images/example.jpg
```

## Deployment

```bash
sam deploy --guided
```

- Choose a **unique S3 deployment bucket** when prompted.
- Note the outputted `ImageApiUrl`, e.g. `https://abc123.execute-api.eu-central-1.amazonaws.com/images/`

### Teardown

```bash
sam delete
```

## CI/CD

The included **GitHub Actions** workflow:

1. Checks out the repo
2. Installs Python deps, runs `pytest`
3. Executes `sam build`
4. Runs `sam deploy --no-confirm-changeset` on the `main` branch

Secrets required in the repo:

| Secret | Description |
| ------ | ----------- |
| `AWS_ACCESS_KEY_ID` | IAM user or OIDC role for deploy |
| `AWS_SECRET_ACCESS_KEY` | if using static keys |
| `AWS_REGION` | e.g. `eu-central-1` |

## Cost note

This architecture stays within the AWS Free Tier for modest testing
(1 M Lambda requests / 1 GB‑s, 5 GB S3, 25 GB‑m DynamoDB). Remember to
**remove the stack** when finished.

## License

MIT © 2025 Your Name
