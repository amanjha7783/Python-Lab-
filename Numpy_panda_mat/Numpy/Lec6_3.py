import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x_cos = np.arange(0, 2*np.pi, 0.1)
y_cos = np.cos(x_cos)

print(y_cos)


plt.figure(figsize=(6,6))
plt.plot(x_cos,y_cos)
plt.title("sin curve")
plt.show()