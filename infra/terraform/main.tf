terraform {
  required_providers { aws = { source = "hashicorp/aws" } }
}
provider "aws" { region = var.region }
variable "region" { default = "us-east-1" }
# Add API Gateway, Lambda, DynamoDB resources here (scaffold)
