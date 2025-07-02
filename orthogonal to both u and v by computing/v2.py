import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors u and v
u = np.array([3, 4, 8])
v = np.array([1, -4, -2])

# Cross product u × v
u_cross_v = np.cross(u, v)

# Compute dot product u · (u × v)
dot_product = np.dot(u, u_cross_v)

print(f"u × v = {u_cross_v}")
print(f"u · (u × v) = {dot_product}")  # Should be 0

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin
origin = np.array([0, 0, 0])

# Plot vectors u, v, u × v
ax.quiver(*origin, *u, color='r', label='u', linewidth=2)
ax.quiver(*origin, *v, color='g', label='v', linewidth=2)
ax.quiver(*origin, *u_cross_v, color='b', label='u × v', linewidth=2)

# Axis limits
ax.set_xlim([0, 30])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

# Axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('u, v, and u × v (Cross Product)', pad=20)

# Remove grid and panes
ax.grid(False)
ax.xaxis._axinfo["grid"]['linewidth'] = 0
ax.yaxis._axinfo["grid"]['linewidth'] = 0
ax.zaxis._axinfo["grid"]['linewidth'] = 0

# Show axis lines only (no background panes)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Show ticks (numbers) only
ax.set_xticks(np.linspace(0, 30, 4))
ax.set_yticks(np.linspace(-20, 20, 5))
ax.set_zticks(np.linspace(-20, 20, 5))

# Hide axes line "walls" behind the plot
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')

# Legend and layout
ax.legend()
plt.tight_layout()
plt.show()
