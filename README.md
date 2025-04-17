# Rock-Paper-Scissors Game
A simple command-line implementation of the classic Rock-Paper-Scissors game.

## Introduction
Rock-Paper-Scissors is a classic hand game that is used to resolve disputes or just for fun. This project is a simple implementation of the game in Python, allowing you to play against the computer.

## Game Rules
1. You can choose between Rock, Paper, or Scissors.
2. The computer randomly selects one of these options.
3. The winner is determined based on the following rules:
    - Rock beats Scissors
    - Scissors beat Paper
    - Paper beats Rock
4. If both the player and the computer choose the same option, the game is a tie.
5. After playing 5 rounds (not counting ties) the final winner will be determined.

## How to Run
Tor run the game, follow these steps:
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to the main project directory.
```bash
cd Rock_paper_scissors
```
3. Add the current directory to the `PYTHONPATH` and run the `main.py` script.
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
4. Install any necessary dependencies:
```bash
pip install -r requirements.txt
```
