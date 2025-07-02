import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
u = np.array([3, 4, 8])
v = np.array([1, -4, -2])
u_cross_v = np.cross(u, v)
dot_product = np.dot(u, u_cross_v)

print(f"u × v = {u_cross_v}")
print(f"u · (u × v) = {dot_product}")

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0, 0, 0])

# Plot vectors
ax.quiver(*origin, *u, color='r', label='u', linewidth=2)
ax.quiver(*origin, *v, color='g', label='v', linewidth=2)
ax.quiver(*origin, *u_cross_v, color='b', label='u × v', linewidth=2)

# Axis limits
ax.set_xlim([0, 30])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

# Axis ticks
ax.set_xticks(np.linspace(0, 30, 4))
ax.set_yticks(np.linspace(-20, 20, 5))
ax.set_zticks(np.linspace(-20, 20, 5))

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Turn off grid and pane backgrounds
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Remove 3D box
ax.set_box_aspect([1, 1, 1])
ax.w_xaxis.line.set_color('black')
ax.w_yaxis.line.set_color('black')
ax.w_zaxis.line.set_color('black')

# Remove axis panes’ edgecolors except for axis lines
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')

# Legend and layout
ax.legend()
plt.tight_layout()
plt.show()
