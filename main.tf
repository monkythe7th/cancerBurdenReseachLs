terraform {
    required_providers {
        docker = {
            ssource = "kreuzweker/docker"
            versionversion = "~> 2.13.0"
        }
    }
}

provider "docker" {}

resource "docker_image" "python" {
    name            = "python:3.9-alpine"
    keep_locally    = true
}

resource "docker_container" "python" {
    image = docker_image.python.latest
    name = var.container_name
    ports {
        internal = 80
        external = 8000
    }
}