"""
File: hangman.py
Name: Tony
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    answer = random_word()
    ans = ""
    for i in range(len(answer)):
        ans += "_"
    head(answer)
    print("You have", str(N_TURNS), "guesses left.")
    guess(answer, ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def head(answer):
    ans = ""
    for i in range(len(answer)):
        ans += "_"
    print("The word looks like: ", str(ans))
    print(answer)
    return ans


def guess(answer, ans):
    # revised version
    chances = N_TURNS
    while True:
        if chances == 0:
            break
        elif ans.isalpha():
            break
        else:
            n = input("Your guess: ")
            n = n.upper()
            if not n.isalpha():
                print("illegal format.")
            elif len(n) != 1:
                print("illegal format.")
            elif answer.find(n) != -1:
                ans = replace(answer, ans, n)  # replace 完後直接用main的ans接
                print("You are correct!")
                if not ans.isalpha():
                    print("The Word looks like: ", ans)
                else:
                    print("You win!")
                    print("The Word was: ", ans)
            else:
                chances -= 1
                if chances > 0:
                    print("There is no", str(n), "'s in the word")
                    print("You have", str(chances), "guesses left.")
                elif chances == 0:
                    print("There is no", str(n), "'s in the word")
                    print("You are completely hung :(")


def replace(the_answer, empty_ans, word):
    # revised version(右邊是助教提醒)
    ans = ""
    i = the_answer.find(word)             # Bug: 這邊只會找到一個，若果answer是APPLE,那只會找到第一個P,第二個P不會被換到
    for i in range(len(the_answer)):      # 改用for loop，一個一個字母檢查
        ch = the_answer[i]
        if ch == word:
            ans += word
        else:
            ans += empty_ans[i]           # index對應舊answer的字母
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
