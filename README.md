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

The dataset `cyber_data.csv` is hosted on GitHub. It includes:
- **Attack Categories:** Descriptions of cyber-attack types.
- **Geographical Data:** Locations of incidents.
- **Timestamps:** Dates and times of attacks.
- **Target Sectors:** Industries or organizations affected.

### Accessing the Dataset

- **Repository:** [DrSufi/CyberData](https://github.com/DrSufi/CyberData)
- **Dataset File:** [cyber_data.csv](https://github.com/DrSufi/CyberData/blob/main/cyber_data.csv)


## Installation

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