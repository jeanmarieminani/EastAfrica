import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
temp_df = pd.read_csv("east_africa_TS_1981_2022.csv")
precip_df = pd.read_csv("east_africa_PRECTOTCORR_SUM_1981_2022.csv")



# Temperature trends
plt.figure(figsize=(10, 5))
plt.plot(temp_trends.index, temp_trends.values, label="Temperature (°C)", color="orange", marker="o")
plt.title("Annual Mean Temperature in Eastern Africa (1981-2022)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.legend()
plt.show()

# Precipitation trends
plt.figure(figsize=(10, 5))
plt.plot(precip_trends.index, precip_trends.values, label="Precipitation (mm)", color="blue", marker="o")
plt.title("Annual Total Precipitation in Eastern Africa (1981-2022)")
plt.xlabel("Year")
plt.ylabel("Precipitation (mm)")
plt.grid()
plt.legend()
plt.show()
