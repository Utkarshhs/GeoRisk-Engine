# GeoRisk-Engine

An end-to-end spatio-temporal environmental risk and hazard forecasting pipeline.

## Overview
GeoRisk-Engine is a predictive machine learning pipeline designed to detect and forecast high-risk weather hazards. By processing rolling time-series meteorological data, the system engineers temporal features to predict environmental anomalies and assess spatial risk levels.

## Tech Stack
* **Ingestion:** Python (requests, Open-Meteo REST API)
* **Database:** MySQL
* **Data Engineering:** NumPy, Pandas
* **Modeling:** Scikit-learn, TensorFlow/Keras

## Pipeline Architecture
1. **Data Collection:** Automated extraction of historical and real-time weather metrics via the Open-Meteo REST API.
2. **Storage:** Relational data management using MySQL to organize structured time-series meteorological records.
3. **Preprocessing:** Data cleaning and temporal feature engineering using Pandas and NumPy to prepare rolling-window datasets.
4. **Risk Prediction:** Baseline model training using Scikit-learn, integrated with TensorFlow/Keras for complex temporal pattern recognition.

## Setup and Installation
1. Clone the repository.
2. Install the required Python dependencies: `pip install -r requirements.txt`
3. Configure your local MySQL server and update the database credentials in `config.py`.
4. Run `ingest.py` to pull initial training data from the Open-Meteo API.
5. Execute `train.py` to fit the models.
