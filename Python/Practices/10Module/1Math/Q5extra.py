import cmath
import numpy as np
import matplotlib.pyplot as plt

# Create a grid of complex numbers z = x + iy
x = np.linspace(-10, 10, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Compute e^(iZ)
E = np.exp(1j * Z)

# Magnitude and Phase
magnitude = np.abs(E)
phase = np.angle(E)

# Plot magnitude
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.contourf(X, Y, magnitude, levels=100, cmap='viridis')
plt.title("Magnitude of e^(i(x + iy))")
plt.xlabel("Real part (x)")
plt.ylabel("Imag part (y)")
plt.colorbar(label='|e^(iZ)|')

# Plot phase
plt.subplot(1, 2, 2)
plt.contourf(X, Y, phase, levels=100, cmap='twilight_shifted')
plt.title("Phase of e^(i(x + iy))")
plt.xlabel("Real part (x)")
plt.colorbar(label='Phase (radians)')

plt.tight_layout()
plt.savefig("Q5extra.png", dpi=300) 
plt.show()
