import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

print("Value of sin 90deg",np.sin(np.pi/2))
print("Value of sin ",np.sin(np.pi/6))
print("Value of cos 90deg",np.cos(np.pi/2))
print("Value of tan 90deg ",np.tan(np.pi/2))
print("Value of tan",np.tan(0))

x = np.arange(1,11)
y = np.arange(10,110,10)

plt.figure(figsize=(6,6))
plt.plot(x,y, 'r--')
plt.show()