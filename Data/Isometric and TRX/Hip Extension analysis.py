import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import from excel
F = pd.read_excel('Unilateral hip extension TRX 2 (1right,2left).xlsx',usecols="D")
t = pd.read_excel('Unilateral hip extension TRX 2 (1right,2left).xlsx',usecols="E")

# Gradient
dF = np.gradient(F,axis=0)
plt.plot(t,dF)
plt.ylabel('dF(N)')
plt.xlabel('t(s)')
plt.ylim(-15, 15)
plt.xlim(37, 56)
plt.show()
#print(dF)

# Plot the results
plt.plot(t,F)
plt.ylabel('F(N)')
plt.xlabel('t(s)')
plt.ylim(0, 250)
plt.xlim(37, 56)
plt.show()

#Divide the F array in four arrays equally space and plot
tright = t[2900:4500]
tleft = t[5400:7000]
Fright = F[2900:4500]
Fleft = F[5400:7000]

t1 = tright/np.max(tright)*100


# Plot both F right leg and F left leg on the same graph with F left on the secondary axis
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Right leg F(N)', color=color)
ax1.plot(t1, Fright, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 250)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left leg F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(t1, Fleft, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 250)
plt.show()

#Divide the Fright and Fleft into four arrays each composed by one repetition

cycle0 = np.arange(start=0, stop=300, step=1)
cycle = cycle0/np.max(cycle0)*100

Fright1 = F[3000:3300]
Fleft1 = F[5540:5840]

Fright2 = F[3415:3715]
Fleft2 = F[5940:6240]

Fright3 = F[3795:4095]
Fleft3 = F[6325:6625]

Fright4 = F[4155:4455]
Fleft4 = F[6605:6905]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('(%)cycle')
ax1.set_ylabel('Right leg F(N)', color=color)
ax1.plot(cycle, Fright1, color=color)
ax1.plot(cycle, Fright2, color=color)
ax1.plot(cycle, Fright3, color=color)
ax1.plot(cycle, Fright4, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 250)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left leg F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(cycle, Fleft1, color=color)
ax2.plot(cycle, Fleft2, color=color)
ax2.plot(cycle, Fleft3, color=color)
ax2.plot(cycle, Fleft4, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 250)
plt.show()

#Export to CSV

#df = pd.DataFrame(data=np.column_stack((cycle,F)),columns=['cycle','F'])
#a = numpy.array([Fleft1],[Fleft2],[Fleft3])
#print(a)
#pd.DataFrame(a).to_csv("df.csv")


# Calculate the average of Fright and Fleft and plot them

Fright1np = np.array(Fright1)
Fright2np = np.array(Fright2)
Fright3np = np.array(Fright3)
Fright4np = np.array(Fright4)
Fright_av = np.arange(start=0, stop=300, step=1)

Fleft1np = np.array(Fleft1)
Fleft2np = np.array(Fleft2)
Fleft3np = np.array(Fleft3)
Fleft4np = np.array(Fleft4)
Fleft_av = np.arange(start=0, stop=300, step=1)

for i in range(len(cycle)):
    Fright_av[i] = (Fright1np[i]+Fright2np[i]+Fright3np[i]+Fright4np[i])/4


for i in range(len(cycle)):
    Fleft_av[i] = (Fleft1np[i]+Fleft2np[i]+Fleft3np[i]+Fleft4np[i])/4

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('(%)cycle')
ax1.set_ylabel('Right leg F(N)', color=color)
ax1.plot(cycle, Fright_av, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(0, 240)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Left leg F(N)', color=color)  # we already handled the x-label with ax1
ax2.plot(cycle, Fleft_av, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Hip extension right and left leg')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.ylim(0, 240)
plt.xlim(0, 100)

plt.show()

#Calculate differences between excercise phases if result>0 Right higher otherwise if result<0 left higher

leg_difference_concentric = max(Fright_av)-max(Fleft_av)
print(leg_difference_concentric)
leg_difference_exxentric = max(Fright_av[150:300])-max(Fleft_av[150:300])
print(leg_difference_exxentric)

#Export to txt file
#np.savetxt('test.out', (Fright1np,Fright2np,Fright3np,Fright4np), delimiter=',')
#np.savetxt('test.out', (Fright1np,Fright2np),delimiter=',')
