import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Import from excel
encoder = pd.read_excel('Encoder calibration2.xlsx',usecols="A")
F = pd.read_excel('Load cell calibration.xlsx',usecols="A")
Sensor_val = pd.read_excel('Load cell calibration.xlsx',usecols="B")
samples = np.arange(start=1, stop=16, step=1)

# Plot load cell function
plt.plot(Sensor_val,F,'k')
plt.scatter(Sensor_val,F, c='k')
plt.ylabel('Force (N)')
plt.xlabel('Sensor value')
plt.title('Load cell calibration')
#plt.ylim(0, 180)
#plt.xlim(223.5, 226)
plt.show()


# Plot encoder samples
#plt.scatter(samples,encoder)
#plt.plot(samples,encoder)
plt.boxplot(encoder)
plt.ylabel('Pulses')
#plt.xlabel('Samples')
plt.title('Encoder calibration')
#plt.ylim(7500, 8500)
#plt.xlim(0, 16)
plt.show()


# Calculate mean and std

mm_pulse = 500/np.mean(encoder)
print(mm_pulse)

