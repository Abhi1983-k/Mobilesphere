# 🎓 Project Title

**Mobilesphere: Mobile Phone Pricing Prediction Using Machine Learning**

---

## 🧩 Problem Statement

The mobile phone market is highly dynamic, with prices depending on multiple independent variables such as RAM, storage, battery capacity, camera specifications, screen size, and brand. The relationship between these features and the final price is often complex and not strictly linear. 

Therefore, there is a need for an intelligent predictive model that can learn pricing patterns from historical data. The goal of this project is to accurately predict the continuous price of a mobile phone based on its hardware and software specifications.

---

## 📖 Project Description

**Mobilesphere** is a machine learning-based project designed to predict mobile phone prices. The model analyzes various smartphone attributes (like Battery Capacity, RAM, Internal Storage, Camera Megapixels, Operating System, and Brand) to estimate the device's market price.

The project involves comprehensive data preprocessing, handling missing values, encoding categorical variables, and applying both linear and ensemble regression algorithms. By capturing patterns from existing mobile data, the system provides valuable pricing insights that can assist manufacturers, retailers, and consumers in making informed decisions.

---

## 📊 Dataset Description

The dataset consists of **Mobile Phone Specifications** containing both numerical and categorical features. Each row represents a specific smartphone model, and the features describe its hardware, software, and connectivity capabilities.

* **Brand & Model** – Manufacturer and device name (e.g., Apple iPhone 11)
* **Battery capacity (mAh)** – Size of the battery
* **Screen size (inches)** & **Resolution** – Display specifications
* **RAM (MB)** & **Internal storage (GB)** – Memory and storage capacities
* **Front & Rear camera** – Megapixel counts for both cameras
* **Operating system** – Android, iOS, Windows, etc.
* **Connectivity** – Wi-Fi, Bluetooth, GPS, 3G/4G/LTE support
* **Price (Target Column)** – The market price of the mobile phone

Each row represents a unique mobile phone in the market.

---

## 🎯 Target Variable (Dependent Variable)

### **Price**

The target variable represents the market price of the mobile phone.

Since the price is a continuous numerical value, this is a **regression problem**, where the goal is to predict the exact or approximate cost of the device based on its attributes.

---

## 🛠️ Methodology

1. **Data Loading and Exploration**
    * Importing the mobile dataset
    * Understanding the structure, rows, and columns
    * Checking for null or missing values

2. **Data Cleaning**
    * Handling missing values appropriately
    * Removing inconsistencies in specifications
    * Encoding categorical variables (e.g., Brand, Operating System)
    
3. **Feature Engineering**
    * Normalizing/Scaling numerical features like Battery Capacity and RAM
    * Transforming features to better represent non-linear relationships

4. **Exploratory Data Analysis (EDA)**
    * Distribution of mobile prices across different brands
    * Correlation between RAM/Storage and Price
    * Impact of Battery Capacity and Camera specs on the final price

5. **Train-Test Split**
    * Splitting the dataset into training and testing sets to evaluate model generalization

6. **Model Training**
    Training supervised machine learning regression models:
    * Linear Regression
    * Random Forest Regressor

7. **Model Evaluation & Comparison**
    * Evaluating models using standard regression metrics
    * Comparing the baseline Linear model with the advanced Random Forest model
    * Analyzing why certain models capture complex device pricing better

---

## 🤖 Machine Learning Models Used

The following regression algorithms are implemented and compared:

* **Linear Regression** – Used as a baseline model due to its simplicity and interpretability. It helps in understanding the linear impact of specific features on the price.
* **Random Forest Regressor** – An ensemble learning method chosen for its ability to capture complex, non-linear relationships between phone features (like brand value + camera quality) and price, effectively reducing overfitting.

---

## 📈 Evaluation Metrics

To measure the performance and accuracy of the regression models, the following metrics are used:

* **R² Score (Coefficient of Determination)** – Measures the proportion of variance in the price that is predictable from the features.
* **Mean Absolute Error (MAE)** – Shows the absolute average distance between the predicted price and the actual price.
* **Mean Squared Error (MSE) / Root Mean Squared Error (RMSE)** – Penalizes larger errors, giving insight into the model's prediction accuracy.

---

## ✅ Expected Outcome

* Accurate and robust prediction of mobile phone prices.
* Identification of key features (like RAM, Brand, or Storage) that heavily influence a phone's market value.
* A clear comparison showing that ensemble models (Random Forest) outperform linear models by capturing non-linear pricing interactions.
* A solid foundation for a deployable pricing engine for e-commerce platforms or a dynamic dashboard for market analysts.
---
