# simple-project-on-k8s

## Deployment

```console
kubectl apply -f storageclass.yaml && \
kubectl apply -f host-vm/ -R && \
kubectl apply -f mongodb/ -R && \
kubectl apply -f redis-broker/ -R && \
kubectl apply -f redis-cache/ -R && \
kubectl apply -f tick/ -R && \
kubectl apply -f google-cloud-storage-proxy/ -R && \
kubectl apply -f simple-api/ -R && \
kubectl apply -f simple-frontend/ -R && \
kubectl apply -f ingress.yaml
```

## Related Posts

- [The incomplete guide to Google Kubernetes Engine](https://vinta.ws/code/the-complete-guide-to-google-kubernetes-engine-gke.html)
