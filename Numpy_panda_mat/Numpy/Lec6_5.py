import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x_cot = np.arange(0, 2*np.pi, 0.1)
y_cot = 1/np.tan(x_cot)

print(y_cot)

plt.figure(figsize=(6,6))
plt.plot(x_cot,y_cot)
plt.title("sin curve")
plt.show()