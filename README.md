# DevOps Task TRADESOCIO

This repository presents my solution to the DevOps challenge, demonstrating proficiency in Software Engineering, DevOps, and Infrastructure tasks. The goal was to build a simple API service , containerize it, set up a CI/CD pipeline, package it with Helm, and deploy it to Kubernetes, all while adhering to best practices and providing comprehensive documentation.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tasks Completed](#tasks-completed)
  - [Task 0: Public Git Repository](#task-0-public-git-repository)
  - [Task 1: API Service](#task-1-api-service)
  - [Task 2: Dockerize](#task-2-dockerize)
  - [Task 3: CI/CD](#task-3-cicd)
  - [Task 4: Helm Chart](#task-4-helm-chart)
  - [Task 5: Deploy to Kubernetes](#task-5-deploy-to-kubernetes)
  - [Task 6: Documentation](#task-6-documentation)
  - [Task 7: Additional Ideas](#task-7-additional-ideas)
- [How to Build, Deploy, and Test](#how-to-build-deploy-and-test)
  - [Prerequisites](#prerequisites)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the API Service Locally (Docker)](#running-the-api-service-locally-docker)
  - [Deploying to Kubernetes (Helm)](#deploying-to-kubernetes-helm)
  - [Testing the API Service](#testing-the-api-service)
- [Project Structure](#project-structure)
- [Future Improvements / TODOs](#future-improvements--todos)
- [Contact](#contact)

---

## Project Overview

This project implements a simple Flask application that echoes request details (headers, method, and body). It's designed to showcase a full DevOps lifecycle, from development to automated deployment on Kubernetes. The aim was to deliver a solution that is robust, scalable, and easy to manage.

---

## Tasks Completed

Here's a breakdown of the tasks addressed in this repository:

### Task 0: Public Git Repository

This repository itself serves as the public Git repository for the source code, hosted on GitHub:
https://github.com/Ameenrehman/TradeSocio-DevOpsTask.git

### Task 1: API Service

The API service is implemented using [**Flask**].
You can find the source code in the [`./api-service`](./api-service) directory.

**Key Features & Best Practices:**

* **Technology Stack**: Node.js with Express.js for a lightweight and efficient web server.
* **Request Echoing**: Captures and displays request headers, method, and body as specified.
* **Cloud-Native Principles**:
    * **The Twelve-Factor App**: Adherence to principles like [list specific principles you followed, e.g., "Config stored in the environment," "Logs as event streams"].
* **Instrumentation (Bonus)**:
    * **Prometheus Metrics**: The application is instrumented with a [**Prometheus Counter/Gauge**] to track [**describe what it tracks, e.g., "total requests received"**]. You can access these metrics at the `/metrics` endpoint.

### Task 2: Dockerize

A `Dockerfile` is provided to containerize the API service. This allows for consistent execution across various environments.

You can find the `Dockerfile` in the [`./api-service`](./api-service) directory.

**Docker Best Practices Applied (Bonus):**

* **Multi-stage Build**: Utilizes a multi-stage build to create a small, efficient production image by separating build-time dependencies from runtime dependencies.
* **Proper Layer Structure**: Arranges `COPY` and `RUN` instructions to maximize Docker layer caching, speeding up subsequent builds.
* **Non-root User**: The container runs as a non-root user for enhanced security.
* **Security Practices**: [Mention other security practices, e.g., "Using official base images," "Minimizing attack surface by only installing necessary packages"].
* **Integration Test (Bonus)**:
    * A simple integration test for the Docker image is included using [**container-structure-test**]. The test validates [**describe what it validates, e.g., "file existence, correct permissions, and exposed ports"**]. You can find the test configuration in [`./test/docker-integration-test.yaml`](./test/docker-integration-test.yaml).

### Task 3: CI/CD

A CI/CD pipeline is implemented using [**GitHub Actions**] to automate the build, test, and (optional) deployment process.

The GitHub Actions workflow definition is located at [`./.github/workflows/main.yml`](./.github/workflows/main.yml).

**Pipeline Stages:**

1.  **Build**: Builds the Docker image of the API service.
2.  **Test**: Runs the Docker integration tests (if implemented) and any unit/integration tests for the API service.
3.  **Scan**: (Optional) Integrates security scanning tools (e.g., Trivy) for vulnerability checks.
4.  **Publish**: Pushes the Docker image to a container registry (e.g., Docker Hub, GitHub Container Registry).
5.  **Deploy**: (Optional - if automated deployment is configured) Deploys the Helm chart to the Kubernetes cluster.

### Task 4: Helm Chart

A Helm chart is created to package the API service for deployment to Kubernetes, ensuring all necessary components for a production-like environment are included.

The Helm chart is located in the [`./helm-chart/api-service`](./helm-chart/api-service) directory.

**Chart Components:**

* **Deployment**: Manages the API service pods.
* **Service**: Exposes the API service within the cluster.
* **Ingress**: Provides external access to the API service (if `ingress.enabled` is true).
* **Service Account**: Defines a dedicated service account for the deployment (for OPA compliance).
* **Role/RoleBinding**: (If applicable) Defines necessary RBAC permissions for the service account.
* **ConfigMap/Secret**: (If applicable) Manages configuration or sensitive data.

**Bonus Points:**

* **Helm Hooks**: [**Describe any Helm hooks implemented, e.g., "A `pre-install` hook is used to run database migrations before the application pods start."**] See `templates/migration-job.yaml` for an example.
* **Helm Tests**: Includes Helm tests to verify the chart's correctness and ensure resources are rendered as expected. Run `helm test api-service` after deployment. See `templates/tests/test-connection.yaml` for an example.

### Task 5: Deploy to Kubernetes

The API service is designed to be deployed to a Kubernetes environment.

This solution has been tested on [**Minikube/k3s/GKE**].

**Bonus Points:**

* **Open Policy Agent (OPA) Integration**:
    * **Deployment**: OPA (with Gatekeeper) has been deployed to the cluster.
    * **Policy**: An OPA test policy is implemented to validate two key security practices for deployments:
        1.  **Non-default Service Account**: Ensures that deployments do not use the `default` service account.
        2.  **Non-root Container**: Validates that containers do not run as the `root` user (`runAsNonRoot: true` or `allowPrivilegeEscalation: false`).
    * The OPA policy definition can be found in [`./kubernetes/opa-policies`](./kubernetes/opa-policies).

### Task 6: Documentation

This `README.md` file serves as the primary documentation, providing clear instructions for building, deploying, and testing the service.

* **Clear Instructions**: Detailed steps are provided in the "How to Build, Deploy, and Test" section.
* **Meaningful Commit Messages**: Git commit messages reflect the changes made and their purpose.
* **In-code Comments**: Relevant comments are included in the source code and configuration files where complexity warrants explanation.

### Task 7: Additional Ideas

* **Automated Security Scanning**: Integration of tools like Trivy into the CI/CD pipeline for vulnerability scanning of Docker images.
* **Container Structure Tests**: Using `container-structure-test` for basic validation of the Docker image.
* **Prometheus Metrics**: Basic application-level metrics exposed via Prometheus client libraries for observability.
* **Structured Logging**: (If implemented) Using a structured logging library for easier log analysis.

---

## How to Build, Deploy, and Test

Follow these instructions to get the API service up and running.

### Prerequisites

Before you begin, ensure you have the following installed:

* [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [**Docker Desktop**](https://www.docker.com/products/docker-desktop/) or Docker Engine
* [**Node.js**](https://nodejs.org/en/download/) (if you want to run the API service locally without Docker initially)
* [**kubectl**](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [**Helm**](https://helm.sh/docs/intro/install/)
* A Kubernetes cluster (e.g., [**Minikube**](https://minikube.sigs.k8s.io/docs/start/), [**k3s/k3d**](https://k3d.io/), or access to a cloud-based cluster like [**GKE**](https://cloud.google.com/kubernetes-engine/docs/quickstart))

### Building the Docker Image

Navigate to the `api-service` directory and build the Docker image:

```bash
cd api-service
docker build -t api-service:latest .