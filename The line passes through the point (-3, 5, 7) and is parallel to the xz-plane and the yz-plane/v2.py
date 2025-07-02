import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ZAxisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Line Mover")

        # Default coordinates
        self.x = -3
        self.y = 5
        self.z = 7

        # Create 3D figure and axis
        self.fig = plt.figure(figsize=(20, 15))
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Embed matplotlib canvas in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        # Plot the initial point
        self.plot_point()

        # Frame for user input fields (x and y)
        input_frame = tk.Frame(master)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="X:").grid(row=0, column=0)
        self.x_entry = tk.Entry(input_frame, width=5)
        self.x_entry.insert(0, str(self.x))
        self.x_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Y:").grid(row=0, column=2)
        self.y_entry = tk.Entry(input_frame, width=5)
        self.y_entry.insert(0, str(self.y))
        self.y_entry.grid(row=0, column=3, padx=5)

        self.update_button = tk.Button(input_frame, text="Update Position", command=self.update_xy)
        self.update_button.grid(row=0, column=4, padx=5)

        # Label showing Z value
        self.z_label = tk.Label(master, text=f"Z = {self.z}", font=("Arial", 14))
        self.z_label.pack(pady=5)

        # Buttons for moving z
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        self.up_button = tk.Button(btn_frame, text="Up (+)", command=self.increase_z, width=10)
        self.up_button.grid(row=0, column=0, padx=5)

        self.down_button = tk.Button(btn_frame, text="Down (-)", command=self.decrease_z, width=10)
        self.down_button.grid(row=0, column=1, padx=5)

    def plot_point(self):
        self.ax.clear()
        self.ax.scatter(self.x, self.y, self.z, color='red', s=60)

        # Show vertical line through current x, y
        self.ax.plot([self.x, self.x], [self.y, self.y], [0, 20], color='gray', linestyle='--', linewidth=1)

        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(0, 20)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('Point on Line: x = const, y = const, z = z')

        self.canvas.draw()

    def increase_z(self):
        self.z += 1
        self.z_label.config(text=f"Z = {self.z}")
        self.plot_point()

    def decrease_z(self):
        self.z -= 1
        self.z_label.config(text=f"Z = {self.z}")
        self.plot_point()

    def update_xy(self):
        try:
            self.x = float(self.x_entry.get())
            self.y = float(self.y_entry.get())
            self.plot_point()
        except ValueError:
            self.z_label.config(text="Invalid input for X or Y")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ZAxisApp(root)
    root.mainloop()
