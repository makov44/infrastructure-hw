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
chmod +x scripts/build-images.sh
./scripts/build-images.sh
```

#### 3. Deploy the services:
```
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

#### 4. Open the URL provided at the end of the deployment in your web browser to view the "Hello world" broadcasts.

## Project Structure

project-root/
│
├── src/
│   ├── broadcaster/
│   │   └── broadcaster.py
│   └── web_server/
│       └── web_server.py
│
├── kubernetes/
│   ├── broadcaster-deployment.yaml
│   ├── web-server-deployment.yaml
│   └── redis-deployment.yaml
│
├── docker/
│   ├── Dockerfile.broadcaster
│   └── Dockerfile.web-server
│
├── scripts/
│   ├── build-images.sh
│   └── deploy.sh
│
├── requirements.txt
└── README.md

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

For any other problems, please open an issue in the GitHub repository.