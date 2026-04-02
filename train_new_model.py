import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "cleaned_mobile_data.csv")

# Load dataset
df = pd.read_csv(data_path)

# Drop unnecessary columns that could cause overfitting or are just IDs
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)
if "Name" in df.columns:
    df.drop("Name", axis=1, inplace=True)
if "Model" in df.columns:
    df.drop("Model", axis=1, inplace=True)

# Separate features and target
X = df.drop("Price", axis=1)
y = df["Price"]

# Encode categorical features
X_encoded = pd.get_dummies(X)

# Ensure the column names of X_encoded are saved properly
columns = X_encoded.columns.tolist()
columns_path = os.path.join(BASE_DIR, "columns.pkl")
with open(columns_path, "wb") as f:
    pickle.dump(columns, f)

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train the model
rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42
)
rf.fit(x_train, y_train)

# Save the trained model
model_path = os.path.join(BASE_DIR, "mobile_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(rf, f)

print("Model trained and saved successfully.")
