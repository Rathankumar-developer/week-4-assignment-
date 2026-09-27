"""
Week 4 - Capstone Project (Option 1): Employee Data Analysis Project

Tasks:
- Load CSV using Pandas
- Calculate average salary, department count
- Filter employees above a salary threshold
- Export results to a new CSV

Dataset: employees.csv (sample data, same shape as a typical Kaggle
employee dataset: EmployeeID, Name, Department, Salary)
"""

import pandas as pd

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "employees_above_threshold.csv"
SALARY_THRESHOLD = 60000


def load_data(path):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} employee records from '{path}'.\n")
    return df


def average_salary(df):
    avg = df["Salary"].mean()
    print(f"Average salary (all employees): {avg:,.2f}")
    return avg


def department_counts(df):
    counts = df["Department"].value_counts()
    print("\nEmployee count by department:")
    print(counts.to_string())
    return counts


def filter_above_threshold(df, threshold):
    filtered = df[df["Salary"] > threshold].sort_values("Salary", ascending=False)
    print(f"\nEmployees earning above {threshold:,}: {len(filtered)}")
    print(filtered.to_string(index=False))
    return filtered


def export_results(df, path):
    df.to_csv(path, index=False)
    print(f"\nExported filtered results to '{path}'.")


def main():
    df = load_data(INPUT_FILE)
    average_salary(df)
    department_counts(df)
    filtered = filter_above_threshold(df, SALARY_THRESHOLD)
    export_results(filtered, OUTPUT_FILE)


if __name__ == "__main__":
    main()
