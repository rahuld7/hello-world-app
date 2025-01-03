#Hello World Python Application with Docker and AKS

This project demonstrates how to build, containerize, and deploy a simple "Hello! ATS company" Python Flask application to Azure Kubernetes Service (AKS) using Docker and Azure DevOps.

Prerequisites

Before you begin, make sure you have the following:

- Docker (https://www.docker.com/get-started)
- Azure CLI (https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- Kubectl (https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- Azure DevOps Account (https://azure.microsoft.com/en-us/services/devops/)
- Azure Container Registry (ACR) (https://azure.microsoft.com/en-us/services/container-registry/)
- An existing AKS cluster

Project Structure

The project contains the following files:

- app.py: Flask application serving a simple HTML page with a "Hello World" message.
- Dockerfile: Docker configuration for containerizing the application.
- deployment.yaml: Kubernetes deployment manifest for deploying the application to AKS.
- service.yaml: Kubernetes service manifest for exposing the application.
- azure-pipelines.yaml: Azure DevOps pipeline configuration for building, pushing, and deploying the application.

Steps

1. Build and Push Docker Image

Build the Docker Image:

docker build -t <your-acr-name>/hello-world-app:latest .

Push the Docker Image to Azure Container Registry (ACR):

docker push <your-acr-name>/hello-world-app:latest


2. Set Up Azure DevOps Pipeline

The pipeline is configured in azure-pipelines.yaml and automatically triggers on changes to the main branch. It performs the following tasks:

1. Build and Push Docker Image: Builds the Docker image and pushes it to ACR.
2. Deploy to AKS: Deploys the application to AKS using the Kubernetes manifests (deployment.yaml and service.yaml).

3. Apply Kubernetes Manifests

Once the image is built and pushed, deploy the application to AKS using the Kubernetes manifests.

Apply the Deployment:

kubectl apply -f deployment.yaml

Apply the Service:

kubectl apply -f service.yaml

4. Access the Application

After deploying the service, retrieve the external IP of the LoadBalancer:

kubectl get services hello-world-service

Once the external IP is available, navigate to the IP in your browser to see the "Hello World" page.

5. Cleanup Resources

To remove the deployed resources:

kubectl delete -f service.yaml
kubectl delete -f deployment.yaml

