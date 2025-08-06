import os
import glob
import pandas as pd

def merge_csv_files(input_folder, output_file):
    # Get all CSV files from the folder
    all_csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

    if not all_csv_files:
        print("No CSV files found in the folder!")
        return

    # Read and merge all CSV files
    dataframes = []
    for file in all_csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    # Concatenate all DataFrames and remove duplicate headers automatically
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged CSV
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved as: {output_file}")

if __name__ == "__main__":
    input_folder = "/Users/adityaanand/Desktop/csv/"  # Change to your folder path
    output_file = "merged.csv"
    merge_csv_files(input_folder, output_file)