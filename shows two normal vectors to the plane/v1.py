import numpy as np
import matplotlib.pyplot as plt

# Define the plane: 3x - 9y + z - 27 = 0
# Solve for z: z = 27 - 3x + 9y

# Create a grid of x and y values
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Compute corresponding z values
Z = 27 - 3*X + 9*Y

# Normal vectors (scaled for visualization)
n1 = np.array([3, -9, 1])
n2 = -2 * n1

# Choose a point on the plane for the normal vectors to start (e.g., at x=0,y=0,z=27)
origin = np.array([0, 0, 27])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', edgecolor='none')

# Plot normal vectors as arrows
ax.quiver(*origin, *n1, length=5, color='red', normalize=True, label='Normal Vector n1')
ax.quiver(*origin, *n2, length=5, color='blue', normalize=True, label='Normal Vector n2')

# Plot the origin point for reference
ax.scatter(*origin, color='black', s=50, label='Point on Plane')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane: 3x - 9y + z - 27 = 0 and Normal Vectors')

ax.legend()

# Set plot limits for better visualization
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([0, 50])

plt.show()
