import joblib
import numpy as np
from kubernetes import client, config
from sklearn.ensemble import IsolationForest

# 1. Loading or invoking  your pre-trained model
model = joblib.load('anomaly_detection_model.pkl')

# 2. Initialize Kubernetes client
config.load_kube_config()
v1 = client.CoreV1Api()

# 3. Get all pods with the label 'app=webapp'
# This ensures we find your three running pods automatically
pods = v1.list_namespaced_pod(namespace="default", label_selector="app=webapp") #If your labels are different then make sure to change put it here accordingly

# 4. Simulate checking each pod for anomalies
for pod in pods.items:
    pod_name = pod.metadata.name

    # Simulating data: Let's pretend pod 'lbxq6' has a CPU spike
    if "lbxq6" in pod_name:
        cpu_usage, memory_usage = 95.0, 80.0  # Anomaly!
    else:
        cpu_usage, memory_usage = 50.0, 60.0  # Normal

    data = np.array([[cpu_usage, memory_usage]])

    #  Predicting
    prediction = model.predict(data)

    if prediction[0] == -1:
        print(f"!!! Anomaly detected in Pod: {pod_name} !!!")
        print("Triggering self-healing: Deleting the anomalous pod.")

        # Self-healing action
        v1.delete_namespaced_pod(name=pod_name, namespace="default")
        print(f"Action Complete: {pod_name} is being replaced by Kubernetes.")
    else:
        print(f"Pod {pod_name} is healthy (CPU: {cpu_usage}%).")
