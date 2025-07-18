from loader import DataLoader
from stats import StatisticalAnalysis
from visuals import Visualizer

class Report:

    def __init__(self):
        self.loader = DataLoader()
        self.loader.load_data("sample.csv")  
        self.stats = StatisticalAnalysis()
        self.visuals = Visualizer()
        self.df = self.loader.df 
    
    def summary(self):
        print(f"Dataset shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}\n")

        for column in self.df.columns:
            print(f"--- Summary for column: {column} ---\n")

            col_stats = self.stats.get_column_stats(column)
            print("Basic Stats:")
            print(col_stats if isinstance(col_stats, dict) else f"Skipped: {col_stats}")
            print()
            dist = self.stats.get_distribution(column)
            print("Distribution (value counts):")
            print(dist.to_dict() if hasattr(dist, 'to_dict') else dist)
            print()

            try:
                outliers = self.stats.detect_outliers_iqr(column)
                print(f"Outliers detected (rows): {len(outliers)}")
                if len(outliers) > 0:
                    print(outliers[[column]].to_dict(orient='records'))
            except Exception as e:
                print(f"Outlier detection skipped: {e}")
            print("\n" + "-"*50 + "\n")

        print("Feature Variability (std dev per numeric column):")
        print(self.stats.feature_variability())
        print()

        target_col = "AnnualIncome"  
        if target_col in self.df.columns:
            print(f"Correlation with target column '{target_col}':")
            print(self.stats.correlation_with_target(target_col))
        else:
            print(f"Target column '{target_col}' not found for correlation.")
        print()

        print("Plotting correlation matrix heatmap...")
        self.visuals.plot_correlation_matrix()

        print("Showing pairplot...")
        hue_col = "Gender" if "Gender" in self.df.columns else None
        self.visuals.show_pairplot(hue=hue_col)

        print("Summary complete.")
