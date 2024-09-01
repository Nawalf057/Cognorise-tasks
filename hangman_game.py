import tkinter as tk
from tkinter import messagebox
import random

# Word list for the game
words = ['python', 'hangman', 'challenge', 'programming', 'developer']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")  # Light grey background

        self.word = random.choice(words).upper()
        self.word_set = set(self.word)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        
        self.display_word = ['_' if letter != ' ' else ' ' for letter in self.word]
        
        self.create_widgets()
        self.update_display_word()
        self.update_hangman_display()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=('Helvetica', 24, 'bold'), bg="#ffcc00", fg="#000000")
        self.title_label.pack(pady=10, fill=tk.X)
        
        self.word_label = tk.Label(self.root, text=' '.join(self.display_word), font=('Helvetica', 20), bg="#f5f5f5", fg="#000000")
        self.word_label.pack(pady=20)
        
        self.hangman_canvas = tk.Canvas(self.root, width=200, height=200, bg="#ffffff", highlightthickness=0)
        self.hangman_canvas.pack(pady=20)
        
        self.entry = tk.Entry(self.root, font=('Helvetica', 20))
        self.entry.pack(pady=10)
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, font=('Helvetica', 15), bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)
        self.guess_button.pack(pady=10)
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=('Helvetica', 15), bg="#FFC107", fg="#000000", relief=tk.RAISED)
        self.restart_button.pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="", font=('Helvetica', 15), bg="#f5f5f5", fg="#000000")
        self.status_label.pack(pady=10)

    def update_display_word(self):
        self.word_label.config(text=' '.join(self.display_word))

    def update_hangman_display(self):
        self.hangman_canvas.delete("all")
        stages = [
            '''
             ------
             |    |
             |    
             |   
             |   
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |   
             |   
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |    |
             |   
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |   /|
             |   
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |   /|\\
             |   
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |   /|\\
             |   /
             |   
            ------
            ''',
            '''
             ------
             |    |
             |    O
             |   /|\\
             |   / \\
             |   
            ------
            '''
        ]
        stage = stages[self.incorrect_guesses]
        self.hangman_canvas.create_text(100, 100, text=stage, font=('Courier', 10), fill='black')

    def check_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Repeated Guess", "You already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[index] = guess
            self.update_display_word()
            if set(self.display_word) == self.word_set:
                messagebox.showinfo("Congratulations!", "You've guessed the word!")
                self.status_label.config(text="Congratulations! You've guessed the word!", fg="#4CAF50")
        else:
            self.incorrect_guesses += 1
            self.update_hangman_display()
            if self.incorrect_guesses == self.max_incorrect_guesses:
                messagebox.showinfo("Game Over", f"The word was: {self.word}")
                self.status_label.config(text=f"Game Over! The word was: {self.word}", fg="#FF5722")
                
    def restart_game(self):
        self.word = random.choice(words).upper()
        self.word_set = set(self.word)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        
        self.display_word = ['_' if letter != ' ' else ' ' for letter in self.word]
        
        self.update_display_word()
        self.update_hangman_display()
        self.status_label.config(text="", fg="#000000")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
