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

    def get_random_command(self):
        return random.choice(list(self.commands.keys()))

    def play_game(self):
        print("Welcome to the Linux Command Game!")
        print("Guess the Linux command based on its description.")
        print("Type 'exit' to quit the game.\n")

        while True:
            command = self.get_random_command()
            description = self.commands[command]

            print(f"Description: {description}")
            user_guess = input("Your guess: ").strip().lower()

            if user_guess == 'exit':
                print("Thanks for playing! Exiting the game.")
                break

            if user_guess == command:
                print("Correct!\n")
            else:
                print(f"Incorrect. The correct command is '{command}'.\n")

if __name__ == "__main__":
    game = LinuxCommandGame()
    game.play_game()
