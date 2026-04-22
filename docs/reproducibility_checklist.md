# 📘 Project Execution Guide – PhD Research Workflow

---

## Input Files Required
- data/sample_data.csv  
Contains raw dataset with columns: student_id, experiment_score, temperature, humidity  
(Missing values included intentionally for cleaning practice)

---

## Scripts to be Executed

### Data Cleaning Script
src/clean_data.py  
- Reads raw dataset  
- Detects missing values  
- Fills missing numeric values using mean imputation  
- Saves output as data/cleaned_data.csv  

### Visualization Script
src/visualize_data.py  
- Reads cleaned dataset  
- Generates plots:
  - Temperature vs Score  
  - Humidity distribution  
  - Correlation heatmap  
- Saves outputs in results/ folder  

---

## Execution Order
1. Open project folder  
2. Ensure data/sample_data.csv exists  
3. Run:
   python src/clean_data.py  
4. Check creation of data/cleaned_data.csv  
5. Run:
   python src/visualize_data.py  
6. Check results/ folder for plots  

---

## Expected Output Files
- data/cleaned_data.csv  
- results/temperature_vs_score.png  
- results/humidity_distribution.png  
- results/correlation_heatmap.png  

---

## Software Dependencies
Install using:
pip install pandas numpy matplotlib seaborn  

Required libraries:
- pandas  
- numpy  
- matplotlib  
- seaborn  

---

## Limitations
- Small dataset reduces statistical reliability  
- Mean imputation may introduce bias  
- No categorical data handling  
- Correlation does not imply causation  
- No predictive modeling included  