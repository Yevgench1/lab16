import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 500)

y = 2.2 * np.exp(x) * np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='purple', linestyle='-', linewidth=2)
plt.title(r'$y = 2.2 e^x \cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig("cosinus.png")
plt.show()
