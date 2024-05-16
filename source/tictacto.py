import os
import time

from config import PLAYER_X, PLAYER_O, CURSOR, SPACE, TRIPLE_SPACE, BOARD
from ai import AI


class TicTacTo:

    def __init__(self):
        self.board_map = [False for _ in range(9)]  # board_map is a list of 9 fields, each field is either False or PLAYER_X or PLAYER_O
        self.current_field = 0  # current_field is the index of the field the cursor is currently on
        self.current_turn = PLAYER_X  # current_turn is the player who is currently at turn
        self.board = ''  # board is the current game board
        self.previous_board = ''  # previous_board is the previous game board
        self.running = True  # running is a boolean that indicates if the game is running
        self.with_ai = True

    def display_board(self):
        """
        Display the game board to the console.
        """
        self.construct_board()

        # if game not running display the board one last time
        if not self.running:
            print(self.board)
            return

        # check if it has changed, if so print it
        if self.board != self.previous_board:
            self.clear_console()
            self.previous_board = self.board
            print(self.board)

    def construct_board(self):
        """
        Construct the game board from the current game state.
        """

        # iterate over board_map and construct the board
        all_fields = []
        for idx, field in enumerate(self.board_map):
            if field:
                if idx == self.current_field:
                    new_field = f"{SPACE}{PLAYER_X}{CURSOR}" if field == PLAYER_X else f"{SPACE}{PLAYER_O}{CURSOR}"
                else:
                    new_field = f"{SPACE}{PLAYER_X}{SPACE}" if field == PLAYER_X else f"{SPACE}{PLAYER_O}{SPACE}"
                all_fields.append(new_field)
            else:
                if idx == self.current_field:
                    all_fields.append(f"{SPACE}{CURSOR}{SPACE}")
                else:
                    all_fields.append(TRIPLE_SPACE)

        self.board = BOARD.format(*all_fields)

    def evaluate_board(self) -> str | int:
        """
        Evaluate the current game board and return the result.
        :return: 0 if no one has won, PLAYER_X if player X has won, PLAYER_O if player O has won.
        """

        # Check rows for winning line
        for i in range(0, 9, 3):
            if self.board_map[i] == self.board_map[i + 1] == self.board_map[i + 2] is not False:
                return PLAYER_X if self.board_map[i] == PLAYER_X else PLAYER_O

        # Check columns for winning line
        for i in range(3):
            if self.board_map[i] == self.board_map[i + 3] == self.board_map[i + 6] is not False:
                return PLAYER_X if self.board_map[i] == PLAYER_X else PLAYER_O

        # Check diagonals for winning line
        if self.board_map[0] == self.board_map[4] == self.board_map[8] is not False:
            return PLAYER_X if self.board_map[0] == PLAYER_X else PLAYER_O
        if self.board_map[2] == self.board_map[4] == self.board_map[6] is not False:
            return PLAYER_X if self.board_map[2] == PLAYER_X else PLAYER_O

        # If no one has won, return 0
        return 0

    def are_fields_left(self) -> bool:
        """
        Check if there are any fields left on the game board.
        :return: True if there are fields left, False otherwise.
        """

        if not any(field is False for field in self.board_map):
            return False
        return True

    def flip_turn(self):
        """
        Flip the current turn to the other player.
        """

        self.current_turn = PLAYER_X if self.current_turn == PLAYER_O else PLAYER_O

    def place_char(self):
        """
        Place the current player's character on the current field.
        """

        index = self.current_field
        if not self.board_map[index]:
            # set field to current player at turn and then flip turn to other player
            self.board_map[index] = self.current_turn
            self.flip_turn()

    @staticmethod
    def clear_console():
        """
        Clear the console.
        """

        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        """
        Run the game loop.
        """

        ai = AI(self) if self.with_ai else None
        while self.running:
            board_eval = self.evaluate_board()

            # check conditions for game stop
            if not board_eval == 0:
                self.close()
                self.display_board()
                print(f"| {board_eval} | has won!")
                break
            if not self.are_fields_left():
                self.close()
                print('No one won!')
                break

            # if game is played with AI, let AI make a move
            if self.with_ai and self.current_turn == PLAYER_O:
                best_move = ai.make_move()
                self.current_field = best_move
                self.place_char()

            self.display_board()

    def close(self):
        """
        Close the game.
        """

        self.running = False
        self.clear_console()
