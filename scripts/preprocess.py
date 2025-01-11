# Import necessary libraries
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
    """
    # Normalise column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Explicitly cast numeric columns before filling
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].astype(float).fillna(0)  # Fill numeric NaNs with 0

    # Fill non-numeric columns
    for col in df.select_dtypes(exclude=[np.number]).columns:
        df[col] = df[col].fillna("Unknown")  # Fill non-numeric NaNs with "Unknown"

    # Extract year from a date column
    if 'attackdate' in df.columns:
        df['year'] = pd.to_datetime(df['attackdate'], errors='coerce').dt.year
    else:
        print("Warning: 'attackdate' column is missing. 'year' column will not be created.")

    # Ensure 'ransomware' is properly processed
    if 'ransomware' in df.columns:
        df['ransomware'] = df['ransomware'].astype('category').cat.codes
    else:
        print("Warning: 'ransomware' column is missing.")

    # Extract IP addresses using regex (optional feature engineering example)
    if 'description' in df.columns:
        df['ip_address'] = df['description'].str.extract(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)')
    
    return df

def save_processed_data(df, output_path):
    """
    Save the cleaned dataset to a new CSV file.
    """
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # File paths
    input_file = "/repos/PFDA-project/data/cyber_data.csv"
    output_file = "/repos/PFDA-project/data/processed_data.csv"

    # Load, clean, and save the data
    print("Loading data...")
    raw_data = load_data(input_file)
    
    print("Cleaning data...")
    cleaned_data = clean_data(raw_data)
    
    print(f"Saving processed data to {output_file}...")
    save_processed_data(cleaned_data, output_file)
    
    print("Preprocessing complete!")
