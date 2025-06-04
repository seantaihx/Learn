'''
Plot the values of exp(iz) where z ranges from -10 to 10 (real axis), 
using cmath.exp() and any plotting library.
'''

import cmath as c
import matplotlib.pyplot as plt


real_values = [x * 0.1 for x in range(-100, 101)]  # steps of 0.1
results = [c.exp(1j * x) for x in real_values]

x_vals = [z.real for z in results]
y_vals = [z.imag for z in results]


plt.plot(x_vals, y_vals)
plt.title("Plot of e^(ix) on the Complex Plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid(True)
plt.axis("equal") 
plt.show()
plt.savefig("Q5ans.png", dpi=300)