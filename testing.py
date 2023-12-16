import random
from colorama import Fore, Style

commands = ["ls", "pwd", "cd", "cp", "mv", "rm", "mkdir", "rmdir", "cat", "echo", "grep", "chmod", "man", "ps", "kill"]

descriptions = {
    "ls": "List directory contents",
    "pwd": "Print working directory",
    "cd": "Change directory",
    "cp": "Copy files or directories",
    "mv": "Move or rename files or directories",
    "rm": "Remove files or directories",
    "mkdir": "Create a directory",
    "rmdir": "Remove an empty directory",
    "cat": "Concatenate and display the content of files",
    "echo": "Display a message or variable",
    "grep": "Search for a pattern in a file",
    "chmod": "Change file permissions",
    "man": "Display manual pages for a command",
    "ps": "List information about running processes",
    "kill": "Terminate or signal processes",
}

def print_header():
    print(Fore.CYAN + "=" * 44)
    print("        Linux Command MCQ Quiz")
    print("=" * 44 + Style.RESET_ALL)

def print_question(correct_command):
    correct_description = descriptions[correct_command]

    # Generate three random commands excluding the correct one
    options = random.sample([cmd for cmd in commands if cmd != correct_command], 3)
    options.append(correct_command)

    # Shuffle the options randomly
    random.shuffle(options)

    print(f"\nWhat does the command '{correct_command}' do?\n")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {Fore.GREEN}{descriptions[option]}{Style.RESET_ALL}")

    return options.index(correct_command) + 1

def play_game():
    current_command = random.choice(commands)

    print_header()
    correct_position = print_question(current_command)

    user_choice = input("Your choice (1-4): ").strip()

    if user_choice.lower() == 'exit':
        quit_game()

    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    if user_choice == correct_position:
        print("\n" + Fore.GREEN + "Congratulations! Your answer is correct." + Style.RESET_ALL)
    else:
        print(f"\n{Fore.RED}Oops! That's incorrect. The correct answer is option {correct_position}.{Style.RESET_ALL}")

    play_game()

def quit_game():
    print_header()
    print("\n" + Fore.CYAN + "Exiting the Linux Command MCQ Quiz. Goodbye!" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 44 + Style.RESET_ALL)
    exit(0)

if __name__ == "__main__":
    play_game()
