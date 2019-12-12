# REDIS SENTINEL SERVICE CONTROLLER
First, if you want to access resource which pods and services you can set cluster-role-admin to your serviceaccount . 
```
kubectl create clusterrolebinding redis-operator-2 --clusterrole cluster-admin --serviceaccount=default:controller || true

```

Notice : I will update RBAC to more least priveleged