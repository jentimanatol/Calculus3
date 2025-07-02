import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PlaneVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Plane and Orthogonal Vector Visualizer")

        # Set up matplotlib 3D figure
        self.fig = plt.figure(figsize=(16, 15))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Plot all elements
        self.plot_plane_and_vector()

    def plot_plane_and_vector(self):
        self.ax.clear()

        # Define grid for the plane
        xx, yy = np.meshgrid(range(-5, 10), range(-5, 10))
        # From 3x - 9y + z - 27 = 0 => z = 27 - 3x + 9y
        zz = 27 - 3 * xx + 9 * yy

        # Plot the plane
        self.ax.plot_surface(xx, yy, zz, alpha=0.5, color='skyblue', edgecolor='gray', linewidth=0.5)

        # Given point
        px, py, pz = 3, 1, 27
        self.ax.scatter(px, py, pz, color='red', s=80, label='Point on Plane')

        # Normal vector to plane: <3, -9, 1>
        n = np.array([3, -9, 1])
        t_vals = np.linspace(-2, 2, 10)
        line_x = px + t_vals * n[0]
        line_y = py + t_vals * n[1]
        line_z = pz + t_vals * n[2]

        self.ax.plot(line_x, line_y, line_z, color='black', linewidth=2, label='Orthogonal Vector')

        # Axis settings
        self.ax.set_xlim(-5, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(0, 40)

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title("Plane: 3x - 9y + z = 27")

        self.ax.legend()
        self.canvas.draw()

# Launch the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PlaneVisualizer(root)
    root.mainloop()
