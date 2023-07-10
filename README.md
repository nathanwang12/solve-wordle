# Wordle Solver

## Running the program

After cloning the repository, run the following command in the terminal (assuming you have Python 3 installed):

```bash
python3 run.py
```

## How it works

The bot will prompt you for your initial guess. Please enter it as a string of five lower case letters. Enter this same guess into Wordle; the bot will then prompt you for the result of this guess under the format (G/Y/B): (G) for correct letter, correct position, (Y) for correct letter, wrong position, and (B) for incorrect letter. Please enter when prompted; the bot will then compute a new guess and repeat the process until the word is solved (or it loses).

Good luck!