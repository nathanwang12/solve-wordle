from collections import Counter

def check_guess(guess, word):
    '''determine result of guess on word'''
    letters = Counter(word)
    res = [None] * 5
    
    # check for correct letters in correct position + incorrect letters
    for i, char in enumerate(guess):
        if char == word[i]:
            res[i] = "G"
            letters[char] -= 1
        elif char not in word:
            res[i] = "B"
    
    # check for correct letters in incorrect position
    for i, char in enumerate(guess):
        if not res[i] and letters[char]:
            res[i] = "Y"
            letters[char] -= 1
        elif not res[i]:
            res[i] = "B"
    
    return "".join(res)

def filter_bank(word_bank, guess, result):
    '''possible answers must have same result as guess'''
    return [word for word in word_bank if check_guess(guess, word) == result]
