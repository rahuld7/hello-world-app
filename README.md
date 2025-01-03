# Deploying Python Flask Application on AKS using Docker and ACR

## Overview
This guide walks you through the deployment of a Python Flask application to Azure Kubernetes Service (AKS) using Docker for containerization and Azure Container Registry (ACR) for storing the Docker image. The deployment is automated using Azure Pipelines.

### **Files Involved**
1. **app.py**  
2. **Dockerfile**  
3. **Azure-pipelines.yaml**  
4. **deployment.yaml**  
5. **service.yaml**

---

## **1. Build and Push Docker Image with Azure Pipelines**

### **File: Azure-pipelines.yaml**

The `Azure-pipelines.yaml` file is used to automate the Continuous Integration and Continuous Deployment (CI/CD) process. It contains two main stages:

#### **Stage 1: Build and Push Docker Image**
- **DockerInstaller@0**: Installs Docker on the build agent.
- **Docker@2**: This step builds the Docker image and pushes it to Azure Container Registry (ACR). It uses the `Dockerfile` and tags the image with `latest`.

Key points:
- **imageName**: Specifies the name of the Docker image (`hello-world-app`).
- **containerRegistry**: Specifies the ACR where the Docker image will be pushed (`k8sdemoacr.azurecr.io`).

The pipeline will trigger every time changes are pushed to the `main` branch.

---

## **2. Dockerizing the Application**

### **File: Dockerfile**

The `Dockerfile` contains instructions on how to build the Docker image for the Python Flask application:

- **Base Image**: Uses the official `python:3.9-slim` image as a base.
- **Application Copy**: Copies the `app.py` into the `/app` directory in the container.
- **Install Dependencies**: Installs Flask using `pip`.
- **Expose Port**: Exposes port `5000` for the Flask application to run.
- **Run Command**: Runs the Flask application (`app.py`).

This file ensures the application is packaged with all dependencies into a Docker image.

---

## **3. Kubernetes Deployment**

### **File: deployment.yaml**

The `deployment.yaml` file defines how the application is deployed to AKS:

- **Kind: Deployment**: Specifies that this resource is a Kubernetes deployment.
- **Replicas**: Defines that only 1 replica (instance) of the application is created in the AKS cluster.
- **Image**: Refers to the Docker image stored in ACR. This image is tagged as `latest` and is pulled from ACR during deployment.
- **Port**: The container listens on port `5000`, which matches the Flask application's configured port.

This file defines how Kubernetes will manage and scale the application container.

---

## **4. Kubernetes Service Configuration**

### **File: service.yaml**

The `service.yaml` file defines a Kubernetes service to expose the application:

- **Kind: Service**: Creates a Kubernetes service that provides stable network access to the application.
- **Selector**: The service selects the pods with the label `app: hello-world` (from the `deployment.yaml` file).
- **Port and TargetPort**: The service listens on port `80` and routes traffic to the container port `5000`.
- **Type: LoadBalancer**: This creates an external load balancer to provide a public IP for accessing the application.

The `LoadBalancer` type ensures that the application is accessible over the internet using a public IP.

---

## **5. Deployment Process Using Azure Pipelines**

1. **Pipeline Triggers**:  
   The pipeline is triggered automatically when changes are pushed to the `main` branch of the repository.

2. **Stage 1 - Build and Push Docker Image**:  
   In the first stage, the pipeline:
   - Installs Docker on the build agent.
   - Builds the Docker image using the `Dockerfile`.
   - Pushes the Docker image to Azure Container Registry (ACR) with the specified tag (`latest`).

3. **Stage 2 - Deploy to Kubernetes**:  
   Once the image is successfully pushed to ACR:
   - The deployment and service configurations are applied to the AKS cluster using `kubectl`.
   - The pipeline uses the Azure Kubernetes Service connection to authenticate and interact with the AKS cluster.
   - The `deployment.yaml` and `service.yaml` files are applied to create the deployment and expose the service via a LoadBalancer.

---

## **6. Accessing the Application**

Once the pipeline completes, the application will be deployed to AKS. To access the application:

1. **Obtain the External IP Address**:  
   Run the following command to retrieve the external IP assigned to the LoadBalancer:

   ```bash
   kubectl get svc hello-world-service
