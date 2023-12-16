import tkinter as tk
from tkinter import messagebox
import random

class LinuxCommandGame:
    def __init__(self):
        self.commands = {
            'ls': 'List directory contents',
            'pwd': 'Print working directory',
            'cd': 'Change directory',
            'cp': 'Copy files or directories',
            'mv': 'Move or rename files or directories',
            'rm': 'Remove files or directories',
            'mkdir': 'Create a directory',
            'rmdir': 'Remove an empty directory',
            'cat': 'Concatenate and display the content of files',
            'echo': 'Display a message or variable',
            'grep': 'Search for a pattern in a file',
            'chmod': 'Change file permissions',
            'man': 'Display manual pages for a command',
            'ps': 'List information about running processes',
            'kill': 'Terminate or signal processes',
        }

        self.window = tk.Tk()
        self.window.title("Linux Command Game")

        self.description_label = tk.Label(self.window, text="Welcome to the Linux Command Game!\nGuess the Linux command based on its description.")
        self.description_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.window, width=30)
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.quit_button = tk.Button(self.window, text="Quit Game", command=self.quit_game)
        self.quit_button.pack(pady=10)

        self.play_game()

    def get_random_command(self):
        return random.choice(list(self.commands.keys()))

    def play_game(self):
        self.current_command = self.get_random_command()
        self.description_label.config(text=f"Description: {self.commands[self.current_command]}")

    def check_guess(self):
        user_guess = self.guess_entry.get().strip().lower()

        if user_guess == 'exit':
            self.quit_game()

        if user_guess == self.current_command:
            messagebox.showinfo("Correct", "Congratulations! Your guess is correct.")
        else:
            messagebox.showerror("Incorrect", f"Oops! The correct command is '{self.current_command}'.")

        self.play_game()
        self.guess_entry.delete(0, tk.END)

    def quit_game(self):
        self.window.destroy()

if __name__ == "__main__":
    game = LinuxCommandGame()
    game.window.mainloop()
