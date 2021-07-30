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
plt.plot(F)
plt.ylabel('F(N)')
plt.xlabel('samples')
#plt.ylim(0, 250)
#plt.xlim(37, 90)
plt.show()

#Divide the F array in four arrays equally space and plot
tleft = t[2800:5000]
tright = t[5000:7200]
Fleft = F[2800:5000]
Fright = F[5000:7200]

t1 = tright/np.max(tright)*100

# Plot both F right arm and F left arm on the same graph with F left on the secondary axis
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Right arm F(N)', color=color)
ax1.plot(t1, Fright, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 100)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left arm F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(t1, Fleft, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 100)
plt.show()

#Divide the Fright and Fleft into four arrays each composed by one repetition

cycle0 = np.arange(start=0, stop=400, step=1)
cycle = cycle0/np.max(cycle0)*100

Fleft1 = F[3060:3460]
Fright1 = F[5240:5640]

Fleft2 = F[3570:3970]
Fright2 = F[6020:6420]

Fleft3 = F[4290:4690]
Fright3 = F[6760:7160]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('(%)cycle')
ax1.set_ylabel('Right arm F(N)', color=color)
ax1.plot(cycle, Fright1, color=color)
ax1.plot(cycle, Fright2, color=color)
ax1.plot(cycle, Fright3, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 100)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left arm F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(cycle, Fleft1, color=color)
ax2.plot(cycle, Fleft2, color=color)
ax2.plot(cycle, Fleft3, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 100)
plt.show()

# Calculate the average of Fright and Fleft and plot them

Fright1np = np.array(Fright1)
Fright2np = np.array(Fright2)
Fright3np = np.array(Fright3)
Fright_av = np.arange(start=0, stop=400, step=1)

Fleft1np = np.array(Fleft1)
Fleft2np = np.array(Fleft2)
Fleft3np = np.array(Fleft3)
Fleft_av = np.arange(start=0, stop=400, step=1)

for i in range(len(cycle)):
    Fright_av[i] = (Fright1np[i]+Fright2np[i]+Fright3np[i])/3


for i in range(len(cycle)):
    Fleft_av[i] = (Fleft1np[i]+Fleft2np[i]+Fleft3np[i])/3

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('(%)cycle')
ax1.set_ylabel('Right leg F(N)', color=color)
ax1.plot(cycle, Fright_av, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 100)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left leg F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(cycle, Fleft_av, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Shoulder External Rotation')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 100)
plt.xlim(0, 100)

plt.show()
