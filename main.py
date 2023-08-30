import matplotlib.pyplot as plt
import numpy as np

# Circle parameters (center coordinates and radii)
pCirc1 = (2, 2)
R_Circ1 = 3

pCirc2 = (5, 5)
R_Circ2 = 4

# Calculate distance between circle centers
L = np.sqrt((pCirc2[0] - pCirc1[0]) ** 2 + (pCirc2[1] - pCirc1[1]) ** 2)

# Determine the relationship between the circles
if L > R_Circ1 + R_Circ2:              # Circles are separate
    intersection_points = []
elif L < np.abs(R_Circ2 - R_Circ1):    # One circle is contained within the other
    intersection_points = []
elif L == 0 and R_Circ1 == R_Circ2:    # Circles coincide
    intersection_points = []
else:                                         # Circles are intersecting or tangent
    a = (R_Circ1 ** 2 - R_Circ2 ** 2 + L ** 2) / (2 * L)
    h = np.sqrt(R_Circ1 ** 2 - a ** 2)
    intersection_point1 = (pCirc1[0] + a * (pCirc2[0] - pCirc1[0]) / L,
                           pCirc1[1] + a * (pCirc2[1] - pCirc1[1]) / L)
    intersection_point2 = (intersection_point1[0] + h * (pCirc2[1] - pCirc1[1]) / L,
                           intersection_point1[1] - h * (pCirc2[0] - pCirc1[0]) / L)
    intersection_point3 = (intersection_point1[0] - h * (pCirc2[1] - pCirc1[1]) / L,
                           intersection_point1[1] + h * (pCirc2[0] - pCirc1[0]) / L)
    intersection_points = [intersection_point2, intersection_point3]

# Visualization
theta = np.linspace(0, 2 * np.pi, 100)
circle1_x = pCirc1[0] + R_Circ1 * np.cos(theta)
circle1_y = pCirc1[1] + R_Circ1 * np.sin(theta)
circle2_x = pCirc2[0] + R_Circ2 * np.cos(theta)
circle2_y = pCirc2[1] + R_Circ2 * np.sin(theta)

plt.figure(figsize=(8, 6))
plt.plot(circle1_x, circle1_y, label='Circle 1')
plt.plot(circle2_x, circle2_y, label='Circle 2')
plt.scatter(*pCirc1, color='red', label='Center 1')
plt.scatter(*pCirc2, color='blue', label='Center 2')
for point in intersection_points:
    plt.scatter(*point, color='green', label='Intersection Point')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Circle Intersection')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()
