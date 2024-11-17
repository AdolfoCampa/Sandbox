
resource "google_compute_instance" "control-shell-vm" {
    machine_type = "e2-micro"
    name = "control-shell"
    zone = "us-central1-b"
    boot_disk {
        
    }
    network_interface {
    }
}

