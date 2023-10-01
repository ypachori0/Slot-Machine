#importing modules
import random

#global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
#the rarer the symbol is, the higher the multiplyer
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#checks to see if there is a 3 in a row and also checks what the symbol is so that a multiplyer can be applied
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #if the symbols do not match in the row, we break out of the loop and check the next row
                break
        else: #if there are no breaks, then that means user won and we apply the multiplyer. what they won is the multiplyer for the symbol times their bet
            winnings += values[symbol] * bet #bet on the line, not the total bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#loop through every row that we have. for every row, we loop through every column. for every column, we only print the current row that we're on
def print_slot_machine(columns): #transposes column matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #loops through all the items in column; enumerate gives index as well as item in column
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="") #don't want the pipe operator for last column so this is just saying that if this is the last column then don't put the "|"

        print()


#collects user input to get deposit
def deposit():
    while True: #using while loop bc i will continually ask the user to enter a deposit amount until a valid amount has been entered
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #if you convert before checking, it could cause an error
            amount = int(amount) #converts string to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True: #using while loop bc i will continually ask the user to enter a deposit amount until a valid amount has been entered
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #adding MAX_LINES into statement and converting from it to string
        if lines.isdigit(): #if you convert before checking, it could cause an error
            lines = int(lines) #converts string to int
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True: #using while loop bc i will continually ask the user to enter a deposit amount until a valid amount has been entered
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #if you convert before checking, it could cause an error
            amount = int(amount) #converts string to int
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break



    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winning_lines) #the splat/unpack operator, passes every single line from winning_lines to this print function. if we have lines 1 and 2, it will pass lines 1 and 2 and say "you won on lines 1 and 2"
    return winnings - total_bet
#main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()