import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the three points
P1 = np.array([3, 4, 5])
P2 = np.array([-2, -9, 0])
P3 = np.array([4, 4, 3])

# Compute two vectors on the plane
v1 = P2 - P1
v2 = P3 - P1

# Compute the normal vector using cross product
n = np.cross(v1, v2)
a, b, c = n
# Calculate d using one of the points in the plane equation
d = a * P1[0] + b * P1[1] + c * P1[2]

# Create meshgrid for x and y
xx, yy = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

# Solve for z using the plane equation: ax + by + cz = d ⇒ z = (d - ax - by)/c
zz = (d - a * xx - b * yy) / c

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='skyblue', rstride=1, cstride=1, edgecolor='gray')

# Plot the points
ax.scatter(*P1, color='red', s=60, label='P1 (3,4,5)')
ax.scatter(*P2, color='green', s=60, label='P2 (-2,-9,0)')
ax.scatter(*P3, color='blue', s=60, label='P3 (4,4,3)')

# Labels and legend
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Plane Through 3 Points")
ax.legend()

# Set limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

plt.tight_layout()
plt.show()
