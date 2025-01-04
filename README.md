# PFDA-project **Cybercrime Analysis**

Lecture by Andrew Beatty at [ATU](https://www.atu.ie/)


***

## Overview

***

This project focuses on analyzing global cybercrime trends using the `cyber_data.csv` dataset. The dataset provides historical information on cyber-attacks spanning 14 months (October 2022 to December 2023) across 225 countries. It contains 77,623 rows and 18 fields, categorizing incidents by attack vector, target sector, and geography.

Using advanced data analysis and visualization techniques, this project explores patterns, trends, and insights to understand the global impact of cybercrime. Additionally, machine learning will be leveraged for predictive analytics.


## Project Objectives

***

- **Temporal Analysis:** Understand how cyber-attacks vary over time.
- **Geographical Analysis:** Visualize the distribution of cyber-attacks across countries and regions.
- **Attack Vector Analysis:** Identify the most common methods used by cybercriminals.
- **Target Sector Analysis:** Determine which industries are most frequently targeted.
- **Predictive Analytics:** Use machine learning to forecast trends and identify high-risk scenarios.

## Libraries

***

The following libraries will be used:

### Data Handling

- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical computations.
- **Regular Expressions:** To clean and preprocess data.

### Data Visualization

- **Matplotlib:** For creating static, publication-quality plots.
- **Seaborn:** For generating detailed statistical visualizations.

### Machine Learning

- **Scikit-learn:** For data preprocessing and predictive modeling.
- **TensorFlow:** For building and training machine learning models.

## Dataset

***

The dataset `cyber_data.csv` is hosted on GitHub. It includes:
- **Attack Categories:** Descriptions of cyber-attack types.
- **Geographical Data:** Locations of incidents.
- **Timestamps:** Dates and times of attacks.
- **Target Sectors:** Industries or organizations affected.

### Accessing the Dataset

- **Repository:** [DrSufi/CyberData](https://github.com/DrSufi/CyberData)
- **Dataset File:** [cyber_data.csv](https://github.com/DrSufi/CyberData/blob/main/cyber_data.csv)


## Installation

***

### Prerequisites

Ensure Python 3.8+ is installed on your machine.

### Required Libraries

Install the required libraries using the following command:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

### Clone the Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/your-username/cybercrime-analysis.git
cd cybercrime-analysis
```

### Dataset Download

Download the `cyber_data.csv` file and place it in the `data/` directory within the project folder.

## Project Structure

***

```plaintext
cybercrime-analysis/
|┃ └── data/
|┃     └── cyber_data.csv
|┃ └── notebooks/
|┃     └── analysis.ipynb
|┃ └── scripts/
|┃     └── preprocess.py
|┃ └── README.md
```

## Usage

***

### Data Exploration

Open the Jupyter notebook:

```bash
jupyter notebook notebooks/analysis.ipynb
```

Explore the dataset, visualize trends, and generate insights.

### Scripts

Run the preprocessing script to clean the data:

```bash
python scripts/preprocess.py
```

## Analysis Techniques

***

### Data Cleaning

- Remove duplicate entries.
- Handle missing values using imputation techniques.
- Use regular expressions to standardize text data.

### Visualization

- **Matplotlib & Seaborn:** Create time series plots, heatmaps, and geographical charts.

### Machine Learning

- Train a predictive model using TensorFlow to identify high-risk attack periods and locations.

## Sample Code

***

### Loading and Exploring Data


```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/cyber_data.csv')

# Display first few rows
print(df.head())

# Summary statistics
print(df.describe())
```

### Plotting Trends

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Temporal analysis
sns.lineplot(data=df, x='timestamp', y='attack_count', hue='attack_type')
plt.title('Trends in Cyber Attacks Over Time')
plt.show()
```

### Predictive Modeling


```python
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Split data
X = df[['feature1', 'feature2']] # Replace with actual features
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile and train
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

## Contribution

***
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Licence

***
This project is licensed under the MIT License.

## Acknowledgments

***
- Dataset: [DrSufi/CyberData](https://github.com/DrSufi/CyberData)
- Libraries: [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [TensorFlow](https://tensorflow.org/)

---