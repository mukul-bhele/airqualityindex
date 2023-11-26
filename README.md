# Air Quality Index Prediction Project

## Overview

This comprehensive project focuses on predicting the Air Quality Index (AQI) by leveraging meteorological parameters. The dataset spans the years 2013 to 2016, offering a rich and diverse collection of atmospheric conditions and air quality data. The primary goal is to develop robust predictive models that can accurately forecast PM 2.5 levels based on various meteorological features.

## Dataset

### Temporal Coverage

The dataset covers four years, from 2013 to 2016, ensuring a broad temporal scope for understanding trends, patterns, and seasonal variations in meteorological and air quality data.

### Meteorological Parameters

1. **T (Temperature):** Represents the daily average temperature. Understanding temperature variations is crucial for assessing its impact on air quality.
2. **TM (Maximum Temperature):** Denotes the maximum temperature recorded on a given day. This parameter provides insights into extreme weather conditions.
3. **Tm (Minimum Temperature):** Signifies the minimum temperature recorded on a specific day. Monitoring minimum temperatures is essential for assessing nighttime cooling.
4. **SLP (Sea Level Pressure):** Reflects the atmospheric pressure at sea level. Changes in pressure can influence air circulation and, consequently, air quality.
5. **H (Humidity):** Depicts the daily average relative humidity. Humidity levels impact the dispersion and concentration of air pollutants.
6. **VV (Visibility):** Indicates the average visibility during the day. Low visibility can be indicative of high pollutant concentrations.
7. **V (Wind Speed):** Represents the average wind speed. Wind speed influences the dispersion of pollutants and can affect air quality.
8. **VM (Maximum Wind Speed):** Denotes the maximum wind speed recorded on a particular day. Understanding wind extremes is crucial for assessing pollutant dispersion.

### PM 2.5 (Particulate Matter 2.5)

The primary focus is on predicting PM 2.5 levels, a critical component of the Air Quality Index (AQI). PM 2.5 represents fine particulate matter, and accurate forecasting is essential for comprehensive air quality assessment. High levels of PM 2.5 are associated with adverse health effects.

### Data Cleaning

The dataset undergoes rigorous cleaning procedures to ensure data integrity. Missing values are addressed, outliers are handled, and rows with incomplete or invalid information are systematically removed. This meticulous process contributes to the reliability of the dataset.

### Data Source

Meteorological data is extracted from HTML files, providing a structured and reliable source. AQI data is obtained from CSV files, ensuring consistency and accuracy in air quality measurements.

## Models

The project employs a diverse set of regression and machine learning models to capture the complexity of the relationship between meteorological parameters and air quality:

1. **Linear Regression:** Provides a baseline model to understand linear relationships between features and the target variable.
2. **Lasso Regression:** Incorporates L1 regularization to encourage sparsity in the model, potentially highlighting the most influential features.
3. **Ridge Regression:** Utilizes L2 regularization to prevent overfitting, particularly beneficial when dealing with multicollinearity.
4. **Random Forest:** Harnesses the power of an ensemble of decision trees, offering robustness and the ability to capture complex relationships.
5. **XGBoost:** An optimized gradient boosting algorithm known for its efficiency and performance in predictive modeling.
6. **Artificial Neural Network (ANN):** Leverages deep learning to capture intricate patterns and relationships within the data.

## Data Processing

Before model development, the dataset undergoes preprocessing steps to ensure its suitability for training and evaluation. This involves handling missing data, normalizing features, and creating training/testing sets for robust model development.

## Model Evaluation

Various metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), are employed to assess the accuracy and performance of the predictive models. This thorough evaluation process helps identify the strengths and limitations of each model.

Feel free to contribute, raise issues, or provide feedback to enhance this project!
