import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Import from excel
ppr = 2400 #Pulses per revolution
F_raw = pd.read_excel('Conical.xlsx',usecols="B")
a_raw = pd.read_excel('Conical.xlsx',usecols="A")
tms = pd.read_excel('Conical.xlsx',usecols="C")
t = tms/1000;
a = -1*a_raw*2*math.pi/ppr
F_raw = np.array(F_raw)
F = 0.0011*F_raw-1.248 #Using load cell calibration equation
#print(len(t))

da = np.gradient(a,axis=0)
dt = np.gradient(t,axis=0)

w = da/dt


# Plot both signals a and F
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('t(s)')
ax1.set_ylabel('F(N)', color=color)
ax1.plot(t, F, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 500)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('angle(rad)', color=color)  # we already handled the x-label with ax1
ax2.plot(t, a, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Conical pulley angle and force')
plt.ylim(-10, 40)
plt.xlim(16, 20)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


# Plot both signals w and F
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('t(s)')
ax1.set_ylabel('F(N)', color=color)
ax1.plot(t, F, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 500)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('angle(rad)', color=color)  # we already handled the x-label with ax1
ax2.plot(t, w, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Conical pulley angular speed and force')
plt.ylim(-100, 100)
plt.xlim(16, 20)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

