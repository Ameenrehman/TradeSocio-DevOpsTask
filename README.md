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
  - [Task 5: Deploy to Openshift ( Redhhat Openshift Sandbox K8 Free Trial)](#task-5-Deploy-to-Openshift)
  - [Task 6: Documentation](#task-6-documentation)
  - [Task 7: Additional Ideas](#task-7-additional-ideas)
- [How to Build, Deploy, and Test](#how-to-build-deploy-and-test)
  - [Prerequisites](#prerequisites)
  - [For Local Testing:](#for-local-testing)
  - [For Prod Testing:](#for-prod-testing)
  - [Get URL](#get-url)
  - [Curl:](#curl)

---

## Project Overview

This project implements a simple Flask application that echoes request details (headers, method, and body). It's designed to showcase a full DevOps lifecycle, from development to automated deployment on Kubernetes. The aim was to deliver a solution that is robust, scalable, and easy to manage. This app is deployed on Redhat Openshift Sandbox (30 day trial version) for better testing and availability.

---

## Tasks Completed

Here's a breakdown of the tasks addressed in this repository:

### Task 0: Public Git Repository

This repository itself serves as the public Git repository for the source code, hosted on GitHub:
`https://github.com/Ameenrehman/TradeSocio-DevOpsTask.git`

### Task 1: API Service

The API service is implemented using [**Flask**].
You can find the source code in the [`./Api-APP/src/app.py`](./Api-APP/src/app.py) directory.

**Key Features & Best Practices:**

* **Technology Stack**: Flask and Python for building simple api service.
* **Request Echoing**: Captures and displays request headers, method, and body as specified.
* **Cloud-Native Principles**:
    * Adherence to clout native principle like explicitly declares dependencies, variables for configuration, application is stateless, Port Binding, while making the app.py service.
* **Instrumentation (Bonus)**:
    * **Prometheus Metrics**: The application is instrumented with a [**Prometheus Counter/Gauge**] to track [**Counter (http_requests_total), Histogram (http_request_duration_seconds), Summary (http_request_size_bytes), Gauge (http_requests_in_progress)**]. 
    You can access these metrics at the `/metrics` endpoint.

### Task 2: Dockerize

A `Dockerfile` is provided to containerize the API service. This allows for consistent execution across various environments.

You can find the `Dockerfile` in the [`./Api-APP/Dockerfile`](./Api-APP/Dockerfile) directory.

**Docker Best Practices Applied (Bonus):**

* **Multi-stage Build**: Utilizes a multi-stage build to create a small, efficient production image by separating build-time dependencies from runtime dependencies.
* **Proper Layer Structure**: Arranges `COPY` and `RUN` instructions to maximize Docker layer caching, speeding up subsequent builds.
* **Non-root User**: The container runs as a non-root user for enhanced security..
* **Integration Test (Bonus)**:
    * A simple integration test for the Docker image is included using [**container-structure-test.yaml**]. The test validates [**"flask existence, app.py existence, requirement.txt file existence, non-root user presence"**]. You can find the test configuration in [`./Api-APP/container-structure-test.yaml`](./container-structure-test.yaml).

### Task 3: CI/CD

A CI/CD pipeline is implemented using [**GitHub Actions**] to automate the build, test, and (optional) deployment process.

The GitHub Actions workflow definition is located at [`./.github/workflows/deploy.yml`](./.github/workflows/deploy.yml).

**Pipeline Stages and Steps:**

1.  **Build and Deploy**: For simplicity i have added only one stage with all necessary steps/jobs.
    * Set up JOb -> Checkout Source Code -> Cache pip dependency -> Setup Docker Buildx -> Cache Docker Layers -> Install Openshift CLI -> Config AWS Credentials -> Login ECR -> Build Docker Image -> Install container structure library -> Pull image for container structure test -> login to openshift -> Create secret for ECR -> Install Helm -> Deploy via Helm -> Helm test -> Show app url and curl url 


### Task 4: Helm Chart

A Helm chart is created to package the API service for deployment to Openshift, ensuring all necessary components for a production-like environment are included.

The Helm chart is located in the [`./api-app-chart`](./api-app-chart) directory.

**Chart Components:**

* **Deployment**: Manages the API service pods.
* **Service**: Exposes the API service within the cluster.
* **Route**: Provides external access to the API service via routes.
* **Gatekeeper**: Provides OPA #TODO ( this is not tested as openshift sandbox doesnt have cluster admin level privileges )
* **Values**: Provide values for our templates in helm cchart

**Bonus Points:**
* **Helm Tests**: Includes Helm tests to verify the chart's correctness and ensure resources are rendered as expected. Run `helm test api-service` after deployment. See `templates/tests/test-connection.yaml` for an example.

### Task 5: Deploy to Openshift ( Redhhat Openshift Sandbox K8 Free Trial)

The API service is designed to be deployed to a Kubernetes environment.

This solution has been tested on [**Opendhift/minikube**].

**Bonus Points:**

* **Open Policy Agent (OPA) Integration**:
    * **Deployment**: OPA (with Gatekeeper) has been made to be deployed to the cluster. #TODO ( not tested due to insufficient acces on oepnshift)
    * **Policy/template**: An OPA test policy is implemented to validate two key security practices for deployments: #TODO ( not executed just place the file)
        1.  **Non-default Service Account**: Ensures that deployments do not use the `default` service account.
        2.  **Non-root Container**: Validates that containers do not run as the `root` user 
    * The OPA policy definition can be found in [`./api-app-cahrt/templates/gatekeeper-template.yaml`](./gatekeeper policy template).

### Task 6: Documentation

This `README.md` file serves as the primary documentation, providing clear instructions for building, deploying, and testing the service.

### Task 7: Additional Ideas: (Suggestions)

* **Automated Security Scanning**: Integration of tools like Trivy into the CI/CD pipeline for vulnerability scanning of Docker images.
* **Prometheus Metrics**: Basic application-level metrics exposed via Prometheus client libraries for observability.
* **Structured Logging**: (If implemented) Using a structured logging library for easier log analysis.

---

## How to Build, Deploy, and Test

Follow these instructions to get the API service up and running.

### Prerequisites

Before you begin, ensure you have the following installed:
* [**VS CODE**]
* [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [**Docker Desktop**](https://www.docker.com/products/docker-desktop/) or Docker Engine for local testing 
* [**kubectl**](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [**Helm**](https://helm.sh/docs/intro/install/)
* [**Docker **]
* A Kubernetes cluster (e.g., [**Minikube**](https://minikube.sigs.k8s.io/docs/start/), Openshift Sandbox)

### For Local Testing:
### Clone the Repo
` git clone https://github.com/Ameenrehman/TradeSocio-DevOpsTask.git `

After cloning the repo, open the folder with vs code or any other.

### Build & RUN Docker Image
```bash
cd Api-APP
docker build -t api-app .
docker run -d -p 5000:5000 --name api-app api-app
```

This will run your api servie app on `localhost:5000` using docker desktop.

### For Prod Testing:
### Clone repo
` git clone https://github.com/Ameenrehman/TradeSocio-DevOpsTask.git `

After cloning copying the folder remove the .git from it and move the folder/files to your git initialize folder

### Setup Github Secrets and ENV Variable
Before running it on Github Action your repo should have ENV/secrets store in github:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
OPENSHIFT_SERVER_URL
OPENSHIFT_TOKEN

For AWs Acess key and secret access key, refer : `https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html`.

For openshift server url and toker , First make a trial accoutn on: `https://www.redhat.com/en/technologies/cloud-computing/openshift/openshift-developer-sandbox-trial` .
Then, after siging up , go to your username ( top right) -> copy login command -> then take the server url and token from there.
Now you are good to go.

### Running Github Action
So when you push in any of the directory :
    ```- 'Api-APP/**'
      - 'k8s/**'
      - 'api-app-chart/**'
    ```
your pipeline will automatically gets triggered, or you can manually trigger the pipeline using workflow dispatch after pushing the code to your repo.

### Get URL
* You can see the app up running on : `https://api-app-route-ameen2607-dev.apps.rm3.7wse.p1.openshiftapps.com`  or `https://api-app-route-ameen2607-dev.apps.rm3.7wse.p1.openshiftapps.com/metrics`. ( or see the url of route in github action output)

### Curl:
 `curl --header "Content-Type: application/json" --data '{"username":"devops","password":"challenge"}' http://api-app-service-ameen2607-dev.apps.rm3.7wse.p1.openshiftapps.com/api`.

*^NOTE: Route: `http://api-app-route-ameen2607-dev.apps.rm3.7wse.p1.openshiftapps.com`.

        Curl: `http://api-app-service-ameen2607-dev.apps.rm3.7wse.p1.openshiftapps.com/api` .

As routes are used to access the application , they cant be curl, so instead use the exposed service of the app to route it.

