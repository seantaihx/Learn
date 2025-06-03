import cmath

print("=== 1. Create Complex Numbers ===")
z1 = 3 + 4j
z2 = complex(1, -2)

print("z1 =", z1)
print("z2 =", z2)

print("\n=== 2. Basic Properties ===")
print("Real part of z1:", z1.real)
print("Imaginary part of z1:", z1.imag)
print("Conjugate of z1:", z1.conjugate())
print("Absolute value (magnitude) of z1:", abs(z1))  # Same as math.sqrt(3² + 4²)

print("\n=== 3. Phase and Polar Coordinates ===")
print("Phase (angle in radians) of z1:", cmath.phase(z1))
polar = cmath.polar(z1)
print("Polar form of z1 (r, θ):", polar)

print("\n=== 4. Convert from Polar to Rectangular ===")
r, theta = polar
print("Back to rectangular form:", cmath.rect(r, theta))

print("\n=== 5. Exponential and Logarithm ===")
print("e^z1:", cmath.exp(z1))
print("log(z1):", cmath.log(z1))

print("\n=== 6. Trigonometric Functions ===")
print("cos(z2):", cmath.cos(z2))
print("sin(z2):", cmath.sin(z2))
print("tan(z2):", cmath.tan(z2))

print("\n=== 7. Square Root of Negative Number ===")
print("sqrt(-1) using cmath:", cmath.sqrt(-1))

print("\n=== Done! ===")
