
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = "sandbox-441501"
  region  = "us-central1-b"
}



