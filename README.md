# EthicsLab

This project is an API for ethical AI experimentation on texts, using Large Language Models (LLMs) served via Ollama.

## Local Development

### Dependency Management

This project uses `uv` for dependency management.

### Running the Application

To run the application locally, use the following command:

```bash
uv run uvicorn src.ethicslab.main:app --reload
```

### API Interface

Once the application is running, the API can be accessed at the following local addresses:

-   **API Root:** `http://localhost:8000/`
-   **API Docs:** `http://localhost:8000/docs`
-   **Health Check:** `http://localhost:8000/health`
-   **Chat Endpoint:** `http://localhost:8000/api/chat/`
-   **Tweet Endpoint:** `http://localhost:8000/api/tweet/`

For the `/api/chat/` endpoint to work locally, you must have Ollama running on your local machine.

## Deployment

The application is designed to be deployed to a Kubernetes cluster as a multi-container application.

### Docker

First, build the Docker images for the API and the Ollama service.

**1. Build the API Image:**

```bash
docker build -t ethicslab-api:latest .
```

**2. Build the Ollama Image:**

This will create a Docker image with the `gemma2:2b` model pre-packaged.

```bash
docker build -f ollama.Dockerfile -t ollama-gemma:latest .
```

### Kubernetes

Once the Docker images are built and pushed to a registry accessible by your Kubernetes cluster, you can deploy the application using the provided manifest.

**1. Apply the Manifest:**

```bash
kubectl apply -f k8s/deployment.yaml
```

This will create:
- A `Deployment` and `Service` for the FastAPI application.
- A `Deployment` and `Service` for the Ollama service.

**2. Access the Deployed Application:**

The API service is exposed via a `LoadBalancer`. To find the external IP address assigned by the load balancer, run:

```bash
kubectl get svc ethicslab-api-service
```

Look for the `EXTERNAL-IP` value. The API will be accessible at `http://<EXTERNAL-IP>`.

### Configuration

The application is configured using an environment variable to locate the Ollama service.

-   `OLLAMA_URL`: The URL of the Ollama service. In the Kubernetes deployment, this is automatically set to `http://ollama-service:11434` to allow the API to communicate with the Ollama container.