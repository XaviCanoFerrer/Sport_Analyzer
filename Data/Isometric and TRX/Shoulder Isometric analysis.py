import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import from excel
F_raw = pd.read_excel('Isometric.xlsx',usecols="B")
tms = pd.read_excel('Isometric.xlsx',usecols="C")
t = tms/1000
F_raw = np.array(F_raw)
F = 0.0011*F_raw-4.9839 #Using load cell calibration equation

# Plot the results
plt.plot(t,F)
plt.ylabel('F(N)')
plt.xlabel('t(s)')
#plt.ylim(0, 250)
plt.xlim(37, 90)
plt.show()
