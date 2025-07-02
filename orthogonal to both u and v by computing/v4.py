import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
u = np.array([3, 4, 8])
v = np.array([1, -4, -2])
u_cross_v = np.cross(u, v)
dot_product = np.dot(u, u_cross_v)

print("u × v =", u_cross_v)
print("u · (u × v) =", dot_product)

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors from origin
origin = np.array([0, 0, 0])
ax.quiver(*origin, *u, color='red', label='u', linewidth=2)
ax.quiver(*origin, *v, color='green', label='v', linewidth=2)
ax.quiver(*origin, *u_cross_v, color='blue', label='u × v', linewidth=2)

# Draw clean X, Y, Z axes manually
ax.plot([0, 30], [0, 0], [0, 0], color='black')  # X axis
ax.plot([0, 0], [-20, 20], [0, 0], color='black')  # Y axis
ax.plot([0, 0], [0, 0], [-20, 20], color='black')  # Z axis

# Set tick marks at start and end
ax.set_xticks([0, 30])
ax.set_yticks([-20, 0, 20])
ax.set_zticks([-20, 0, 20])

# Set axis limits
ax.set_xlim(0, 30)
ax.set_ylim(-20, 20)
ax.set_zlim(-20, 20)

# Axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Remove background and grid
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Legend and layout
ax.legend()
plt.tight_layout()
plt.show()
