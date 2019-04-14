import matplotlib.pyplot as plt
import pandas as pd

# read result
result = pd.read_csv("Data/Processed/result.csv",usecols=["year","UnEmployeeRate","movieScore"])


plt.rcParams.update({'font.size': 18})

# draw chart
plt.plot(result["year"],result["movieScore"], label = "Movie Score")
plt.plot(result["year"],result["UnEmployeeRate"], label = "UnEmployee  Rate")

plt.legend()
plt.savefig("reports/correlation.png")
plt.show()
