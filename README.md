# url-shortener

Url shortener service written in Python.
The app is deployed to Kubernetes

## Before you begin

### Install Helm
[Helm](https://helm.sh/) is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Locally

* Run `pip install -r requirements.txt` from the project directory.

### Docker

* Build the image by running `docker build -t url-shortener .` from the project directory. 

## Deployment

### Kubernetes

* Make sure you have [helm](https://helm.sh/) installed on your machine.
* From `k8s` directory, run `./deploy <image tag>.` 

Helm will deploy the app and it's dependencies to the currently selected Kubernetes cluster.

## Testing

### Unit tests

TBD

### Load testing

TBD

## Architecture