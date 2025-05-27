import math

print("=== 1. Basic Constants ===")
print("Pi:", math.pi)
print("Euler's number (e):", math.e)

print("\n=== 2. Rounding Functions ===")
print("math.ceil(4.3):", math.ceil(4.3))     # Round up
print("math.floor(4.7):", math.floor(4.7))   # Round down
print("math.trunc(4.9):", math.trunc(4.9))   # Remove decimal

print("\n=== 3. Power and Roots ===")
print("math.pow(2, 3):", math.pow(2, 3))     # 2^3 as float
print("math.sqrt(16):", math.sqrt(16))       # Square root
print("5 ** 2 =", 5 ** 2)                    # Built-in power operator

print("\n=== 4. Absolute and Logarithm ===")
print("math.fabs(-7):", math.fabs(-7))       # Absolute value (float)
print("math.log(100, 10):", math.log(100, 10))  # log base 10
print("math.log10(100):", math.log10(100))   # Same as above

print("\n=== 5. Trigonometry (in Radians) ===")
angle_rad = math.radians(90)  # Convert degrees to radians
print("math.sin(90°):", math.sin(angle_rad))
print("math.cos(90°):", math.cos(angle_rad))
print("math.tan(45°):", math.tan(math.radians(45)))

print("\n=== 6. Degree/Radian Conversion ===")
print("Convert 180° to radians:", math.radians(180))
print("Convert π radians to degrees:", math.degrees(math.pi))

print("\n=== 7. Min/Max with math.inf ===")
print("math.isinf(9999999999):", math.isinf(9999999999))
print("Max of [3, 7, -2]:", max([3, 7, -2]))
print("math.inf is larger than 1e10:", math.inf > 1e10)

print("\n=== Done! ===")
