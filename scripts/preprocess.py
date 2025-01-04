# This script handles data cleaning and preparation.
import pandas as pd
import numpy as np
import re

def load_data(file_path):
    """
    Load the raw cybercrime dataset.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean and preprocess the dataset.
    - Handle missing values.
    - Normalize columns.
    - Extract features.
    """
    # Handle missing values
    df.fillna("Unknown", inplace=True)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Extract year from a date column (example)
    if 'date' in df.columns:
        df['year'] = pd.to_datetime(df['date'], errors='coerce').dt.year

    # Example: Extract IP addresses using regex
    if 'description' in df.columns:
        df['ip_address'] = df['description'].str.extract(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)')

    return df

def save_processed_data(df, output_path):
    """
    Save the cleaned dataset to a new CSV file.
    """
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "data/cyber_data.csv"
    output_file = "data/processed_data.csv"

    # Load, clean, and save the data
    print("Loading data...")
    raw_data = load_data(input_file)
    print("Cleaning data...")
    cleaned_data = clean_data(raw_data)
    print(f"Saving processed data to {output_file}...")
    save_processed_data(cleaned_data, output_file)
    print("Preprocessing complete!")

