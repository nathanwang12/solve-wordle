from .check import check_guess, filter_bank

class SmartAlgo:

    @classmethod
    def make_guess(cls, answer_bank, guess_bank=None):
        '''determine best guess dependent on size and content of answer_bank'''
        print("Making Guess...")

        # when answer_bank small, advantageous to make "wrong" guesses for info
        word_bank = cls.select_bank(answer_bank, guess_bank)
        guess = None
        words_left = len(word_bank)
        guess_worst_case = words_left + 1
        lowest_total = words_left * words_left

        for word in word_bank:
            # avoid words with double letters when answer_bank large
            if len(answer_bank) >= 1000 and len(set(word)) < 5:
                continue

            worst_case, total = cls.grade_guess(word, answer_bank, lowest_total)

            # avg num words left improves
            if total < lowest_total:
                lowest_total = total
                guess_worst_case = worst_case
                guess = word
            
            # in event of tie, choose word with best (lowest) worst case
            elif total == lowest_total and worst_case < guess_worst_case:
                lowest_total = total
                guess_worst_case = worst_case
                guess = word

        return guess

    @classmethod
    def grade_guess(cls, guess, answer_bank, lowest_total=None):
        '''determine worst case and avg (total) outcome of guess'''
        # highest potential number of words left in answer_bank
        worst_case = 0
        # total number of words left in answer_bank (i.e. avg)
        total = 0

        for word in answer_bank:
            res = check_guess(guess, word)

            if res == 'GGGGG':
                continue
            
            # num words left in answer_bank after guess
            words_left = len(filter_bank(answer_bank, guess, res))
            total += words_left
            worst_case = max(worst_case, words_left)

            # worse then current best
            if lowest_total and total > lowest_total:
                break

        return worst_case, total

    @classmethod     
    def select_bank(cls, answer_bank, guess_bank):
        '''determine word_bank to use for guessing'''
        # if answer_bank is small, use guess_bank to gain more info
        if len(answer_bank) <= 50 and guess_bank:
            return guess_bank
        
        return answer_bank

        