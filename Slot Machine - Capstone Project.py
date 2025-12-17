import random


def spin_slot():
    symbols = ["A", "B", "C", "7"]

    first = random.choice(symbols)
    second = random.choice(symbols)
    third = random.choice(symbols)

    return first, second, third


def check_win(a, b, c, bet):
    winnings = 0

    if a == b and b == c:
        if a == "7":
            winnings = bet * 10
        elif a == "C":
            winnings = bet * 5
        else:
            winnings = bet * 3
        print("JACKPOT!")

    elif a == b or b == c or a == c:
        winnings = bet * 2
        print("Small win!")

    else:
        print("No match.")

    return winnings


def play_round(balance, round_number):
    print("\n--- Round", round_number, "---")
    print("Current balance:", balance)

    bet = int(input("Enter bet amount: "))

    if bet <= 0:
        print("Invalid bet. Round skipped.")
        return balance

    if bet > balance:
        print("Not enough money to play this round.")
        return balance

    balance = balance - bet
    print("Spinning...")

    a, b, c = spin_slot()
    print("[", a, "|", b, "|", c, "]")

    winnings = check_win(a, b, c, bet)
    balance = balance + winnings

    if winnings > 0:
        print("You won:", winnings)
    else:
        print("You lost your bet.")

    print("Balance after round:", balance)
    return balance


def main():
    starting_balance = 100
    balance = starting_balance

    print("Welcome to the 3-Round Slot Machine!")
    print("Starting balance:", balance)

    round_number = 1

    while round_number <= 3:
        if balance <= 0:
            print("\nYou have run out of money.")
            break

        balance = play_round(balance, round_number)

        if balance <= 0:
            print("\nYou do not have enough money to continue.")
            break

        round_number = round_number + 1

    total_winnings = balance - starting_balance

    print("\n--- Game Over ---")
    print("Starting balance:", starting_balance)
    print("Final balance:", balance)

    if total_winnings > 0:
        print("Total winnings:", total_winnings)
    elif total_winnings < 0:
        print("Total loss:", total_winnings)
    else:
        print("You broke even.")


main()
