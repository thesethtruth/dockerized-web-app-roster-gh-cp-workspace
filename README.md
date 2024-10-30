# Simple Web App with Docker

This is a simple web application that uses Docker to containerize the frontend, backend, and database. The frontend is built with React, Daisy UI, and Tailwind CSS. The backend is built with FastAPI, and the database is SQLite.

## Prerequisites

- Docker
- Docker Compose

## Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/githubnext/workspace-blank.git
cd workspace-blank
```

2. Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

This will build and start the frontend, backend, and database services.

## Accessing the Application

- The frontend will be available at `http://localhost:3000`
- The backend API will be available at `http://localhost:8000`

## Stopping the Application

To stop the application, run:

```bash
docker-compose down
```

This will stop and remove the containers.

## Deploying to Azure using Terraform

1. Install Terraform: Follow the instructions on the [Terraform website](https://www.terraform.io/downloads.html) to install Terraform.

2. Configure Azure credentials: Set up your Azure credentials by following the instructions on the [Terraform Azure Provider documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs).

3. Initialize Terraform: Navigate to the `terraform` directory and run the following command to initialize Terraform:

```bash
cd terraform
terraform init
```

4. Apply the Terraform configuration: Run the following command to apply the Terraform configuration and deploy the application to Azure:

```bash
terraform apply
```

This will create the necessary resources in Azure and deploy the frontend, backend, and database containers.

5. Access the application: Once the deployment is complete, you can access the application using the public IP address or DNS name provided by Azure.
