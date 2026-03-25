# 🚀 KubeHeal AI: Self-Healing Kubernetes via Anomaly Detection

**KubeHeal AI** is an intelligent infrastructure management tool that integrates Machine Learning (Isolation Forests) with the Kubernetes Python SDK to automate fault recovery. It monitors pod performance metrics and proactively "heals" the cluster by restarting anomalous pods before they cause system-wide failures.

---

## 🌟 Key Features
* **AI-Driven Monitoring**: Uses an unsupervised **Isolation Forest** model to detect multivariate anomalies in CPU and Memory usage.
* **Automated Remediation**: Automatically interacts with the K8s API to terminate and reschedule pods flagged as "unhealthy."
* **Zero-Config Simulation**: Includes a training pipeline that generates synthetic system stress data for model validation.
* **K8s Integration**: Built using the official `kubernetes-python` client for seamless cluster interaction.

---

## 🛠️ Technical Stack
* **Orchestration**: Kubernetes (Minikube), Kubectl
* **Language**: Python 3.8+
* **Machine Learning**: Scikit-Learn (Isolation Forest), Pandas, NumPy
* **DevOps Tools**: Docker, Kubernetes Python SDK

---

## 📂 Project Structure
* `train_model.py`: Generates synthetic telemetry data and trains the `IsolationForest` model.
* `monitor_and_heal.py`: The core engine. Loads the model, scans the K8s cluster, and executes healing actions.
* `anomaly_detection_model.pkl`: The serialized "brain" of the system.
* `webapp-deployment.yaml`: Sample Nginx deployment used for testing.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have a running Kubernetes cluster (Minikube recommended) and Python installed.
```bash
minikube start --driver=docker
pip install pandas scikit-learn kubernetes joblib

# Deploy the Web Application
kubectl create deployment webapp --image=nginx --replicas=3

# Train the AI Model
python3 train_model.py    #It will generate anomaly_detection_model.pkl

# Run the Sentinel
python3 monitor_and_heal.py

📊 How it Works
Data Ingestion: The script gathers CPU/Memory metrics from the running pods.

Inference: The data is passed through the Isolation Forest model.

Decision: If the anomaly_score == -1, the pod is marked for termination.

Self-Healing: The K8s API deletes the pod, and the Deployment controller automatically provisions a fresh, healthy replacement.