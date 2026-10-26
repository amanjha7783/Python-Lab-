import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x_tan = np.arange(0, 2*np.pi, 0.1)
y_tan = np.tan(x_tan)

print(y_tan)


plt.figure(figsize=(6,6))
plt.plot(x_tan,y_tan)
plt.title("sin curve")
plt.show()