from copy import deepcopy
from solver.logic.smart import SmartAlgo
from solver.logic.check import filter_bank
from solver.static import ANSWER_BANK, GUESS_BANK
import re

class Game():
    answer_bank = ANSWER_BANK
    guess_bank = GUESS_BANK

    def solve(self):
        answer_bank = deepcopy(self.answer_bank)

        # get initial guess
        guess = self.get_guess()

        while True:
            if not answer_bank:
                print("No Words Left in Word Bank. Better Luck Next Time.")
                return
            
            result = self.get_result()

            if result == "GGGGG":
                print("WINNER WINNER CHICKEN DINNER")
                return
            
            answer_bank = filter_bank(answer_bank, guess, result)

            if len(answer_bank) == 1:
                print(f"Answer: {answer_bank[0]}")
                print("WINNER WINNER CHICKEN DINNER")
                return

            guess = SmartAlgo.make_guess(answer_bank, self.guess_bank)
            print(f"Recommended Guess: {guess}")

    def get_guess(self):
        '''prompt user for initial guess'''
        res = input("Enter Guess: ")
        format = re.match(r"^[a-z]{5}$", res)

        # check for valid input
        if not format:
            print("Invalid input: please check syntax")
            return self.get_guess()
        
        return res
        
    def get_result(self):
        '''prompt user for result of guess'''
        res = input("Enter Result: (G/Y/B) ")
        format = re.match(r"^[GYB]{5}$", res)

        # check for valid input
        if not format:
            print("Invalid input: please check syntax")
            return self.get_result()
        
        return res
        



