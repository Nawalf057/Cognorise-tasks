import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import string
from PIL import Image, ImageTk

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("700x500")
        self.resizable(False, False)

        # Load and set background image
        self.background_image = Image.open("password.png")
        self.background_image = self.background_image.resize((700, 500), Image.Resampling.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.password_history = []
        self._create_widgets()

    def _create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="Password Generator", font=("Arial", 24, "bold"), bg="#2b2f77", fg="#ffffff")
        title_label.pack(pady=20)

        # Frame for Password Length
        frame_length = tk.Frame(self, bg="#2b2f77")
        frame_length.pack(pady=10)
        self.length_label = tk.Label(frame_length, text="Password Length:", font=("Arial", 14, "bold"), bg="#2b2f77", fg="#ffffff")
        self.length_label.pack(side=tk.LEFT, padx=5)
        self.length_entry = tk.Entry(frame_length, font=("Arial", 14), width=5, fg="#000000", bg="#ffffff")
        self.length_entry.pack(side=tk.LEFT, padx=5)

        # Special Characters Checkbox
        self.include_special = tk.BooleanVar()
        self.special_checkbox = tk.Checkbutton(
            self, text="Include special characters", font=("Arial", 12), variable=self.include_special, bg="#2b2f77", fg="#ffffff", selectcolor="#61afef"
        )
        self.special_checkbox.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(
            self, text="Generate Password", font=("Arial", 14, "bold"), command=self.generate_password, bg="#4caf50", fg="#ffffff"
        )
        self.generate_button.pack(pady=10)

        # Frame for Password Display
        frame_display = tk.Frame(self, bg="#2b2f77")
        frame_display.pack(pady=10)
        self.password_display = tk.Entry(frame_display, font=("Arial", 14), borderwidth=2, relief=tk.SUNKEN, width=40, fg="#000000", bg="#ffffff")
        self.password_display.pack(side=tk.LEFT, padx=5)
        self.copy_button = tk.Button(
            frame_display, text="Copy", font=("Arial", 12), command=self.copy_to_clipboard, bg="#f44336", fg="#ffffff"
        )
        self.copy_button.pack(side=tk.LEFT, padx=5)
        self.save_button = tk.Button(
            frame_display, text="Save", font=("Arial", 12), command=self.save_password, bg="#ff9800", fg="#ffffff"
        )
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Show Password Checkbox
        self.show_password = tk.BooleanVar()
        self.show_password_check = tk.Checkbutton(self, text="Show Password", variable=self.show_password, command=self.toggle_password, bg="#2b2f77", fg="#ffffff", selectcolor="#61afef")
        self.show_password_check.pack(pady=5)

        # Strength Meter
        self.strength_meter = tk.Canvas(self, width=300, height=20, bg="#ddd")
        self.strength_meter.pack(pady=5)
        self.strength_label = tk.Label(self, text="", font=("Arial", 14, "bold"), bg="#2b2f77", fg="#ffffff")
        self.strength_label.pack(pady=5)

        # Requirements Frame
        self.requirements_frame = tk.Frame(self, bg="#2b2f77")
        self.requirements_frame.pack(pady=10)
        self.length_req = tk.Label(self.requirements_frame, text="At least 8 characters", font=("Arial", 12), bg="#2b2f77", fg="#ffffff")
        self.length_req.pack(anchor="w")
        self.upper_req = tk.Label(self.requirements_frame, text="At least one uppercase letter", font=("Arial", 12), bg="#2b2f77", fg="#ffffff")
        self.upper_req.pack(anchor="w")
        self.lower_req = tk.Label(self.requirements_frame, text="At least one lowercase letter", font=("Arial", 12), bg="#2b2f77", fg="#ffffff")
        self.lower_req.pack(anchor="w")
        self.digit_req = tk.Label(self.requirements_frame, text="At least one digit", font=("Arial", 12), bg="#2b2f77", fg="#ffffff")
        self.digit_req.pack(anchor="w")
        self.special_req = tk.Label(self.requirements_frame, text="At least one special character", font=("Arial", 12), bg="#2b2f77", fg="#ffffff")
        self.special_req.pack(anchor="w")

        # History Button
        self.history_button = tk.Button(
            self, text="View History", font=("Arial", 12), command=self.view_history, bg="#3f51b5", fg="#ffffff"
        )
        self.history_button.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 6:
                messagebox.showwarning("Warning", "Password length should be at least 6 characters for better security.")
                return
            characters = string.ascii_letters + string.digits
            if self.include_special.get():
                characters += string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(show="" if self.show_password.get() else "*")
            self.assess_strength(password)
            self.password_history.append(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def save_password(self):
        password = self.password_display.get()
        if password:
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")
            messagebox.showinfo("Saved", "Password saved to passwords.txt!")

    def assess_strength(self, password):
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        if length >= 12 and has_upper and has_lower and has_digit and has_special:
            strength = "Strong"
            color = "green"
            bar_length = 300
        elif length >= 8 and ((has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special)):
            strength = "Moderate"
            color = "orange"
            bar_length = 200
        else:
            strength = "Weak"
            color = "red"
            bar_length = 100
        self.strength_label.config(text=f"Password Strength: {strength}", fg=color)
        self.strength_meter.delete("all")
        self.strength_meter.create_rectangle(0, 0, bar_length, 20, fill=color)
        self.length_req.config(fg="green" if length >= 8 else "red")
        self.upper_req.config(fg="green" if has_upper else "red")
        self.lower_req.config(fg="green" if has_lower else "red")
        self.digit_req.config(fg="green" if has_digit else "red")
        self.special_req.config(fg="green" if has_special else "red")

    def toggle_password(self):
        if self.show_password.get():
            self.password_display.config(show="")
        else:
            self.password_display.config(show="*")

    def view_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("Password History")
        history_window.geometry("400x300")
        history_window.configure(bg="#2b2f77")
        history_text = scrolledtext.ScrolledText(history_window, font=("Arial", 12), width=50, height=15, fg="#000000", bg="#ffffff")
        history_text.pack(pady=10, padx=10)
        for index, password in enumerate(self.password_history, start=1):
            history_text.insert(tk.END, f"{index}. {password}\n")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
