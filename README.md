# Flask Random Dog App Deployment Guide

This guide will help you deploy a simple Flask application that displays a random dog image to Azure Kubernetes Service (AKS) using Azure Container Registry (ACR). Follow the steps below to build, push, and deploy your application.

## Prerequisites

1. **Azure CLI**: Ensure you have the Azure CLI installed. You can download it [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
2. **Docker**: Ensure you have Docker installed. You can download it [here](https://www.docker.com/products/docker-desktop).
3. **Kubernetes CLI (kubectl)**: Ensure you have kubectl installed. Instructions can be found [here](https://kubernetes.io/docs/tasks/tools/).
4. **An Azure account**: Sign up [here](https://azure.microsoft.com/en-us/free/).
5. **Flask and requests**: TO run a Flask app successfully, you need to install the depenceies by running "pip install Flask requests"

## Step 1: Build and Push Docker Image to ACR

### 1.1 Login to Azure

```sh
az login

#create a resource group
az group create --name myResourceGroup --location eastus

#Create an ACR instance
az acr create --resource-group myResourceGroup --name myACRRegistry --sku Basic

#Login to ACR
az acr login --name myACRRegistry

#Build your image
docker build -t myapp:v1 .

#Tag your image
docker tag myapp:v1 myacr.azurecr.io/myapp:v1

#Push your image to ACR
docker push myacr.azurecr.io/myapp:v1

## Step 2: Deploy to AKS
#Create AKS cluster
az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 1 --enable-addons monitoring --generate-ssh-keys

#Get AKS creds
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster

#Create secret
kubectl create secret docker-registry myacrsecret \
  --docker-server=mannieacr.azurecr.io \
  --docker-username=<acr-username> \ #Use application ID of service principal
  --docker-password=<acr-password>  #use value ID of service principal

#Deploy application
kubectl apply -f deployment.yaml

#Verify
kubectl describe deployment myapp-deployment

#Display App
To display your app on the browser, use service external IP of the app.




```
