# 📊 PhD Research Workflow

## Project Title
- PhD Research Workflow: Data Cleaning, Analysis, and Visualization

## Project Structure
- data/
  - sample_data.csv
  - cleaned_data.csv
- docs/
  - analysis_notes.md
- references/
  - paper1.md
  - paper2.md
  - paper3.md
- results/
  - plot1_temperature_vs_score.png
  - plot2_scores_by_student.png
  - plot3_humidity_distribution.png
  - plot4_correlation_heatmap.png
- src/
  - clean_data.py
  - visualize_data.py
- .gitignore
- README.md

## Files Used
- data/sample_data.csv → raw dataset with missing values  
- data/cleaned_data.csv → cleaned dataset after preprocessing  
- docs/analysis_notes.md → analysis observations and notes  
- references/ → research papers used for study  
- results/ → generated plots and visualizations  
- src/clean_data.py → script for handling missing values and cleaning data  
- src/visualize_data.py → script for generating visualizations  

## How to Run the Project
- git clone https://github.com/vardannikhilphd/phd-research-workflow  
- cd PHD-RESEARCH-WORKFLOW  
- pip install pandas matplotlib seaborn  
- python src/clean_data.py  
- python src/visualize_data.py  

## Expected Outputs
- data/cleaned_data.csv  
- results/plot1_temperature_vs_score.png  
- results/plot2_scores_by_student.png  
- results/plot3_humidity_distribution.png  
- results/plot4_correlation_heatmap.png  

## Assumptions
- Missing values handled using mean imputation  
- Dataset is small and used for experimentation  
- Relationships assumed to be linear for analysis  

## Limitations
- Small dataset reduces generalization  
- Mean imputation may introduce bias  
- No machine learning or predictive modeling included  
- Correlation does not imply causation  