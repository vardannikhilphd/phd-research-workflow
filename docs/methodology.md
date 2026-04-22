# Data Analysis Notes
---
## Purpose of the Dataset
The dataset is designed to study the relationship between environmental factors such as (`temperature` and `humidity`).  and student performance (scores).  
The objective is to identify patterns, trends, and correlations that may influence academic outcomes.


The goal is to:
- Practice data cleaning and preprocessing  
- Analyze relationships between variables  
- Generate meaningful visualizations  
- Demonstrate a structured Git-based development workflow  

---

## Handling Missing Values
- Missing values were intentionally included in `sample_data.csv` to simulate real-world data issues  
- Numeric columns (`experiment_score`, `temperature`, `humidity`) were handled using **mean imputation** in `clean_data.py`  
- The script automatically detects missing values and replaces them with the column mean  
- The cleaned dataset is saved as `data/cleaned_data.csv`  

---

## Why This Strategy Was Chosen
- Mean imputation is simple and effective for small datasets used in this exercise  
- It allows retention of all rows without discarding potentially useful data  
- It is easy to implement programmatically in Python  
- Suitable for a baseline approach before applying more advanced techniques  
- Alternative methods like **median imputation** or **model-based imputation** can be explored in future work  

---

## Visualisations Generated
Using `visualize_data.py`, the following plots were generated and saved in the `results/` folder:

- **Temperature vs Experiment Score Plot**  
  Shows how temperature variations relate to student performance  

- **Scores by Student Plot**  
  Compares experiment scores across different students  

- **Humidity Distribution Plot**  
  Displays the spread and frequency of humidity values  

- **Correlation Heatmap**  
  Highlights relationships between all numerical variables in the dataset  

---

## Limitations
- The dataset is synthetic and small (at least 10 rows), limiting real-world applicability  
- Mean imputation may distort data distribution, especially with extreme values  
- Assumes linear relationships in correlation analysis  
- Limited number of features (only temperature, humidity, and score)  
- Visualizations provide insights but do not establish causation  

---

## Workflow Context (Git Integration)
- Data creation and initial commit were done on the `main` branch  
- Data cleaning was implemented in the `feature-data-cleaning` branch  
- Visualization was implemented in the `feature-visualisation` branch  
- Each feature was developed, committed, and pushed separately to maintain modularity  
- This approach demonstrates proper use of branching in version control  

---