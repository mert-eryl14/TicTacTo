import keyboard
from tictacto import TicTacTo
from config import PLAYER_X, PLAYER_O

# init game
game = TicTacTo()


# setup events for keyboard presses
def process_keypress(key):
    # block input if AI is activated and it's the AI's turn
    if game.with_ai:
        if game.current_turn == PLAYER_O:
            return

    f = game.current_field
    # go up
    if key.name == 'w' and 0 <= (f - 3) <= 8:
        game.current_field -= 3
    # go down
    if key.name == 's' and 0 <= (f + 3) <= 8:
        game.current_field += 3
    # go left
    if key.name == 'a' and 0 <= (f - 1) <= 8:
        game.current_field -= 1
    # go right
    if key.name == 'd' and 0 <= (f + 1) <= 8:
        game.current_field += 1
    # flip turn
    if key.name == 'enter':
        game.place_char()


if __name__ == '__main__':
    # clear console and ask user if they want to play against AI
    game.clear_console()
    game.with_ai = True if input("Do you want to play against AI? (y/n): ") == 'y' else False

    # setup callback function on any keypress
    keyboard.on_press(process_keypress)

    # run game loop
    game.run()
