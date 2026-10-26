import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x_sin = np.arange(0, 2*np.pi, 0.1)
y_sin = np.sin(x_sin)

print(y_sin)


x_cos = np.arange(0, 2*np.pi, 0.1)
y_cos = np.cos(x_cos)

print(y_cos)

x_tan = np.arange(0, 2*np.pi, 0.1)
y_tan = np.tan(x_tan)

print(y_tan)


x_cot = np.arange(0, 2*np.pi, 0.1)
y_cot = 1/np.tan(x_cot)

print(y_cot)


plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
plt.plot(x_sin,y_sin, 'r--')
plt.title("sin curve")

plt.subplot(2,2,2)
plt.plot(x_cos,y_cos, 'b--')
plt.title("cos curve")

plt.subplot(2,2,3)
plt.plot(x_tan,y_tan, 'g--')
plt.title("tan curve")

plt.subplot(2,2,4)
plt.plot(x_cot,y_cot, 'y--')
plt.title("cot curve")

plt.show()