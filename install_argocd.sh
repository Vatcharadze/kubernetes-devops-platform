#!/bin/bash

#Requirements-->
#Installed kubectl command-line tool.
#Have a kubeconfig file (default location is ~/.kube/config).
#CoreDNS. Can be enabled for microk8s by microk8s enable dns && microk8s stop && microk8s start

#Please run this script after starting Cluster.
kubectl create namespace argocd
kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

