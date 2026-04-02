#!/usr/bin/env python
# coding: utf-8

# MobileSphere: Mobile Price Prediction and Market Analysis using Machine Learning”
This project analyzes mobile phone specifications and predicts mobile prices using machine learning models. The project includes data cleaning, exploratory data analysis, feature engineering, model building, and comparative evaluation using performance metrics such as R², MAE, MSE, and RMSE.
# Data Gathering

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


# In[ ]:


df = pd.read_csv("Mobile_data.csv")
df.head()


# DATA CLEANING

# In[ ]:


df.info()
df.isnull().sum()
df = df.dropna()
df = df.drop_duplicates()


# EDA 

# In[ ]:


plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title("Price Distribution")
plt.show()


# In[ ]:


plt.figure(figsize=(12,6))
sns.boxplot(x='Brand', y='Price', data=df)
plt.xticks(rotation=90)
plt.title("Brand vs Price")
plt.show()


# In[ ]:


sns.scatterplot(x='RAM (MB)', y='Price', data=df)
plt.title("RAM vs Price")
plt.show()


# In[ ]:


sns.scatterplot(x='Internal storage (GB)', y='Price', data=df)
plt.title("Storage vs Price")
plt.show()


# In[ ]:


sns.scatterplot(x='Battery capacity (mAh)', y='Price', data=df)
plt.title("Battery vs Price")
plt.show()


# In[ ]:


sns.scatterplot(x='Rear camera', y='Price', data=df)
plt.title("Camera vs Price")
plt.show()


# In[ ]:


plt.figure(figsize=(10,6))
numeric_df = df.select_dtypes(include=['int64','float64'])
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()


# FEATURE ENCODING

# In[ ]:


df = pd.get_dummies(df, drop_first=True)


# In[ ]:


import pickle

columns = X.columns
pickle.dump(columns, open("columns.pkl", "wb"))


# TRAIN AND TEST 

# In[ ]:


from sklearn.model_selection import train_test_split

X = df.drop("Price", axis=1)
y = df["Price"]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[ ]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# MACHINE LEARNING MODELS

# In[ ]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)
pred_lr = lr.predict(x_test)


# In[ ]:


from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
pred_dt = dt.predict(x_test)


# In[ ]:


from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

rf.fit(x_train, y_train)
pred_rf = rf.predict(x_test)


# In[ ]:


import pickle
pickle.dump(rf, open("mobile_model.pkl", "wb"))


# In[ ]:


from sklearn.ensemble import GradientBoostingRegressor

gb = GradientBoostingRegressor(
    n_estimators=400,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

gb.fit(x_train, y_train)
pred_gb = gb.predict(x_test)


# MODEL COMPARISON

# In[ ]:


from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import numpy as np

models = {
    "Linear": pred_lr,
    "Decision Tree": pred_dt,
    "Random Forest": pred_rf,
    "Gradient Boost": pred_gb
}

for name, pred in models.items():
    print(name)
    print("R2:", r2_score(y_test, pred))
    print("MAE:", mean_absolute_error(y_test, pred))
    print("MSE:", mean_squared_error(y_test, pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
    print("------")


# In[ ]:


from sklearn.metrics import r2_score

print("Random Forest R2:", r2_score(y_test, pred_rf))
print("Gradient Boost R2:", r2_score(y_test, pred_gb))


# In[ ]:


from sklearn.ensemble import GradientBoostingRegressor

gb = GradientBoostingRegressor()
gb.fit(x_train, y_train)


# In[ ]:


from altair.vegalite.v5 import data
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data\clean_mobile_data.csv")

# Encoding
df_encoded = pd.get_dummies(df)

# Features & Target
X = df_encoded.drop("Price", axis=1)
y = df_encoded["Price"]

# Save columns
columns = X.columns
pickle.dump(columns, open("columns.pkl1", "wb"))

# Split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
rf = RandomForestRegressor()
rf.fit(x_train, y_train)

# Save model
pickle.dump(rf, open("mobile_model.pkl1", "wb"))

