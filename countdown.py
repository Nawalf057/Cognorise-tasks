import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("400x250")
        self.root.configure(bg="#e0f7fa")  # Light cyan background

        # Initialize timer variables
        self.time_left = 0
        self.timer_running = False
        
        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Create widgets with a solid background color
        self.title_label = tk.Label(self.root, text="Countdown Timer", font=('Helvetica', 20, 'bold'), bg="#00bcd4", fg="#ffffff")
        self.title_label.pack(pady=10)

        self.time_label = tk.Label(self.root, text="Enter time (seconds):", font=('Helvetica', 15), bg="#e0f7fa", fg="#000000")
        self.time_label.pack(pady=5)
        
        self.time_entry = tk.Entry(self.root, font=('Helvetica', 15))
        self.time_entry.pack(pady=5)
        
        self.start_button = tk.Button(self.root, text="Start Timer", command=self.start_timer, font=('Helvetica', 15), bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop Timer", command=self.stop_timer, font=('Helvetica', 15), bg="#FFC107", fg="#000000", relief=tk.RAISED)
        self.stop_button.pack(pady=5)
        
        self.reset_button = tk.Button(self.root, text="Reset Timer", command=self.reset_timer, font=('Helvetica', 15), bg="#FF5722", fg="#ffffff", relief=tk.RAISED)
        self.reset_button.pack(pady=10)
        
        self.timer_display = tk.Label(self.root, text="00:00", font=('Helvetica', 50, 'bold'), bg="#e0f7fa", fg="#000000")
        self.timer_display.pack(pady=20)

    def start_timer(self):
        try:
            self.time_left = int(self.time_entry.get())
            if self.time_left <= 0:
                raise ValueError
            self.timer_running = True
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")

    def update_timer(self):
        if self.timer_running:
            if self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                self.timer_display.config(text=f"{mins:02}:{secs:02}")
                self.time_left -= 1
                self.root.after(1000, self.update_timer)  # Update every second
            else:
                self.timer_display.config(text="00:00")
                self.timer_running = False
                messagebox.showinfo("Time's Up", "The countdown has finished!")

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.stop_timer()
        self.time_entry.delete(0, tk.END)
        self.timer_display.config(text="00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
