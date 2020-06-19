# url-shortener

Url shortener service written in Python.
The app is deployed to Kubernetes

## Before you begin

### Install Helm
[Helm](https://helm.sh/) is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Install dependencies locally

* Run `pip install -r requirements.txt` from the project directory.

### Or via docker

* Build the image by running `docker build -t url-shortener .` from the project directory. 

## Deployment

### Kubernetes

* Make sure you have [helm](#install-helm) installed on your machine.
* From `k8s` directory, run `./deploy <image tag>.` 

Helm will deploy the app and it's dependencies to the currently selected Kubernetes cluster.

## Testing

### Load testing

Load testing is done using [Molotov](https://molotov.readthedocs.io/en/stable/). 
To start hammering the server with roughly 10k VU/s, run: 

```
molotov test/load_test.py -w 1000 -p 10 -v
```   

The script points to `localhost:8080` by default, to change it, set `MOLOTOV_HOSTNAME` environment variable:

```
 MOLOTOV_HOSTNAME=http://34.89.107.231 molotov test/load_test.py -w 1000 -p 10 -v
```

## Design

### UrlShortener

UrlShortener class is responsible for getting a unique id for any given URL.

### Server

Server class is responsible for creating an `aihttp.web.Application` for serving traffic. Request handlers are defined in [RequestHandler](#requesthandler) class.

### RequestHandler

RequestHandler class is responsible for handling HTTP requests.

* `shorten_url` POST method responds with an id for any particular URL.
* `redirect` GET method redirects to the original URL found by key. If no URL was found, it responds with a 404 error.