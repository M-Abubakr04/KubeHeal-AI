import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest # Corrected import
import joblib

# We are creating this dummy data for the sake of practice it includes Cpu and Memory metrics
np.random.seed(42)
data = {
    "cpu_usage": np.random.normal(50, 5, 1000),         #Setting Highest Cpu usage to 50%
    "memory_usage": np.random.normal(60, 10, 1000)      #Setting Highest Memory usage to 60%
}
# Introducing Anomalies for the sake of practicing
data["cpu_usage"][200:250] = np.random.normal(90, 5, 50)
data["memory_usage"][400:450] = np.random.normal(20, 5, 50)
df = pd.DataFrame(data)

# Training the Model
model = IsolationForest(contamination=0.05)
model.fit(df)

# Saving the model
joblib.dump(model, 'anomaly_detection_model.pkl')
#Verifying
print("Model trained and saved as anomaly_detection_model.pkl")
