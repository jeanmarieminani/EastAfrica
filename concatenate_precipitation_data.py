import pandas as pd
import glob
import os

def concatenate_precipitation_data(input_folder, output_file):
    # Find all CSV files for precipitation data
    precipitation_files = glob.glob(os.path.join(input_folder, "region_*_PRECTOTCORR_SUM_1981_2022.csv"))

    # Initialize an empty list to store data
    data_frames = []

    # Process each file
    for file in precipitation_files:
        print(f"Processing {file}...")
        try:
            # Read the file line by line to find the correct header
            with open(file, "r") as f:
                lines = f.readlines()

            # Find the line where the actual data begins
            start_row = 0
            for i, line in enumerate(lines):
                if line.startswith("PARAMETER,YEAR"):
                    start_row = i
                    break

            # Read the CSV starting from the correct row
            df = pd.read_csv(file, skiprows=start_row)

            # Ensure the required columns exist
            required_columns = ["YEAR", "LAT", "LON", "JAN", "FEB", "MAR", "APR", "MAY",
                                "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "ANN"]
            df = df[required_columns]  # Select only these columns

            # Append the DataFrame to the list
            data_frames.append(df)

        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

    # Concatenate all data into one DataFrame
    if data_frames:  # Check if there are valid DataFrames
        combined_df = pd.concat(data_frames, ignore_index=True)

        # Debug: Print a summary of the combined DataFrame
        print("Combined DataFrame Columns:", combined_df.columns)
        print("Sample Rows:\n", combined_df.head())

        # Save the concatenated data to a single CSV file
        combined_df.to_csv(output_file, index=False)
        print(f"Concatenated precipitation data saved to {output_file}")
    else:
        print("No valid data files to concatenate.")

# Input folder containing precipitation files
input_folder = "nasa_power_data_csv"

# Output consolidated file
output_file = "east_africa_PRECTOTCORR_SUM_1981_2022.csv"

# Run the function
concatenate_precipitation_data(input_folder, output_file)
