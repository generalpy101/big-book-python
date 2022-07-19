from random import randint
from typing import Optional
from pyfiglet import figlet_format

# section constants begin
MAX_TRIES = 10
MAX_DIGITS = 3
# section constants end

# Returns a random number as a string between a range
def get_random_number(begin: Optional[int] = 0, end: Optional[int] = 100) -> str:
    return str(randint(begin, end))

# Function for processing hints
def get_hints(secret: str, guess: str) -> str:
    clues_arr = []
    for i in range(MAX_DIGITS):
        if guess[i] == secret[i]:
            clues_arr.append("Fermi")
        elif guess[i] in secret:
            clues_arr.append("Pico")

    if len(clues_arr) == 0:
        return "Bagels"
    else:
        return " ".join(clues_arr)


def handle_result(secret: str, guess: str) -> str:
    if not guess.isdecimal():
        return f"Error!! {guess} is not a valid number"
    elif len(guess) != len(secret):
        return f"Error!! {guess}'s length is less than {MAX_DIGITS}"
    else:
        return get_hints(secret, guess)


def main():
    # For any number of digits, min value is 10 ^ (x - 1)
    # For max number, we calculate min value for digits one more than required
    # and then subtract 1 from it.
    _min = 10**(MAX_DIGITS - 1)
    _max = 10 ** (MAX_DIGITS) - 1
    s3cr3t = get_random_number(_min, _max)
    tries = MAX_TRIES

    try:
        while tries:
            user_input = input(
                f"Enter your guess ({tries} tr{'ies' if tries > 1 else 'y'} left) : ")

            if s3cr3t == user_input:
                print(f"\nCongratulations!! You won!")
                trophy = """  
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `'''''''`
          """
                print(trophy)
                exit(0)
            else:
                hint = handle_result(s3cr3t, user_input)
                print(hint)

            tries -= 1
        else:
            print(f"\nNo attempts left. The number was {s3cr3t}")
            print("Better luck next time :)")

    except KeyboardInterrupt:
        print("\nCtrl + C pressed, exiting...")
        print("Bye Bye!!")

    except Exception as e:
        print(e)


def print_intro():
    banner = figlet_format("B A G E L S")
    print(banner)

    info_text = f'''Welcome to Bagels!!

Bagles is a deductive logic game.
I will guess a {MAX_DIGITS} digit(s) number and you will have to guess that number.
But but but, here\'s the catch, you will only haver {MAX_TRIES} tries to guess so use them carefully.

I will also give you hints :)
    If your guess has correct digits at correct places, I\'ll say "Fermi" for each correct place
    If your guess has correct digits but at wrong places, I\'ll say "Pico" for each correct digit
    If both cases stated above fail, then I\'ll say "Bagels"

So you've got rules clear, let's start!!

I\'ve guessed a number...
'''
    print(info_text)


if __name__ == '__main__':
    print_intro()
    main()
