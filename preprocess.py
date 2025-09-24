import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data.csv")

# One-hot encode controller_kind
df = pd.get_dummies(df, columns=["controller_kind"], drop_first=True)

# ✅ Select only required features
features = [
    

    "cpu_request",
    "mem_request",
    "cpu_limit",
    "mem_limit",
    "runtime_minutes"
] + [col for col in df.columns if col.startswith("controller_kind_")]

target = "cpu_usage"
# Drop missing values in selected columns
df = df[features + [target]].dropna()

# Split features & target
X = df[features]
y = df[target]

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Save processed data
processed = pd.DataFrame(X_scaled, columns=features)
processed["cpu_usage"] = y.reset_index(drop=True)
processed.to_csv("processed_data.csv", index=False)

print("✅ Preprocessing done, saved to processed_data.csv")
