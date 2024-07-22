# Hello World Microservices

This project implements a simple microservices architecture that broadcasts "Hello world" messages at random intervals and displays them in a web browser.

## Prerequisites

- Docker
- Minikube
- kubectl
- Python 3.9+

### Installing Prerequisites on macOS

#### 1. Install Homebrew (if not already installed)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Docker
```
brew install --cask docker
```
After installation, launch Docker Desktop from your Applications folder.

#### 3. Install Minikube
```
brew install minikube
```

#### 4. Install kubectl
```
brew install kubectl
```

#### 5. Install Python 3.9+
```
brew install python@3.9
```

To verify the installations, you can run:
```
docker --version
minikube version
kubectl version --client
python3 --version
```

## Setup Instructions

#### 1. Start Minikube:
```
minikube start
```

#### 2. Build the Docker images:
```
chmod +x build-images.sh
./build-images.sh
```

#### 3. Deploy the services:
```
chmod +x deploy.sh
./deploy.sh
```

#### 4. Open the URL provided at the end of the deployment in your web browser to view the "Hello world" broadcasts.

## Project Structure

- `broadcaster.py`: Service that broadcasts "Hello world" messages
- `web_server.py`: Web server that displays the messages in real-time
- `requirements.txt`: Python dependencies
- Kubernetes configuration files (*.yaml)
- Dockerfiles for each service

## Development

To make changes to the services:

1. Modify the Python files as needed
2. Rebuild the Docker images (step 3 in Setup Instructions)
3. Reapply the Kubernetes configurations (step 4 in Setup Instructions)

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure all prerequisites are installed and up-to-date
- Verify that Minikube is running (`minikube status`)
- Check the logs of the services (`kubectl logs <pod-name>`)

For any other problems, please open an issue in the GitHub repository.