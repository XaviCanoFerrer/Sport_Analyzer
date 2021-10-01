import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import plotly.graph_objects as go
from scipy.signal import find_peaks

# Import from excel
mmpp = 0.063 # mm per pulse 0.063
encoder_raw = pd.read_excel('BOSCO.xlsx',usecols="B")
tms = pd.read_excel('BOSCO.xlsx',usecols="D")
t = tms/1000;
s_mm = encoder_raw*mmpp # Displacement in mm
s = s_mm/1000 # Displacement in mm



# Find the minimum
minimum = np.min(s)
print(minimum)

# Add this offset to the displacement to get a positive displacement

s = s + abs(minimum)

# Calculate speed in mm/s
ds = np.gradient(s,axis=0)
dt = np.gradient(t,axis=0)
v = ds/dt

# Plot displacement
plt.plot(t,s)
plt.ylabel('Displacement (m)')
plt.xlabel('Time (s)')
plt.ylim(0, 0.7)
plt.xlim(40, 115)
plt.show()

# Plot velocity
plt.plot(t,v)
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
#plt.ylim(-0.25, 0.32)
plt.xlim(40, 115)
plt.show()

m = 69
F = m*9.81
P = F*v

# Plot power
plt.plot(t,P)
plt.ylabel('Power W')
plt.xlabel('Time (s)')
#plt.ylim(-0.25, 0.32)
plt.xlim(40, 115)
plt.show()

P = P.flatten()

# Find peaks on the power signal
peaks, _ = find_peaks(P, height=700)
plt.plot(P)
plt.plot(peaks, P[peaks], "P")
plt.ylabel('Power W')
plt.xlabel('Time (s)')
plt.xlim(4500, 11000)
#plt.plot(np.zeros_like(P), "--", color="gray")
plt.show()
