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
print(f"u · (u × v) = {dot_product}")  # Should be 0 if orthogonal

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin point
origin = np.array([0, 0, 0])

# Plot vectors u, v, and u × v
ax.quiver(*origin, *u, color='r', label='u', length=1, normalize=False)
ax.quiver(*origin, *v, color='g', label='v', length=1, normalize=False)
ax.quiver(*origin, *u_cross_v, color='b', label='u × v', length=1, normalize=False)

# Label axes
ax.set_xlim([0, 30])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vectors u, v and u × v (Cross Product)')

ax.legend()
plt.tight_layout()
plt.show()
