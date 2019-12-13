import json
import yaml
import os
import time
import logging
from redis_svc import Connect
from kubernetes import client, config, watch, kubernetes


def check_label(label):
    state = True

    master_label = "master"

    if master_label != label:
        state = False

    return state

def get_cluster_config():
    if 'KUBERNETES_PORT' in os.environ:
        config.load_incluster_config()
    else:
        config.load_kube_config()

    configuration = client.Configuration()
    configuration.assert_hostname = False

    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))

    return api_instance

    


if __name__ == "__main__":

    api_instance = get_cluster_config()
    obj = Connect()

    namespace = os.environ["REDIS_CLUSTER_NAMESPACE"]

    while True:
        REDIS_POD_IP=obj.get_master()
        print(REDIS_POD_IP)
        api_response = api_instance.list_namespaced_pod(namespace)
        datas = api_response.items

        for data in datas:
            print(REDIS_POD_IP)
            time.sleep(20)
            if data.status.pod_ip == REDIS_POD_IP:
                print(data.metadata.labels)
                pod_name = data.metadata.name

                if check_label(data.metadata.labels["role"]) == False:
                    status = api_instance.patch_namespaced_pod(pod_name, namespace, {"metadata":{"labels":{"role":"master"}}})
                    print(status)
                else: 
                    print("No Update")

