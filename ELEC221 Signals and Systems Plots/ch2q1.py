import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
#s = np.cos(10*np.pi*pow(t,2))
s = (1 + np.cos(np.pi * t)) * np.sin(2 * np.pi * 20 * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('Unit')
plt.title('Graph for Ch2Q1')
plt.grid(True)
plt.savefig("ch2q1.png")
plt.show()
