
resource "google_compute_instance" "control-shell" {
  machine_type = var.control-instance-type
  name         = "control-shell"
  zone         = var.control-zone
  boot_disk {
    initialize_params {
      size = 5
      type = "pd-balanced"
    }
  }
  network_interface {
    network = "default"
  }
}

