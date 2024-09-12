terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket-lambda-dawdawdawdawd"
    key            = "terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock-table-lambda-dawdawdawdawd"
    encrypt        = true
  }
}
