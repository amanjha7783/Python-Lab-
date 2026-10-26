import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x_sin = np.arange(0, 2*np.pi, 0.1)
y_sin = np.sin(x_sin)

print(y_sin)


plt.figure(figsize=(6,6))
plt.plot(x_sin,y_sin)
plt.title("sin curve")
plt.show()