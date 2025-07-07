DevOps Challenge

This repository addresses a DevOps challenge to assess technical proficiency in Software Engineering, DevOps, and Infrastructure tasks. Below is a detailed description of the tasks and requirements.

Overview

This exercise consists of several subtasks to evaluate your skills across various domains. You are not required to complete all tasks but should aim to showcase your strengths and explore new areas. The task is expected to take 2-4 hours. For any questions, feel free to reach out.

Tasks

0. Create a Public Git Repository

Create a public Git repository for the source code using your preferred provider (e.g., GitHub, GitLab, Bitbucket).

1. Create an API Service

Develop a simple web application that prints the request headers, method, and body. Choose your preferred tech stack and programming language.

Example Test Case:

curl --header "Content-Type: application/json" --data '{"username":"xyz","password":"xyz"}' http://${URL}:${PORT}/api

Expected Response:

Welcome to our demo API, here are the details of your request:

***Headers***:
Content-Type: application/json

***Method***:
POST

***Body***:
{"username":"xyz", "password":"xyz"}

Bonus Points:





Follow best practices for cloud-native applications (e.g., The Twelve-Factor App principles).



Instrument the code with a Prometheus counter or gauge using Prometheus client libraries.

2. Dockerize

Create a Dockerfile to build a Docker image and automate the setup of your API service, enabling it to run anywhere with one or two commands.

Bonus Points:





Apply Docker best practices: proper layer structure, multi-stage builds if needed, and security practices for building/running containers.



Include a simple integration test for the Dockerfile using container-structure-test or similar tools.

3. CI/CD

Integrate the application with a CI/CD pipeline using GitHub Actions or another technology to automate the process from code commit to deployment.

4. Create a Helm Chart

Create a Helm chart to package your service, ensuring it includes all components required for a production-like environment (e.g., service, ingress, RBAC entities). Include 3rd-party dependencies if necessary.

Bonus Points:





Implement Helm hooks for running migrations.



Include Helm tests for verification.

5. Deploy to Kubernetes

Deploy the service to your preferred Kubernetes environment (e.g., Minikube, k3s, GKE) and verify it works as expected.

Bonus Points:





Deploy Open Policy Agent (OPA) into the cluster.



Implement an OPA test policy to validate that deployments use a non-default service account and containers do not run as the root user.

6. Documentation





Create a README.md file with clear instructions on how to build, deploy, and test the service.



Provide a reasonable amount of documentation, including comments where necessary, without documenting every line of code or configuration.



Use meaningful commit messages in Git.



Include #TODO comments for shortcuts taken or approaches you would handle differently in a production environment.

7. Additional Ideas

Implement creative solutions to optimize the workflow or automate deployment. Showcase innovative ideas or tools to enhance the project.

Results

Submit only the public Git repository address containing your project.

Hints





No Kubernetes cluster? Consider using Minikube, k3s/k3d, or GKE (note that GKE may incur costs).



Ensure all scripts and code are compatible with Linux or macOS.



Use any information sources you need.



Aim to spend no more than 4 hours on the project.

Good Luck!

We look forward to seeing your solution and creativity in tackling this challenge!