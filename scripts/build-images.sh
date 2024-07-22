#!/bin/bash

# Ensure we're using Minikube's Docker daemon
eval $(minikube docker-env)

# Build the broadcaster image
docker build -t broadcaster:latest -f docker/Dockerfile.broadcaster --build-arg SERVICE=broadcaster .

# Build the web-server image
docker build -t web-server:latest -f docker/Dockerfile.web-server --build-arg SERVICE=web_server .

# Display images
docker images

echo "Docker images built successfully!"