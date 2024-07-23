# Hello World Microservices

## Project Description

This project demonstrates a simple microservices architecture that broadcasts "Hello world" messages at random intervals and displays them in real-time via a web browser.

## Architecture

The system consists of three main components:

1. **Broadcaster Service**: Generates "Hello world" messages at random intervals (between 1 to 10 seconds) and publishes them to a Redis channel.

2. **Web Server Service**: Subscribes to the Redis channel, receives the broadcasted messages, and forwards them to connected web clients via WebSockets.

3. **Redis**: Acts as a message broker between the broadcaster and web server services.

The services are containerized using Docker and orchestrated with Kubernetes (via Minikube for local development).

```
+-------------+     +-------+     +------------+     +---------+
| Broadcaster | --> | Redis | <-- | Web Server | <-- | Browser |
+-------------+     +-------+     +------------+     +---------+
```

## Tech Stack

- **Programming Language**: Python 3.9+
- **Web Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Message Broker**: Redis
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube for local development)
- **Container Registry**: Local (Minikube's built-in Docker daemon)

## Prerequisites

- Docker
- Minikube
- kubectl

## Setup Instructions

1. Start Minikube:
   ```
   minikube start
   ```

2. Build the Docker images:
   ```
   chmod +x scripts/build-images.sh
   ./scripts/build-images.sh
   ```

3. Deploy the services:
   ```
   chmod +x scripts/deploy.sh
   ./scripts/deploy.sh
   ```

4. Open the URL provided at the end of the deployment in your web browser to view the "Hello world" broadcasts.

## Development

To make changes to the services:

1. Modify the Python files in the respective src/ subdirectories as needed
2. Rebuild the Docker images by running ./scripts/build-images.sh
3. Redeploy the services by running ./scripts/deploy.sh

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure all prerequisites are installed and up-to-date
- Verify that Minikube is running (`minikube status`)
- Check the logs of the services (`kubectl logs <pod-name>`)
