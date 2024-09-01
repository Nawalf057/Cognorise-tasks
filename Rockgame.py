import tkinter as tk
from PIL import Image, ImageTk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        # Load background image
        self.bg_image = Image.open("self.jpg")  # Replace with your background image path
        self.bg_image = self.bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label for the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.user_score = 0
        self.computer_score = 0

        # Load images for Rock, Paper, Scissors
        self.rock_img = self.load_image("rock.png")
        self.paper_img = self.load_image("paper.png")
        self.scissors_img = self.load_image("secci.png")

        # Create widgets
        self._create_widgets()

    def load_image(self, filepath):
        """Load and resize an image to 120x120 pixels."""
        image = Image.open(filepath)
        image = image.resize((120, 120), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    def _create_widgets(self):
        # Labels for the images
        self.rock_label = tk.Label(self.root, image=self.rock_img, bg="white")
        self.paper_label = tk.Label(self.root, image=self.paper_img, bg="white")
        self.scissors_label = tk.Label(self.root, image=self.scissors_img, bg="white")

        self.rock_label.grid(row=0, column=0, padx=10, pady=10)
        self.paper_label.grid(row=0, column=1, padx=10, pady=10)
        self.scissors_label.grid(row=0, column=2, padx=10, pady=10)

        # Buttons for selecting Rock, Paper, Scissors
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("Rock"), 
                                     font=("Arial", 12), bg="#ff6347", fg="white", width=10)
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper"), 
                                      font=("Arial", 12), bg="#4682b4", fg="white", width=10)
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors"), 
                                         font=("Arial", 12), bg="#32cd32", fg="white", width=10)

        self.rock_button.grid(row=1, column=0, padx=10, pady=10)
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)

        # Label to show the result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16), bg="#f0f8ff")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10)

        # Labels to show the scores
        self.score_label = tk.Label(self.root, text="Scores", font=("Arial", 14, "bold"), bg="#f0f8ff")
        self.score_label.grid(row=3, column=0, columnspan=3)

        self.user_score_label = tk.Label(self.root, text=f"Your Score: {self.user_score}", font=("Arial", 12), bg="#f0f8ff")
        self.user_score_label.grid(row=4, column=0, padx=10, pady=5)

        self.computer_score_label = tk.Label(self.root, text=f"Computer Score: {self.computer_score}", font=("Arial", 12), bg="#f0f8ff")
        self.computer_score_label.grid(row=4, column=2, padx=10, pady=5)

    def play(self, user_choice):
        """Play the game with the user's choice and update the score."""
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}. {result}")
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  # Adjust the window size to fit the background image
    game = RockPaperScissors(root)
    root.mainloop()
