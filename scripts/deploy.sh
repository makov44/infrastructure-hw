#!/bin/bash

# Function to check if image exists in Minikube
check_image() {
    image_name=$1
    if minikube ssh "docker image inspect $image_name" &> /dev/null; then
        echo "Image $image_name exists in Minikube"
    else
        echo "Image $image_name does not exist in Minikube"
        exit 1
    fi
}

# Check images before deploying
check_image "broadcaster:latest"
check_image "web-server:latest"

# Deploy Redis
echo "Deploying Redis..."
kubectl apply -f kubernetes/redis-deployment.yaml
kubectl rollout status deployment/redis

# Deploy broadcaster
echo "Deploying broadcaster..."
kubectl apply -f kubernetes/broadcaster-deployment.yaml
kubectl rollout status deployment/broadcaster

# Deploy web-server
echo "Deploying web-server..."
kubectl apply -f kubernetes/web-server-deployment.yaml
kubectl rollout status deployment/web-server

echo "All services deployed successfully!"

# Get the URL for the web server
minikube service web-server --url