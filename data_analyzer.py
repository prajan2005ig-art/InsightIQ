import pandas as pd

def analyze_dataset(df):

    rows, columns = df.shape

    missing_values = df.isnull().sum()

    duplicate_rows = df.duplicated().sum()

    data_types = df.dtypes

    numerical_summary = df.describe()

    print("\nTotal missing cells:", df.isnull().sum().sum())

    print("\n========== INSIGHTIQ DATA ANALYSIS ==========")

    print(f"\nNumber of rows: {rows}")
    print(f"Number of columns: {columns}")

    print("\nMissing values in each column:")
    print(missing_values)

    print(f"\nNumber of duplicate rows: {duplicate_rows}")

    print("\nColumn data types:")
    print(data_types)

    print("\nNumerical summary:")
    print(numerical_summary)

    return {
        "rows": rows,
        "columns": columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "data_types": data_types,
        "numerical_summary": numerical_summary
    }

