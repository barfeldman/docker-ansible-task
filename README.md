# Docker-Compose Deployment Automation on CentOS Using Ansible

## Introduction
This project aims to deploy a secure, automated environment to run Docker Compose services on a CentOS server using Ansible. The automation includes encrypted credentials handling, structured folder organization, and integration with external Docker images and configuration from GitHub.

## Prerequisites
- CentOS server with access to the internet for Docker and GitHub repository retrieval.
- Ansible installed on a control node.
- GitHub repository with the Docker Compose file.

## Steps Overview

### 1. Docker and Docker-Compose Setup
The playbook ensures the installation of required Docker and Docker Compose dependencies.

### 2. Docker Hub Login and Image Pull
The encrypted credentials allow login to Docker Hub securely to pull necessary images.

### 3. Docker Compose Service Deployment
The playbook uses Docker Compose to deploy the specified services with configurations pulled directly from GitHub.

### 4. Service Verification and Diagnostics
Ansible checks service health, runs diagnostics using nmap, and verifies connectivity between containers.

## Folder Structure
This project follows a structured approach for ease of deployment and maintenance. Key components include:
- **Playbooks**: Main automation scripts.
- **Roles**: Modular role for Docker installation and setup.
- **Group Vars**: Centralized variable management for the entire environment.
- **Docs**: Explanation and architecture diagram for comprehensive understanding.

## Security
Sensitive information like Docker Hub credentials is encrypted with Ansible Vault, ensuring data security.

## Usage
1. Configure the Vault password file for secure credentials.
2. Run the playbook with the command:
   ```bash
   ansible-playbook ansible/playbooks/deploy_docker_compose.yml --ask-vault-pass
