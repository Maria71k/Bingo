import random

class Bingo:
    def __init__(self):
        self.numbers = random.sample(range(1, 91), 90)
        self.player_card = random.sample(range(1, 91), 15)
        self.computer_card = random.sample(range(1, 91), 15)
        self.called_numbers = []

    def print_card(self, card):
        print("   B   I   N   G   O")
        for i in range(0, 15, 5):
            print(f"{card[i]:3} {card[i+1]:3} {card[i+2]:3} {card[i+3]:3} {card[i+4]:3}")

    def play(self):
        print("Welcome to Bingo!\n")
        print("Your Bingo card:")
        self.print_card(self.player_card)
        print("\nComputer's Bingo card:")
        self.print_card(self.computer_card)
        print("\nLet's play!\n")

        while True:
            called_number = self.numbers.pop()
            self.called_numbers.append(called_number)
            print(f"Called number: {called_number}")
            if called_number in self.player_card:
                self.player_card[self.player_card.index(called_number)] = 'X'
                print("You have this number on your card!")
                self.print_card(self.player_card)
            if called_number in self.computer_card:
                self.computer_card[self.computer_card.index(called_number)] = 'X'
                print("Computer has this number on its card!")
                self.print_card(self.computer_card)

            if self.check_winner(self.player_card):
                print("Congratulations! You won!")
                break
            if self.check_winner(self.computer_card):
                print("Computer wins!")
                break

    def check_winner(self, card):
        rows = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [0, 5, 10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [0, 6, 12], [4, 6, 8]]
        for row in rows:
            if all(card[i] == 'X' for i in row):
                return True
        return False

if __name__ == "__main__":
    bingo = Bingo()
    bingo.play()
