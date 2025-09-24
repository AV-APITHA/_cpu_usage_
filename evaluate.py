import pandas as pd
import pickle, json
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load processed data
df = pd.read_csv("processed_data.csv")
X = df.drop("cpu_usage", axis=1)
y = df["cpu_usage"]
# Load trained model
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

 

# Predict
y_pred = model.predict(X)

# Metrics
metrics = {
    

    "RMSE": mean_squared_error(y, y_pred) ** 0.5,
     "MAE": mean_absolute_error(y, y_pred),
      "R2": r2_score(y, y_pred)
}

# Save metrics
with open("metrics.json", "w") as f:
  json.dump(metrics, f, indent=4)

                    

print("✅ Evaluation done → metrics.json")
  
