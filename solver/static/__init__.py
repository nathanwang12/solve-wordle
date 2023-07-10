from pathlib import Path

LIST_DIR = Path(__file__).parent

with open(LIST_DIR / 'answers.txt') as f:
    ANSWERS = [w.strip() for w in f.readlines()]

with open(LIST_DIR / 'guesses.txt') as f:
    GUESSES = [w.strip() for w in f.readlines()]

ANSWER_BANK = ANSWERS
GUESS_BANK = GUESSES
