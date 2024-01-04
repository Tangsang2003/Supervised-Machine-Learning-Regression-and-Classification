import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000)  # Start, Finish, Points-in-between
distance_robber = 2.5 * t
distance_sheriff = 3 * (t-5)
fig, ax = plt.subplots()
plt.title('Bank Robber Caught')
plt.xlabel('Time (in minutes)')
plt.ylabel('Distance (in Kms)')
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, distance_robber, c="green")
ax.plot(t, distance_sheriff, c="red")
plt.axvline(x=30, color="purple", linestyle="--")
plt.axhline(y=75, color="purple", linestyle="--")
plt.show()
