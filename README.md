# QuickBite — Food Ordering Application on Amazon EKS

QuickBite is a small real-world food ordering application designed as a cloud-native DevOps project.

Users can browse a food menu, add items to a cart and place an order. The application is containerized with Docker and deployed on Amazon EKS. AWS infrastructure is provisioned with Terraform and Kubernetes manages the application workload.

## Architecture

GitHub → Jenkins → Docker → Amazon ECR → Terraform → Amazon EKS → Kubernetes Service → AWS Load Balancer → Browser

## Technologies

- Python / Flask
- HTML / CSS / JavaScript
- Docker
- Kubernetes
- Amazon EKS
- Terraform
- AWS VPC
- Amazon ECR
- Jenkins
- Trivy
- AWS CLI
- kubectl

## Features

- Food menu
- Shopping cart
- Order placement
- Order ID generation
- Health endpoint
- Kubernetes readiness/liveness probes
- Two application replicas

## Deploy Infrastructure

Configure AWS credentials and verify them:

    aws sts get-caller-identity

Then:

    cd terraform
    terraform init
    terraform fmt -recursive
    terraform validate
    terraform plan
    terraform apply

This creates the VPC and EKS infrastructure.

## Build and Push Image

Create an ECR repository:

    aws ecr create-repository --repository-name quickbite --region us-east-2

Authenticate:

    aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-2.amazonaws.com

Build:

    docker build -t quickbite ./app

Tag:

    docker tag quickbite:latest <ACCOUNT_ID>.dkr.ecr.us-east-2.amazonaws.com/quickbite:latest

Push:

    docker push <ACCOUNT_ID>.dkr.ecr.us-east-2.amazonaws.com/quickbite:latest

Replace the placeholder image in kubernetes/deployment.yaml with your ECR image URI.

## Configure kubectl

    aws eks update-kubeconfig --region us-east-2 --name quickbite-eks

Verify:

    kubectl get nodes

## Deploy Application

    kubectl apply -f kubernetes/namespace.yaml
    kubectl apply -f kubernetes/deployment.yaml

Check:

    kubectl get pods -n quickbite
    kubectl get svc -n quickbite

Open the external LoadBalancer hostname shown by the service.

## CI/CD

The Jenkins pipeline demonstrates:

1. Git checkout
2. Terraform formatting and validation
3. Docker image build
4. Trivy image scan
5. Terraform plan

Credentials should be stored in Jenkins/AWS credential management and never committed to GitHub.

## Cleanup

    kubectl delete namespace quickbite
    cd terraform
    terraform destroy

## Author

Kuricheti Alekhya

B.Tech — Computer Science and Business Systems
