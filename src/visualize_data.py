import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Read the cleaned data
df = pd.read_csv('data/cleaned_data.csv')

print("="*60)
print("DATA LOADED SUCCESSFULLY")
print("="*60)
print(df)
print("\nData Shape:", df.shape)
print("\nData Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 5)

# ==================== PLOT 1: Scatter Plot ====================
print("\n" + "="*60)
print("GENERATING PLOT 1: Scatter Plot (Temperature vs Experiment Score)")
print("="*60)

plt.figure(figsize=(10, 6))
plt.scatter(df['temperature'], df['experiment_score'], 
           color='#2E86AB', s=100, alpha=0.7, edgecolors='black', linewidth=1.5)
plt.xlabel('Temperature (°C)', fontsize=12, fontweight='bold')
plt.ylabel('Experiment Score', fontsize=12, fontweight='bold')
plt.title('Temperature vs Experiment Score', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['temperature'], df['experiment_score'], 1)
p = np.poly1d(z)
plt.plot(df['temperature'].sort_values(), p(df['temperature'].sort_values()), 
        "r--", alpha=0.8, linewidth=2, label='Trend Line')
plt.legend()

plt.tight_layout()
plt.savefig('results/plot1_temperature_vs_score.png', dpi=300, bbox_inches='tight')
print("✓ Plot 1 saved: results/plot1_temperature_vs_score.png")
plt.close()

# ==================== PLOT 2: Bar Plot ====================
print("\n" + "="*60)
print("GENERATING PLOT 2: Bar Plot (Experiment Scores by Student)")
print("="*60)

plt.figure(figsize=(14, 6))
colors = ['#A23B72' if score < df['experiment_score'].mean() else '#F18F01' 
          for score in df['experiment_score']]
bars = plt.bar(df['student_id'], df['experiment_score'], color=colors, 
              edgecolor='black', linewidth=1.2, alpha=0.8)

# Add mean line
plt.axhline(y=df['experiment_score'].mean(), color='red', linestyle='--', 
           linewidth=2, label=f'Mean: {df["experiment_score"].mean():.2f}')

plt.xlabel('Student ID', fontsize=12, fontweight='bold')
plt.ylabel('Experiment Score', fontsize=12, fontweight='bold')
plt.title('Experiment Scores by Student', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('results/plot2_scores_by_student.png', dpi=300, bbox_inches='tight')
print("✓ Plot 2 saved: results/plot2_scores_by_student.png")
plt.close()

# ==================== PLOT 3: Histogram ====================
print("\n" + "="*60)
print("GENERATING PLOT 3: Histogram (Distribution of Humidity)")
print("="*60)

plt.figure(figsize=(10, 6))
plt.hist(df['humidity'], bins=8, color='#06A77D', edgecolor='black', 
        alpha=0.7, linewidth=1.5)
plt.xlabel('Humidity (%)', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Distribution of Humidity', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# Add mean and median lines
plt.axvline(df['humidity'].mean(), color='red', linestyle='--', 
           linewidth=2, label=f'Mean: {df["humidity"].mean():.2f}')
plt.axvline(df['humidity'].median(), color='blue', linestyle='--', 
           linewidth=2, label=f'Median: {df["humidity"].median():.2f}')
plt.legend()

plt.tight_layout()
plt.savefig('results/plot3_humidity_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Plot 3 saved: results/plot3_humidity_distribution.png")
plt.close()

# ==================== PLOT 4: Heatmap ====================
print("\n" + "="*60)
print("GENERATING PLOT 4: Heatmap (Correlation Matrix)")
print("="*60)

plt.figure(figsize=(8, 6))
numeric_df = df[['experiment_score', 'temperature', 'humidity']]
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
           center=0, square=True, linewidths=2, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Numeric Variables', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('results/plot4_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Plot 4 saved: results/plot4_correlation_heatmap.png")
plt.close()

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"✓ All plots generated successfully!")
print(f"✓ Total plots created: 4")
print(f"✓ Saved location: results/")
print(f"✓ Data shape: {df.shape}")
print(f"✓ Experiment Score - Mean: {df['experiment_score'].mean():.2f}, Std: {df['experiment_score'].std():.2f}")
print(f"✓ Temperature - Mean: {df['temperature'].mean():.2f}, Std: {df['temperature'].std():.2f}")
print(f"✓ Humidity - Mean: {df['humidity'].mean():.2f}, Std: {df['humidity'].std():.2f}")
print("="*60)