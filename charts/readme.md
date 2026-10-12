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

Pls refer this link <https://github.com/actions-runner-controller/actions-runner-controller>

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