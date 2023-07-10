from solver.interface import Game

def main():
    print("Beat Wordle with Nathan's Amazing Solver!")
    print("The solver will suggest a word to enter into Wordle.")
    print("Enter the result of your guess in the format (G/Y/B):")
    print("G = correct letter in correct position")
    print("Y = correct letter in incorrect position")
    print("B = incorrect letter")
    print("Good luck! (To quit, ctrl^c)")
    Game().solve()

if __name__ == "__main__":
    main()  