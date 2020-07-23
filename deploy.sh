#!/bin/bash
echo "Creating the volume..."
kubectl apply -f ./kubernetes/persistent-volume.yml
kubectl apply -f ./kubernetes/persistent-volume-claim.yml


echo "Creating the database credentials..."
kubectl apply -f ./kubernetes/secret.yml


echo "Creating the postgres deployment and service..."
kubectl create -f ./kubernetes/postgres-deployment.yml
kubectl create -f ./kubernetes/postgres-service.yml


echo "Creating the flask deployment and service..."
kubectl create -f ./kubernetes/flask-deployment.yml
kubectl create -f ./kubernetes/flask-service.yml


echo "Creating the vue deployment and service..."
kubectl create -f ./kubernetes/vue-deployment.yml
kubectl create -f ./kubernetes/vue-service.yml


echo "Adding the ingress..."
minikube addons enable ingress

echo "Pausing for Ingress to become available (takes up to a few minutes)..."
sleep 4m

echo "Creating ingress object..."
kubectl apply -f ./kubernetes/minikube-ingress.yml


echo "Creating and seeding the database..."
POD_NAME=$(kubectl get pod -l service=postgres -o jsonpath="{.items[0].metadata.name}")
kubectl exec $POD_NAME --stdin --tty -- createdb -U sample books

FLASK_POD_NAME=$(kubectl get pod -l app=flask -o jsonpath="{.items[0].metadata.name}")
kubectl exec $FLASK_POD_NAME --stdin --tty -- python manage.py recreate_db
kubectl exec $FLASK_POD_NAME --stdin --tty -- python manage.py seed_db


echo "Adding check.alive ip to /etc/hosts"
export HOSTS_ENTRY="$(minikube ip)    check.alive"
sudo grep "$HOSTS_ENTRY" /etc/hosts || sudo sed -i "1s/^/$HOSTS_ENTRY \n/" /etc/hosts
