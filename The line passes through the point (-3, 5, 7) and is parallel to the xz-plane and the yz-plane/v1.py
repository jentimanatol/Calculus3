import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ZAxisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Z-Axis Line Mover")

        # Initial coordinates
        self.x = -3
        self.y = 5
        self.z = 7

        # Create 3D figure and axis
        self.fig = plt.figure(figsize=(25, 15))
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Embed the matplotlib plot in the Tkinter GUI
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Initial plot
        self.plot_point()

        # Label showing current Z value
        self.z_label = tk.Label(master, text=f"Z = {self.z}", font=("Arial", 14))
        self.z_label.pack(pady=5)

        # Buttons to control movement
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        self.up_button = tk.Button(btn_frame, text="Up (+)", command=self.increase_z, width=10)
        self.up_button.grid(row=0, column=0, padx=5)

        self.down_button = tk.Button(btn_frame, text="Down (-)", command=self.decrease_z, width=10)
        self.down_button.grid(row=0, column=1, padx=5)

    def plot_point(self):
        # Clear and redraw the plot
        self.ax.clear()
        self.ax.scatter(self.x, self.y, self.z, color='red', s=60)
        
        # Optionally show the full vertical line:
        self.ax.plot([self.x, self.x], [self.y, self.y], [0, 20], color='gray', linestyle='--', linewidth=1)

        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(0, 20)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('Point on Line: x = -3, y = 5, z = z')

        self.canvas.draw()

    def increase_z(self):
        self.z += 1
        self.z_label.config(text=f"Z = {self.z}")
        self.plot_point()

    def decrease_z(self):
        self.z -= 1
        self.z_label.config(text=f"Z = {self.z}")
        self.plot_point()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ZAxisApp(root)
    root.mainloop()
