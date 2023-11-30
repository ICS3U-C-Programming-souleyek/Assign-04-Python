#!/usr/bin/env python3

# Created by: souleye keita
# Created on: nov. 28, 2023
# this program gets total even and odd intergers entered


def main():
    print("Welcome to Evens and Odds Total. This will display the total evens and odds number that you entered.")
    evens_total = 0
    odds_total = 0
    while True:
        user_respond = input("Enter an integer (or q to quit): ")
        if user_respond.lower() == "q":
            print(
                f"You entered {evens_total} even numbers and {odds_total} odd numbers."
            )
            break
        try:
            user_respond = int(user_respond)
        except ValueError:
            print(f"{user_respond} is not an integer. ", end="")
        else:
            if user_respond % 2 == 0:
                evens_total += 1
            else:
                odds_total += 1


if __name__ == "__main__":
    main()
