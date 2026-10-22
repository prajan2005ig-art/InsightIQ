
import pandas as pd

def generate_insights(df, results):
    insights = []

    # 1. Dataset overview
    rows, columns = df.shape
    insights.append(
        f"The dataset contains {rows:,} rows "
        f"and {columns} columns."
    )

    # 2. Missing values
    missing = results["missing_values"]
    total_missing = int(missing.sum())

    if total_missing > 0:
        insights.append(
            f"Found {total_missing:,} missing cells."
        )

        column = missing.idxmax()
        count = int(missing.max())

        insights.append(
            f"'{column}' has the most missing values "
            f"({count:,})."
        )
    else:
        insights.append("No missing values were detected.")

    # 3. Duplicate rows
    duplicates = int(results["duplicate_rows"])

    if duplicates > 0:
        insights.append(
            f"Found {duplicates:,} duplicate rows."
        )
    else:
        insights.append("No duplicate rows were detected.")

    # 4. Identify column types
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    text_columns = df.select_dtypes(
        include=["object", "category", "string"]
    ).columns

    insights.append(
        f"Numeric columns: {len(numeric_columns)}; "
        f"text/category columns: {len(text_columns)}."
    )

    # 5. Summarise numerical columns automatically
    if len(numeric_columns) > 0:
        for column in numeric_columns[:3]:
            values = pd.to_numeric(
                df[column], errors="coerce"
            ).dropna()

            if len(values) == 0:
                continue

            insights.append(
                f"'{column}': average = {values.mean():,.2f}, "
                f"minimum = {values.min():,.2f}, "
                f"maximum = {values.max():,.2f}."
            )
    else:
        insights.append(
            "No numeric columns are available "
            "for numerical summaries."
        )

    # 6. Summarise categorical columns automatically
    if len(text_columns) > 0:
        for column in text_columns[:3]:
            values = df[column].dropna()

            if values.empty:
                continue

            common_value = values.astype(str).mode()

            if not common_value.empty:
                insights.append(
                    f"Most common value in '{column}': "
                    f"{common_value.iloc[0]}."
                )

    return insights
