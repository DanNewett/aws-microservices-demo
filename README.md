# AWS Microservices Demo
Serverless sample: API Gateway → Lambda (Python) → DynamoDB. Includes Terraform and a GitHub Actions deploy.

## Architecture
- `/orders` POST/GET -> Lambda -> DynamoDB
- CloudWatch metrics & logs; minimal tracing hooks

## CI/CD
- On push to main: validate Terraform, run unit tests, deploy to dev (placeholder)
