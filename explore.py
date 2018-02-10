import pandas as pd
import matplotlib.pyplot as plt
# Read in the data set
_dt = pd.read_csv("PS_20174392719_1491204439457_log.csv")

# Visualise steps
n , b , p = plt.hist(_dt['step'],50,normed=1,facecolor='red')
plt.plot(b)
plt.show()
# Seems that