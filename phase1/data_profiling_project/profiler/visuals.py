import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loader import DataLoader
import numpy as np

class Visualizer:

    def __init__(self):
        loader = DataLoader()
        loader.load_data("sample.csv")
        self.df = loader.df
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns

        plt.rcParams["figure.figsize"] = (12, 8)
        sns.set_style("darkgrid")

    def plot_histogram(self, column):
        """Shows a histogram of the user-given column"""
        if column not in self.numeric_cols:
            print("Column must be numeric")
            return

        sns.histplot(self.df[column].dropna(), kde=True, bins=30)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

    def plot_boxplot(self, column):
        """Shows a boxplot of the user-given column"""
        if column not in self.numeric_cols:
            print("Column must be numeric")
            return

        sns.boxplot(y=self.df[column].dropna())
        plt.title(f"Boxplot of {column}")
        plt.ylabel(column)
        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self):
        """Shows a correlation matrix heatmap"""
        corr = self.df[self.numeric_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Matrix Heatmap")
        plt.tight_layout()
        plt.show()

    def show_pairplot(self, hue=None):
        """Shows a pairplot of numeric features (optional hue column)"""
        if hue and hue not in self.df.columns:
            print(f"Hue column '{hue}' not found.")
            return

        sns.pairplot(self.df[self.numeric_cols.union([hue])] if hue else self.df[self.numeric_cols],
                     hue=hue, diag_kind="kde")

        plt.suptitle("Pairplot of Numerical Features", y=1.02)
        plt.tight_layout()
        plt.show()

    def show_distribution(self, column):
        """Shows a distribution plot of the user-given column"""
        if column not in self.numeric_cols:
            print("Column must be numeric")
            return

        sns.kdeplot(self.df[column].dropna(), shade=True)
        plt.title(f"Distribution Plot of {column}")
        plt.xlabel(column)
        plt.tight_layout()
        plt.show()