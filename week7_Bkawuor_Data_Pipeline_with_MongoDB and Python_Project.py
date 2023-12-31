# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xqv6D8PnyAV8T7KjOxFpvLnleR51kQRt

# Telecommunications Fraud Detection Using MongoDB and Python

## Problem Statement

Telecommunications companies need to detect fraudulent activities such as unauthorized use of premium services or fake billing. Building a data pipeline with MongoDB and Python could help identify suspicious activity by extracting data from billing systems, call logs, and other sources,
transforming the data to identify patterns or anomalies, and storing it in MongoDB for furtheranalysis.
"""

import pandas as pd
import pymongo
from pymongo import MongoClient
import logging
import gzip

# Extraction function
def extract_data():
    # Load call log data from CSV file
    call_logs = pd.read_csv('call_logs.csv')

    # Load billing data from CSV file
    billing_data = pd.read_csv('billing_data.csv')

    # Merge the two datasets based on common columns
    merged_data = pd.merge(call_logs, billing_data, on=['phone_number', 'call_date'])

    # Convert call duration to minutes for easier analysis
    merged_data['duration_minutes'] = merged_data['call_duration'] / 60

    # Use Python logging module to log errors and activities
    logger = logging.getLogger(__name__)
    logger.info("Data extraction completed.")

    return merged_data

# Transformation function
def transform_data(df):
    # Data cleaning and handling missing values
    transformed_data = df.dropna()

    # Group and aggregate the data
    df.describe()

    # Identify patterns in the data
    # ...

    # Use data compression techniques to optimize performance
    compressed_data = gzip.compress(transformed_data.to_json().encode())

    # Use Python logging module to log errors and activities
    logger = logging.getLogger(__name__)
    logger.info("Data transformation complete.")


# Loading function
def load_data(transformed_data):
    # Connect to MongoDB
    client = pymongo.MongoClient(host, port, ssl=True, ssl_cert_reqs='CERT_NONE')
    db = client[db_name]
    collection = db[collection_name]

    client = MongoClient("mongodb+srv://jkMongoProj:Galaxy123!@cluster0.0bkm2h2.mongodb.net/?retryWrites=true&w=majority")
    db = client.get_database('mongodbproj')
    collection = db.call_records

    # Create indexes on the collection
    # ...

    # Use bulk inserts to optimize performance
    operations = [pymongo.InsertOne(doc) for doc in documents]

    # Use the write concern option to ensure that data is written to disk
    collection.acknowledge_writes(w=1, j=True)

    # Use Python logging module to log errors and activities
    logger = logging.getLogger(__name__)
    logger.info("Data loading completed.")

# Example usage
if __name__ == '__main__':
    file_path = 'call_logs.csv'
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    load_data(transformed_data)