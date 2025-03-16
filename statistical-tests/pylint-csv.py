import os
import pandas as pd

# Define the input Excel file path
input_file = "/home/saima/projects/NonFunc-AWQ/mcEval-py/deepseekcoder-33B-instruct-hf/pylint/pylint_analysis.xlsx"

# Define the output directory and CSV file path
output_directory = "/home/saima/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8"
output_csv_path = os.path.join(output_directory, "r-pylint_33b-fp.csv")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the Excel file
df = pd.read_excel(input_file)

# Extract relevant columns
df_filtered = df[["Task ID", "Error", "Warning", "Convention", "Refactor"]].copy()

# Function to count the number of error codes in each column
def count_errors(column):
    return column.fillna("").apply(lambda x: len(x.split("\n")) if x.strip() else 0)

# Apply the counting function to each category
df_filtered["Error"] = count_errors(df_filtered["Error"])
df_filtered["Warning"] = count_errors(df_filtered["Warning"])
df_filtered["Convention"] = count_errors(df_filtered["Convention"])
df_filtered["Refactor"] = count_errors(df_filtered["Refactor"])

# Extract the numeric part of the task ID (e.g., taskid-123 from taskid-123_some_text)
#df_filtered["Task ID Numeric"] = df_filtered["Task ID"].str.extract(r'taskid-(\d+)').astype(int)
df_filtered["Task ID Numeric"] = df_filtered["Task ID"].str.extract(r'Python-(\d+)').astype(int)


# Sort by extracted numeric task ID
df_filtered = df_filtered.sort_values(by=["Task ID Numeric"])

# Drop the temporary sorting column
df_filtered = df_filtered.drop(columns=["Task ID Numeric"])

# Save to CSV
df_filtered.to_csv(output_csv_path, index=False)

print(f"CSV file successfully saved at: {output_csv_path}")
