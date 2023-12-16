#!/bin/bash

commands=("ls" "pwd" "cd" "cp" "mv" "rm" "mkdir" "rmdir" "cat" "echo" "grep" "chmod" "man" "ps" "kill")

function print_styled_message() {
    local message="$1"
    echo -e "\e[1;34m$message\e[0m"
}

function play_game() {
    current_command=${commands[$((RANDOM % ${#commands[@]}))]}

    print_styled_message "Welcome to the Linux Command Game!"
    echo -e "Guess the Linux command based on its description:\n"
    echo -e "Description: ${descriptions[$current_command]}"
    
    read -p "Your guess: " user_guess

    if [[ "$user_guess" == "exit" ]]; then
        quit_game
    fi

    if [[ "$user_guess" == "$current_command" ]]; then
        print_styled_message "\nCongratulations! Your guess is correct."
    else
        print_styled_message "\nOops! The correct command is '\e[1;32m$current_command\e[0m'."
    fi

    play_game
}

function quit_game() {
    print_styled_message "Exiting the Linux Command Game. Goodbye!"
    exit 0
}

declare -A descriptions=(
    ["ls"]="List directory contents"
    ["pwd"]="Print working directory"
    ["cd"]="Change directory"
    ["cp"]="Copy files or directories"
    ["mv"]="Move or rename files or directories"
    ["rm"]="Remove files or directories"
    ["mkdir"]="Create a directory"
    ["rmdir"]="Remove an empty directory"
    ["cat"]="Concatenate and display the content of files"
    ["echo"]="Display a message or variable"
    ["grep"]="Search for a pattern in a file"
    ["chmod"]="Change file permissions"
    ["man"]="Display manual pages for a command"
    ["ps"]="List information about running processes"
    ["kill"]="Terminate or signal processes"
)

play_game
