#!/bin/bash

commands=("ls" "pwd" "cd" "cp" "mv" "rm" "mkdir" "rmdir" "cat" "echo" "grep" "chmod" "man" "ps" "kill")

function print_header() {
    echo -e "\e[1;34m============================================\e[0m"
    echo -e "\e[1;34m        Linux Command Guessing Game\e[0m"
    echo -e "\e[1;34m============================================\e[0m"
}

function print_description() {
    local command="$1"
    echo -e "\nDescription: \e[1;33m${descriptions[$command]}\e[0m"
}

function print_feedback() {
    local feedback_color="$1"
    local feedback_message="$2"
    echo -e "\n\e[${feedback_color}m${feedback_message}\e[0m"
}

function play_game() {
    current_command=${commands[$((RANDOM % ${#commands[@]}))]}

    print_header
    echo -e "\nGuess the Linux command based on its description:"
    print_description "$current_command"
    
    read -p "Your guess: " user_guess

    if [[ "$user_guess" == "exit" ]]; then
        quit_game
    fi

    if [[ "$user_guess" == "$current_command" ]]; then
        print_feedback "1;32" "Congratulations! Your guess is correct."
    else
        print_feedback "1;31" "Oops! The correct command is '\e[1;37m$current_command\e[0m'."
    fi

    play_game
}

function quit_game() {
    print_header
    print_feedback "1;34" "Exiting the Linux Command Game. Goodbye!"
    echo -e "\e[1;34m============================================\e[0m"
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
