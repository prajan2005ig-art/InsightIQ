
# InsightIQ — Automated Dataset Analysis and Insight Generation

## Overview
InsightIQ is a Python-based desktop application that automates the initial analysis of CSV datasets. It helps users understand dataset structure, identify data quality issues, review statistical summaries, and generate automated key findings through a simple Tkinter interface.

## Features
- Upload CSV datasets through a desktop file picker.
- Display the number of rows and columns.
- Detect missing values in each column and across the dataset.
- Identify duplicate rows.
- Inspect column data types.
- Generate numerical summary statistics.
- Generate rule-based key findings from uploaded data.
- Display analysis results within the application window.

## Technologies Used
- Python
- Pandas
- Tkinter

## Project Structure
```text
InsightIQ/
├── mainproj.py
├── data_analyzer.py
├── insights.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository
```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder
```bash
cd InsightIQ
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## How to Run
Start the application using:

```bash
python mainproj.py
```

Click **Upload CSV Dataset**, select a CSV file, and view the analysis report in the application window.

## How It Works
1. Tkinter allows the user to select a CSV file.
2. Pandas loads the selected dataset into a DataFrame.
3. The data analyzer calculates dataset dimensions, missing values, duplicate rows, column types, and numerical statistics.
4. The insights module generates rule-based findings from the analysis results.
5. The application displays the results in the Tkinter interface.

## Limitations
- Key findings are generated using predefined Python rules, not a generative AI model.
- The usefulness of the findings depends on the uploaded dataset's structure and contents.
- The application analyses CSV files but does not automatically clean or modify the original dataset.

## Future Improvements
- Add data visualization for different dataset types.
- Improve date and identifier column detection.
- Add more robust error handling and automated tests.
- Explore AI-assisted explanations of analytical results.

## Author
Prajan

## Purpose
Built as a learning project to practise Python programming, data analysis with Pandas, desktop GUI development, and exploratory data analysis.