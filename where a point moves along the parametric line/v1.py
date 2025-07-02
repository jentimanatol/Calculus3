import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

class ParametricLineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Animated Parametric Line")

        # Initial t value and animation control
        self.t = 0
        self.animating = False

        # Fixed z value from the equation
        self.z = -6

        # Create figure and 3D axis
        self.fig = plt.figure(figsize=(15, 14))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Initial plot
        self.plot_point()

        # Label for t
        self.t_label = tk.Label(master, text=f"t = {self.t}", font=("Arial", 14))
        self.t_label.pack(pady=5)

        # Control buttons
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start_animation, width=10)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_animation, width=10)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_animation, width=10)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def parametric_point(self, t):
        # Line: x = 5 + 3t, y = 2 - 4t, z = -6
        x = 5 + 3 * t
        y = 2 - 4 * t
        z = self.z
        return x, y, z

    def plot_point(self):
        self.ax.clear()

        # Current position
        x, y, z = self.parametric_point(self.t)
        self.ax.scatter(x, y, z, color='red', s=60)

        # Draw full parametric line for reference
        t_vals = [i for i in range(-10, 11)]
        x_vals = [5 + 3 * t for t in t_vals]
        y_vals = [2 - 4 * t for t in t_vals]
        z_vals = [self.z for _ in t_vals]
        self.ax.plot(x_vals, y_vals, z_vals, color='gray', linestyle='--')

        # Axes labels and limits
        self.ax.set_xlim(-30, 30)
        self.ax.set_ylim(-40, 40)
        self.ax.set_zlim(-10, 0)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('Point on Parametric Line')

        self.canvas.draw()

    def start_animation(self):
        if not self.animating:
            self.animating = True
            threading.Thread(target=self.animate).start()

    def animate(self):
        while self.animating:
            self.t += 0.1
            self.t_label.config(text=f"t = {self.t:.2f}")
            self.plot_point()
            time.sleep(0.1)

    def stop_animation(self):
        self.animating = False

    def reset_animation(self):
        self.animating = False
        self.t = 0
        self.t_label.config(text=f"t = {self.t}")
        self.plot_point()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ParametricLineApp(root)
    root.mainloop()
