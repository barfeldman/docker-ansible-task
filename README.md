# Docker-Compose Deployment Automation on CentOS Using Ansible

## Overview
This project sets up an automated way to deploy Docker Compose services on a CentOS server using Ansible. It includes secure handling of credentials, organized folder structures, and pulls Docker images and configurations directly from GitHub.

## Requirements
- A CentOS server connected to the internet to download Docker and retrieve files from GitHub.
- Ansible installed on the control machine.
- A GitHub repository with the Docker Compose file.

## Process Summary

### 1. Install Docker and Docker Compose
The playbook ensures Docker and Docker Compose are installed along with any necessary dependencies.

### 2. Secure Docker Hub Login and Image Pull
Using encrypted credentials, the playbook securely logs in to Docker Hub and pulls the required images for deployment.

### 3. Deploy Services with Docker Compose
The playbook pulls the Docker Compose configuration file from GitHub and starts the services as defined in the file.

### 4. Verify and Test Services
Ansible verifies the services are up and accessible, runs diagnostic checks using `nmap`, and confirms the connectivity between containers.

## Folder Layout
This project is organized to make it easy to deploy and manage. Key parts include:
- **Playbooks**: The main automation files.
- **docker_setup**: A files for setting up Docker.
- **Basic Architecture**: Contains architecture picture for basic understanding.

## Security
Sensitive information, like Docker Hub credentials, is encrypted using Ansible Vault, making the deployment process secure.

## How to Run
1. Set up your Vault password file for secure access to credentials.
2. Run the playbook using:
   ```bash
   ansible-playbook ansible/playbooks/deploy_docker_compose.yml --ask-vault-pass
