# PFDA-project **Cybercrime Analysis**

Lecture by Andrew Beatty at [ATU](https://www.atu.ie/)

***

## Overview

This project explores global cybercrime trends using the `cyber_data.csv` dataset, which contains detailed records of cyber-attacks spanning 14 months (October 2022 to December 2023) across 225 countries. The dataset includes 77,623 rows and 19 fields, capturing information such as attack vectors, target sectors, and geographical locations.

The project provides an in-depth analysis of cybercrime trends, highlights vulnerabilities across various sectors, and uses machine learning techniques to predict high-risk scenarios. Data visualizations, including pie charts, bar plots, and heatmaps, enhance the analysis for actionable insights.

## Project Objectives

1. **Temporal Analysis**:
   - Examine cyber-attack trends over time.
   - Identify peak periods and annual trends.
2. **Geographical Analysis**:
   - Visualize the distribution of cyber-attacks across regions.
   - Highlight top-affected countries.
3. **Attack Method Analysis**:
   - Analyze the most common attack vectors used by cybercriminals.
4. **Sectoral Vulnerability**:
   - Identify industries most frequently targeted by cyber-attacks.
5. **Predictive Analytics**:
   - Leverage machine learning to forecast risks and identify high-risk periods or sectors.

## Tools and Libraries

### Data Handling
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Regular Expressions**: Data cleaning and feature extraction.

### Data Visualization
- **Matplotlib**: Static and customizable visualizations.
- **Seaborn**: Statistical and advanced plotting.

### Machine Learning
- **Scikit-learn**: Data preprocessing and predictive modeling.
- **TensorFlow/Keras**: Neural network design and training.

## Project Structure

```plaintext
cybercrime-analysis/
│
├── data/
│   ├── cyber_data.csv          # Raw dataset
│   ├── processed_data.csv      # Cleaned dataset
│
├── notebooks/
│   ├── analysis.ipynb          # EDA and machine learning
│   ├── cybercrime-visual-analysis.ipynb  # Advanced visualizations
│
├── scripts/
│   ├── preprocess.py           # Data cleaning and preprocessing script
│
├── .gitignore
├── README.md                   # Project documentation
```

## Installation

### Prerequisites

Ensure Python 3.8+ is installed.

### Required Libraries

Install the necessary libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

### Dataset

Download the `cyber_data.csv` dataset and place it in the `data/` directory.

## Usage

### Data Preprocessing

Run the preprocessing script to clean and prepare the data:

```bash
python scripts/preprocess.py
```

### Data Exploration

Open the Jupyter notebooks to explore and visualize the data:

- For general analysis and machine learning:
  ```bash
  jupyter notebook notebooks/analysis.ipynb
  ```

- For advanced visualizations:
  ```bash
  jupyter notebook notebooks/cybercrime-visual-analysis.ipynb
  ```

## Documentation and Insights

### Preprocessing Script (`preprocess.py`)

The preprocessing script handles data cleaning and preparation:
- Normalizes column names.
- Handles missing values by filling numeric fields with 0 and categorical fields with "Unknown."
- Extracts the year from the `attackdate` column.
- Encodes categorical fields like `ransomware` for machine learning.

### Notebooks

1. **`analysis.ipynb`**:
   - Conducts exploratory data analysis.
   - Implements machine learning models to predict high-risk scenarios.

2. **`cybercrime-visual-analysis.ipynb`**:
   - Creates advanced visualizations:
     - Pie charts: Attack methods and geographical distribution.
     - Bar charts: Temporal trends and attack frequencies.
     - Heatmaps: Temporal attack distribution by month and year.

## Sample Visualizations

### Temporal Analysis
- **Bar Chart**: Cyber-attacks by year.
- **Heatmap**: Distribution of attacks by month and year.

### Geographical Distribution
- **Pie Chart**: Top affected countries.
- **Bar Chart**: Number of attacks per country.

### Attack Methods
- **Pie Chart**: Distribution of attack vectors.
- **Bar Chart**: Frequency of attack methods.

### Predictive Insights
- **Pie Chart**: Predicted risk levels.
- **Bar Chart**: Breakdown of predicted risks.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request to suggest changes or report bugs.

## Sources and References

- **Dataset**: [DrSufi/CyberData](https://github.com/DrSufi/CyberData)
- **Documentation**:
  - [Pandas](https://pandas.pydata.org/)
  - [Matplotlib](https://matplotlib.org/)
  - [TensorFlow](https://tensorflow.org/)
- **Tools**: Jupyter Notebook, Anaconda, Python.

## License

This project is licensed under the MIT License.

---

## Acknowledgments

***
- Dataset: [DrSufi/CyberData](https://github.com/DrSufi/CyberData)
- Libraries: [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [TensorFlow](https://tensorflow.org/)

***

Additional Resources:

For further guidance on conducting data analysis with Python, consider the following resources:

Data Science for Crime Analysis with Python: This book provides a comprehensive introduction to using Python for crime data analysis, 
including practical examples and code snippets. 
[ANDREW P. WHEELER](https://andrewpwheeler.com/wp-content/uploads/2024/03/ds_pythoncrimeanalysis_earlyrelease-1.pdf?utm_source=chatgpt.com)

Crime Data Exploration with Python3, Numpy, and Pandas: This blog series offers tutorials on analyzing crime data using Python's 
data analysis libraries. [RICHARD KELLER BLOG](https://blog.richardkeller.net/crime-data-exploration-with-python3-numpy-and-pandas-part-1/?utm_source=chatgpt.com)

By leveraging the CyberData dataset and these resources, it will be possible to develop a comprehensive analysis that sheds light on various facets of cybercrime, 
enhancing the understanding and contributing valuable insights to the field.
