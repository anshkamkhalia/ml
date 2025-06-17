import numpy as np
from loader import DataLoader
import pandas as pd

class StatisticalAnalysis:

    def __init__(self):
        loader = DataLoader()
        loader.load_data("sample.csv")
        self.df = loader.df 

    def get_column_stats(self, column):
        if column not in self.df.columns:
            return f"Column '{column}' not found."

        if not np.issubdtype(self.df[column].dtype, np.number):
            return f"Column '{column}' is not numeric."

        col = self.df[column].dropna()

        return {
            "mean": col.mean(),
            "median": col.median(),
            "mode": col.mode().tolist(),
            "std_dev": col.std(),
            "min": col.min(),
            "max": col.max(),
            "percentiles": col.quantile([0.25, 0.5, 0.75]).to_dict(),
            "skewness": col.skew(),
            "kurtosis": col.kurt()
        }

    
    def get_distribution(self, column):
        """
        Returns a value count distribution for categorical or discrete columns.
        """

        if column not in self.df.columns:
            return f"Column: {column} not found or not numeric."

        col = self.df[column].dropna()
        return col.value_counts()

    def detect_outliers_iqr(self, column):
        """
        Detects outliers in a numerical column using the IQR method.
        Returns a DataFrame with only the outlier rows.
        """

        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in the dataset.")

        if not np.issubdtype(self.df[column].dtype, np.number):
            raise TypeError(f"Column '{column}' must be numeric.")

        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
        return outliers

    def column_summary(self, column):
        """
        Runs all the above stats for given numeric column, and stores them in a dict or DataFrame.
        """

        return (
            {
                "Column Stats":self.get_column_stats(column),
                "Distribution":self.get_distribution(column),
                "Outliers":self.detect_outliers_iqr(column),
            }
        )
    
    def feature_variability(self):
        """
        Measures standard deviation or coefficient of variation for each numeric column.
        """

        return_dict = {}

        for column in self.df.select_dtypes(include=np.number).columns:
            return_dict[column] = self.df[column].std()

        return return_dict

    def correlation_with_target(self, target):
        if target not in self.df.columns:
            return f"Target column '{target}' not found."

        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if target not in numeric_cols:
            return f"Target column '{target}' is not numeric, cannot calculate correlations."

        numeric_cols.remove(target)

        return_dict = {}
        for column in numeric_cols:
            corr_value = self.df[column].corr(self.df[target])
            return_dict[column] = corr_value

        return return_dict
