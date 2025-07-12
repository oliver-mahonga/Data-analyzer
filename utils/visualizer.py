import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
from rich import print

def generate_all_plots(df, output_dir='graphs'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, color='skyblue')
        plt.title(f"Histogram of {col}")
        plt.savefig(f"{output_dir}/{col}_hist.png")
        plt.close()

    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=df[col], color='lightcoral')
        plt.title(f"Boxplot of {col}")
        plt.savefig(f"{output_dir}/{col}_box.png")
        plt.close()

    if len(numeric_cols) >= 2:
        plt.figure(figsize=(10, 8))
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.savefig(f"{output_dir}/correlation_heatmap.png")
        plt.close()

    if len(numeric_cols) <= 5:
        sns.pairplot(df[numeric_cols])
        plt.savefig(f"{output_dir}/pairplot.png")
        plt.close()
    print("All your plots have been saved in the graphs folder please open it and check your plots")
def main ():
    generate_all_plots()