import pandas as pd

class DataLoader:

    def __init__(self):

        self.missing_values = False
        self.column_list = {}

    def load_data(self, name):
        """Loads the dataset from the datasets folder and adds to the dictionary containing all of the columns and their datatypes"""

        try:
            if not name.endswith(".csv"):
                name += ".csv"
            path = f"C:\\Users\\Ansh\\Downloads\\DEVELOPMENT\\machine_learning\\phase1\\data_profiling_project\\profiler\\datasets\\{name}"
            self.df = pd.read_csv(path)

            self.column_list.clear()

            for column in self.df.columns:
                non_null = self.df[column].dropna()
                self.column_list[column] = type(non_null.iloc[0]) if not non_null.empty else None

        except Exception as e:
            print(f"Dataset not found: {e}")
    
    def check_missing_values(self):
        """
        Checks if the dataframe contains any null values.
        Returns True if yes, else False.
        """

        self.missing_values_series = self.df.isnull().any()
        self.missing_values = self.missing_values_series.any()
        return self.missing_values


    def display_columns(self):
        """Displays the columns names and respective datatypes in a clean manner"""

        for column in self.column_list:
            unique_values = self.df[column].dropna().unique()
            print(f"{column}: {self.column_list[column]} -> {unique_values if len(unique_values) <= 10 else len(unique_values)} unique values\n")
    
    def get_shape(self):
        """Returns the shape of the dataframe"""

        return self.df.shape
    
    def get_missing_values(self):
        """Returns a dictionary of missing value counts"""

        return self.df.isnull().sum().to_dict()
    
    def get_basic_stats(self):
        """Returns basic stats using the describe() function"""

        return self.df.describe().T.to_dict()
    
    def get_correlation_matrix(self):
        """Returns a basic correlation matrix"""

        return self.df.select_dtypes(include='number').corr()
    
    def preview_data(self, rows=5):
        """Shows the first 5 rows of the data"""

        return self.df.head(rows)
