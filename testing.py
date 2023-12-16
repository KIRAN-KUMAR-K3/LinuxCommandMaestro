import random

# Dictionary of Linux commands and their descriptions
linux_commands = {
    'ls': 'List files and directories',
    'pwd': 'Print working directory',
    'cd': 'Change directory',
    'mkdir': 'Create a directory',
    'touch': 'Create an empty file',
    'cp': 'Copy files or directories',
    'mv': 'Move or rename files or directories',
    'rm': 'Remove files or directories',
    'cat': 'Concatenate and display the content of files',
    'grep': 'Search for a pattern in files',
    'ps': 'Display information about running processes',
    'chmod': 'Change file permissions',
    'df': 'Display disk space usage',
    'tar': 'Archive files',
    'find': 'Search for files and directories',
}

def ask_question():
    # Ask a random question about a Linux command
    correct_command = random.choice(list(linux_commands.keys()))

    # Generate choices with correct command
    choices = [linux_commands[correct_command]]
    while len(choices) < 4:
        random_command = random.choice(list(linux_commands.values()))
        if random_command not in choices:
            choices.append(random_command)

    # Shuffle choices
    random.shuffle(choices)

    print(f"\nWhat does the command '{correct_command}' do?\n")

    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    try:
        user_answer = int(input("Your choice (1-4): ").strip())
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return False

    if user_answer == 0:
        print("Exiting the quiz. Goodbye!")
        return True

    # Find the index of the correct command in the shuffled choices
    correct_position = choices.index(linux_commands[correct_command]) + 1

    if user_answer == correct_position:
        print("Correct! Well done!\n")
    else:
        print(f"Incorrect. The correct answer is: {correct_position}. {linux_commands[correct_command]}\n")

    return False

if __name__ == "__main__":
    print("Welcome to the Linux Command Quiz!")
    print("Guess the Linux command based on its description.")
    print("Enter the number corresponding to your choice.")
    print("Enter '0' to exit the quiz.\n")

    while not ask_question():
        pass
