import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class PlaneVisualizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Plane + Orthogonal Vector Visualizer")

        # Input frame
        input_frame = tk.Frame(master)
        input_frame.pack(pady=5)

        # Plane coefficients
        tk.Label(input_frame, text="Plane: ax + by + cz + d = 0").grid(row=0, column=0, columnspan=4)

        self.a_entry = self.make_entry(input_frame, "a:", 1, 0, "3")
        self.b_entry = self.make_entry(input_frame, "b:", 1, 2, "-9")
        self.c_entry = self.make_entry(input_frame, "c:", 1, 4, "1")
        self.d_entry = self.make_entry(input_frame, "d:", 1, 6, "-27")

        # Point coordinates
        tk.Label(input_frame, text="Point (x, y, z):").grid(row=2, column=0, columnspan=4, pady=(10, 0))

        self.x_entry = self.make_entry(input_frame, "x₀:", 3, 0, "3")
        self.y_entry = self.make_entry(input_frame, "y₀:", 3, 2, "1")
        self.z_entry = self.make_entry(input_frame, "z₀:", 3, 4, "27")

        # Plot button
        tk.Button(input_frame, text="Plot Plane & Vector", command=self.plot_plane).grid(row=4, column=0, columnspan=7, pady=10)

        # Plot canvas
        self.fig = plt.figure(figsize=(6, 5))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

    def make_entry(self, frame, label, row, col, default):
        tk.Label(frame, text=label).grid(row=row, column=col, padx=2)
        entry = tk.Entry(frame, width=5)
        entry.insert(0, default)
        entry.grid(row=row, column=col+1, padx=2)
        return entry

    def plot_plane(self):
        try:
            # Read user inputs
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            d = float(self.d_entry.get())

            x0 = float(self.x_entry.get())
            y0 = float(self.y_entry.get())
            z0 = float(self.z_entry.get())

            # Check if point satisfies the plane
            if abs(a * x0 + b * y0 + c * z0 + d) > 1e-6:
                messagebox.showwarning("Warning", "The point does NOT lie on the plane!")

            # Generate plane grid
            xx, yy = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))
            if c != 0:
                zz = (-a * xx - b * yy - d) / c
            else:
                zz = np.zeros_like(xx) + z0  # fallback (plane perpendicular to z)

            self.ax.clear()

            # Plot plane
            self.ax.plot_surface(xx, yy, zz, alpha=0.5, color='skyblue', edgecolor='gray')

            # Plot point
            self.ax.scatter(x0, y0, z0, color='red', s=80, label='Point')

            # Plot normal vector from point
            n = np.array([a, b, c])
            t_vals = np.linspace(-2, 2, 10)
            vx = x0 + t_vals * n[0]
            vy = y0 + t_vals * n[1]
            vz = z0 + t_vals * n[2]
            self.ax.plot(vx, vy, vz, color='black', linewidth=2, label='Normal Vector')

            # Axes and labels
            self.ax.set_xlim(-10, 10)
            self.ax.set_ylim(-10, 10)
            self.ax.set_zlim(-10, 30)

            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.set_zlabel('Z')
            self.ax.set_title(f"Plane: {a}x + {b}y + {c}z + {d} = 0")

            self.ax.legend()
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PlaneVisualizerApp(root)
    root.mainloop()
