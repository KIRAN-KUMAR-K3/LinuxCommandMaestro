#!/bin/bash

commands=("ls" "pwd" "cd" "cp" "mv" "rm" "mkdir" "rmdir" "cat" "echo" "grep" "chmod" "man" "ps" "kill")

score=0
level=1

function display_intro() {
    clear
    echo -e "\e[1;36mWelcome to the Linux Command Game!\e[0m"
    echo -e "\e[1;33mGuess the Linux command based on its description.\e[0m"
    echo -e "\e[1;32mType 'exit' to quit the game.\e[0m"
    echo
}

function display_score() {
    echo -e "\e[1;35mScore: $score\e[0m"
    echo -e "\e[1;35mLevel: $level\e[0m"
}

function play_game() {
    local random_command=${commands[$((RANDOM % ${#commands[@]}))]}
    local description=$(grep -oP "(?<=^$random_command': ').*" "$0")  # Extract description from the script

    echo -e "\e[1;34mDescription: $description\e[0m"
    user_guess=""
    
    read -p "Your guess: " user_guess

    if [ "$user_guess" == "exit" ]; then
        echo -e "\e[1;36mThanks for playing! Exiting the game.\e[0m"
        exit 0
    fi

    if [ "$user_guess" == "$random_command" ]; then
        echo -e "\e[1;32mCorrect!\e[0m"
        ((score++))
    else
        echo -e "\e[1;31mIncorrect. The correct command is '$random_command'.\e[0m"
    fi

    if [ "$score" -ge $((level * 3)) ]; then
        ((level++))
        echo -e "\e[1;33mCongratulations! You've advanced to level $level.\e[0m"
    fi

    display_score
    read -n 1 -s -r -p "Press any key to continue..."
}

display_intro
display_score

while true; do
    play_game
done
