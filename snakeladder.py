import random

# Define the game board with snakes and ladders
snake_and_ladder = {
    2: 38, 7: 14, 8: 31, 16: 6, 15: 26, 18: 12, 24: 16, 28: 84, 36: 44,
    46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80
}

# Initialize player positions
player_positions = {
    "Player 1": 0,
    "Player 2": 0
}

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to move a player on the board
def move_player(player, steps):
    player_positions[player] += steps
    if player_positions[player] in snake_and_ladder:
        player_positions[player] = snake_and_ladder[player_positions[player]]

# Function to check if a player has won
def has_won(player):
    return player_positions[player] >= 100

# Main game loop
current_player = "Player 1"

while True:
    input(f"{current_player}, press Enter to roll the die...")
    steps = roll_die()
    print(f"{current_player} rolled a {steps}.")
    
    move_player(current_player, steps)

    if has_won(current_player):
        print(f"{current_player} has won!")
        break

    print(f"{current_player} is now at position {player_positions[current_player]}.\n")

    # Switch to the other player
    current_player = "Player 1" if current_player == "Player 2" else "Player 2"
