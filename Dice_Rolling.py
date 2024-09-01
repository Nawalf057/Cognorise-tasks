import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class DiceRollingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Rolling Simulator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f5f5f5")  # Light grey background

        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Dice Rolling Simulator", font=('Helvetica', 20, 'bold'), bg="#ffcc00", fg="#000000")
        self.title_label.pack(pady=10)

        self.sides_label = tk.Label(self.root, text="Number of Sides:", font=('Helvetica', 15), bg="#f5f5f5", fg="#000000")
        self.sides_label.pack(pady=5)
        
        self.sides_entry = tk.Entry(self.root, font=('Helvetica', 15))
        self.sides_entry.pack(pady=5)
        
        self.rolls_label = tk.Label(self.root, text="Number of Rolls:", font=('Helvetica', 15), bg="#f5f5f5", fg="#000000")
        self.rolls_label.pack(pady=5)
        
        self.rolls_entry = tk.Entry(self.root, font=('Helvetica', 15))
        self.rolls_entry.pack(pady=5)

        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice, font=('Helvetica', 15), bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)
        self.roll_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 15), bg="#f5f5f5", fg="#000000")
        self.result_label.pack(pady=20)
        
    def roll_dice(self):
        try:
            num_sides = int(self.sides_entry.get())
            num_rolls = int(self.rolls_entry.get())
            
            if num_sides < 1 or num_rolls < 1:
                raise ValueError
            
            results = [random.randint(1, num_sides) for _ in range(num_rolls)]
            result_text = "Roll Results:\n" + ", ".join(map(str, results))
            self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers greater than 0.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollingSimulator(root)
    root.mainloop()
