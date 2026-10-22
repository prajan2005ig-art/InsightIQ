from insights import generate_insights
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

from data_analyzer import analyze_dataset

def upload_csv():
    file_path = filedialog.askopenfilename(
        title="Select a CSV dataset",
        filetypes=[("CSV files", "*.csv")]
    )

    if not file_path:
        return

    try:

        df = pd.read_csv(file_path)


        results = analyze_dataset(df)
        findings = generate_insights(df,results)


        output_text.delete("1.0", tk.END)


        output_text.insert(tk.END, "INSIGHTIQ - DATA ANALYSIS REPORT\n")
        output_text.insert(tk.END, "=" * 45 + "\n\n")

        output_text.insert(
            tk.END,
            f"File: {file_path.split('/')[-1].split(chr(92))[-1]}\n"
        )
        output_text.insert(tk.END, f"Rows: {results['rows']}\n")
        output_text.insert(tk.END, f"Columns: {results['columns']}\n")
        output_text.insert(
            tk.END,
            f"Duplicate rows: {results['duplicate_rows']}\n"
        )


        total_missing = results["missing_values"].sum()
        output_text.insert(
            tk.END,
            f"Total missing cells: {total_missing}\n\n"
        )


        output_text.insert(tk.END, "MISSING VALUES BY COLUMN\n")
        output_text.insert(tk.END, "-" * 35 + "\n")

        output_text.insert(
            tk.END,
            results["missing_values"].to_string() + "\n\n"
        )


        output_text.insert(tk.END, "COLUMN DATA TYPES\n")
        output_text.insert(tk.END, "-" * 35 + "\n")

        output_text.insert(
            tk.END,
            results["data_types"].to_string() + "\n\n"
        )


        output_text.insert(tk.END, "KEY FINDINGS\n")
        output_text.insert(tk.END, "-" * 35 + "\n")

        for finding in findings:
            output_text.insert(tk.END, f"- {finding}\n")

        output_text.insert(tk.END, "\n")

        output_text.insert(tk.END, "NUMERICAL SUMMARY\n")
        output_text.insert(tk.END, "-" * 35 + "\n")

        output_text.insert(
            tk.END,
            results["numerical_summary"].to_string() + "\n"
        )


        output_text.see("1.0")

    except Exception as error:
        messagebox.showerror(
            "Upload Error",
            f"Could not analyze the CSV:\n{error}"
        )


root = tk.Tk()
root.title("InsightIQ - Data Analyzer")
root.geometry("850x650")


title = tk.Label(
    root,
    text="InsightIQ",
    font=("Arial", 22, "bold")
)
title.pack(pady=12)

subtitle = tk.Label(
    root,
    text="Automated Dataset Analysis",
    font=("Arial", 11)
)
subtitle.pack(pady=3)

# CSV upload button
upload_button = tk.Button(
    root,
    text="Upload CSV Dataset",
    command=upload_csv,
    font=("Arial", 12),
    padx=15,
    pady=8
)
upload_button.pack(pady=10)


report_frame = tk.Frame(root)
report_frame.pack(fill="both", expand=True, padx=15, pady=10)

scrollbar = tk.Scrollbar(report_frame)
scrollbar.pack(side="right", fill="y")


output_text = tk.Text(
    report_frame,
    wrap="none",
    font=("Consolas", 10),
    yscrollcommand=scrollbar.set
)
output_text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=output_text.yview)


output_text.insert(
    tk.END,
    "Welcome to InsightIQ!\n\n"
    "Upload a CSV file to view its analysis report here."
)

# Start the application
root.mainloop()