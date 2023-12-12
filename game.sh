#!/bin/bash

commands=("ls" "pwd" "cd" "cp" "mv" "rm" "mkdir" "rmdir" "cat" "echo" "grep" "chmod" "man" "ps" "kill")

function play_game() {
    local random_command=${commands[$((RANDOM % ${#commands[@]}))]}
    local description=$(grep -oP "(?<=^$random_command': ').*" "$0")  # Extract description from the script

    user_guess=$(zenity --entry --title="Linux Command Game" --text="Guess the Linux command based on its description:\n\n$description" --width=400)

    if [ "$user_guess" == "exit" ]; then
        zenity --info --title="Linux Command Game" --text="Thanks for playing! Exiting the game."
        exit 0
    fi

    if [ "$user_guess" == "$random_command" ]; then
        zenity --info --title="Correct" --text="Congratulations! Your guess is correct."
    else
        zenity --error --title="Incorrect" --text="Oops! The correct command is '$random_command'."
    fi

    play_game
}

zenity --info --title="Linux Command Game" --text="Welcome to the Linux Command Game!\nGuess the Linux command based on its description." --width=300

play_game
