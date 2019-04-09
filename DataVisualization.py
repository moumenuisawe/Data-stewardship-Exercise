import matplotlib.pyplot as plt
import pandas as pd

# read result
result = pd.read_csv("Data/Processed/result.csv",usecols=["year","UnEmployeeRate","movieScore"])
# draw chart
plt.plot(result["year"],result["movieScore"], label = "Movie Score")
plt.plot(result["year"],result["UnEmployeeRate"], label = "UnEmployee  Rate")

plt.legend()
plt.show()