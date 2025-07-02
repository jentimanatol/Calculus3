import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define function to plot a triangle with a right angle
def plot_right_triangle(x_value, right_angle_point_label):
    # Points
    A = np.array([3, 8, 1])
    B = np.array([1, 1, 1])
    C = np.array([x_value, 5, 6])

    # Setup 3D plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(f"Right Triangle at Point {right_angle_point_label}, x = {x_value}")
    
    # Plot the triangle edges
    ax.plot(*zip(A, B), color='blue', label='AB')
    ax.plot(*zip(B, C), color='green', label='BC')
    ax.plot(*zip(C, A), color='orange', label='CA')

    # Plot the points
    ax.scatter(*A, color='red', s=50)
    ax.scatter(*B, color='red', s=50)
    ax.scatter(*C, color='red', s=50)

    # Annotate points
    ax.text(*A, 'A', fontsize=12)
    ax.text(*B, 'B', fontsize=12)
    ax.text(*C, 'C', fontsize=12)

    # Axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.tight_layout()
    plt.show()

# Plot both cases
plot_right_triangle(13.5, "A")
plot_right_triangle(-13, "B")
