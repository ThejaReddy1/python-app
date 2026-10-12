Creating a new Helm chart for the Python application.
```bash
helm create python-app
```
It will create the chart for your deployment and then update the values.yaml as per your requirement. 



# Installing Argo CD using Helm
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo list
helm upgrade --install argocd argo/argo-cd -f values-argo.yaml -n d --create-namespace 
k get ing -n argocd
k get secret -n argocd
k get secrets -n argocd argocd-initial-admin-secret -o yaml
echo "<secret>" | base64 -d
```


# Running Self Hosted GitHub Runners in kubernetes

Refer to the [Actions Runner Controller repository](https://github.com/actions-runner-controller/actions-runner-controller).

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml

helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm upgrade --install --namespace actions-runner-system --create-namespace  --set=authSecret.create=true  --set=authSecret.github_token="<pat_Token>"  --wait actions-runner-controller actions-runner-controller/actions-runner-controller
```

### Create a Runner Deployment
```bash
cat <<EOF | kubectl apply -n actions-runner-system -f -
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: self-hosted-runner
spec:
  replicas: 1
  template:
    spec:
      repository: <your-github-username>/<your-repo-name>
EOF
```

# Installing Argo CD  CLI using curl

```bash
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

[Argo CD CLI installation](https://argo-cd.readthedocs.io/en/stable/cli_installation/)

### validate Argo CD CLI installation
```bash
argocd version
```

### login to Argo CD
```bash
argocd login <argocd-server> --username admin --password <password> --insecure --grpc-web
```
### Argo CD Application Management

### create an app
```bash
argocd app create <app-name> --repo <repo-url> --path <path> --values <values-file> --dest-server <dest-server> --dest-namespace <dest-namespace> 
```

### List apps 
```bash
argocd app list
```

### Get app details
```bash
argocd app get <app-name>
```

### Sync an app
```bash
argocd app sync <app-name>
```

### Delete an app
```bash
argocd app delete <app-name>
```

### Logout from Argo CD
```bash
argocd logout <argocd-server>
```