import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.cos(10*np.pi*pow(t,2))
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('Unit')
plt.title('Graph for Ch1Q1')
plt.grid(True)
plt.savefig("ch1q1.png")
plt.show()
