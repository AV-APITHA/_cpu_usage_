import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load processed data
df = pd.read_csv("processed_data.csv")
X = df.drop("cpu_usage", axis=1)
y = df["cpu_usage"]
# Train RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save trained model
with open("model.pkl", "wb") as f:
  pickle.dump(model, f)

  

print("✅ Model trained → model.pkl")
