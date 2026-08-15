# Optional remote state configuration.
# Configure your own S3 backend only after creating your own bucket.
#
# terraform {
#   backend "s3" {
#     bucket = "YOUR-OWN-TERRAFORM-STATE-BUCKET"
#     key    = "quickbite/terraform.tfstate"
#     region = "us-east-2"
#   }
# }
