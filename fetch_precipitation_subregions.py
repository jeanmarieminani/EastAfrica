import os
import time
import requests

def request_power_data_csv(lat_min, lat_max, lon_min, lon_max, start_year, end_year, file_name):
    """Request NASA POWER data for PRECTOTCORR_SUM and save it as CSV."""
    url = "https://power.larc.nasa.gov/api/temporal/monthly/regional"
    params = {
        "parameters": "PRECTOTCORR_SUM",  # Corrected precipitation sum
        "community": "AG",               # Agriculture community
        "longitude-min": lon_min,
        "longitude-max": lon_max,
        "latitude-min": lat_min,
        "latitude-max": lat_max,
        "format": "CSV",                 # Output format
        "start": start_year,             # Start year
        "end": end_year,                 # End year
    }

    try:
        print(f"Requesting PRECTOTCORR_SUM data for {file_name}")
        print(f"Parameters: {params}")
        response = requests.get(url, params=params, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Save the response content directly to file
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Successfully downloaded: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {file_name}: {e}")
        if response.text:
            print(f"Response content: {response.text}")
        print("Skipping to the next request...")

def main():
    # Output directory
    output_dir = "nasa_power_data_csv"
    os.makedirs(output_dir, exist_ok=True)

    # Define sub-regions
    sub_regions = [
        {"lat_min": -12, "lat_max": -2, "lon_min": 28, "lon_max": 38},
        {"lat_min": -12, "lat_max": -2, "lon_min": 38, "lon_max": 48},
        {"lat_min": -2, "lat_max": 8, "lon_min": 28, "lon_max": 38},
        {"lat_min": -2, "lat_max": 8, "lon_min": 38, "lon_max": 48},
        {"lat_min": 8, "lat_max": 18, "lon_min": 28, "lon_max": 38},
        {"lat_min": 8, "lat_max": 18, "lon_min": 38, "lon_max": 48},
    ]

    # Define years
    start_year = 1981
    end_year = 2022

    # Loop through sub-regions
    for i, region in enumerate(sub_regions):
        file_name = os.path.join(
            output_dir,
            f"region_{i+1}_PRECTOTCORR_SUM_{start_year}_{end_year}.csv"
        )
        request_power_data_csv(
            lat_min=region["lat_min"],
            lat_max=region["lat_max"],
            lon_min=region["lon_min"],
            lon_max=region["lon_max"],
            start_year=start_year,
            end_year=end_year,
            file_name=file_name
        )
        # Delay between requests to avoid server overload
        time.sleep(2)

if __name__ == "__main__":
    main()
