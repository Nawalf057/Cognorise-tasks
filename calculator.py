import tkinter as tk
import math

class CustomCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Custom Calculator")
        self.geometry("350x500")
        self.resizable(False, False)
        self.configure(bg="#282828")
        self._create_widgets()

    def _create_widgets(self):
        self.display = tk.Entry(self, font=("Courier", 20, "bold"), borderwidth=5, relief=tk.SUNKEN, justify='right', fg="#00FF00", bg="#000000")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.display.insert(0, "0")

        buttons = [
            ('AC', 1, 0), ('←', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 1, 2), ('.', 5, 2), ('=', 5, 3)
        ]

        self.button_colors = {}

        for (text, row, col, *opt) in buttons:
            self._create_button(text, row, col, *opt)

        self._configure_grid()

    def _create_button(self, text, row, col, rowspan=1, colspan=1):
        button_color = self._get_button_color(text)
        button = tk.Button(
            self, text=text, font=("Courier", 16), borderwidth=5, relief=tk.RAISED,
            command=lambda t=text: self._on_button_click(t), bg=button_color, fg="#ffffff"
        )
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)
        self.button_colors[button] = button_color

    def _get_button_color(self, text):
        if text.isdigit() or text == '.':
            return "#4682B4"  # Different shade of blue
        elif text in ('=', '+', '-', '*', '/'):
            return "#8B0000"  # Dark red
        elif text == 'AC':
            return "#006400"  # Dark green
        elif text == '←':
            return "#FFD700"  # Gold
        elif text == '%':
            return "#800080"  # Purple
        else:
            return "#000000"  # Black

    def _configure_grid(self):
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def _on_button_click(self, char):
        if char == 'AC':
            self._clear_display()
        elif char == '←':
            self._backspace()
        elif char == '=':
            self._calculate_result()
        elif char == '%':
            self._calculate_percentage()
        else:
            self._append_to_display(char)

    def _clear_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def _backspace(self):
        current_text = self.display.get()
        if len(current_text) > 1:
            self.display.delete(len(current_text) - 1, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

    def _calculate_result(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def _calculate_percentage(self):
        try:
            number = float(self.display.get())
            result = number / 100
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def _append_to_display(self, char):
        current_text = self.display.get()
        if current_text == "0":
            self.display.delete(0, tk.END)
            self.display.insert(0, char)
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    calculator = CustomCalculator()
    calculator.mainloop()
