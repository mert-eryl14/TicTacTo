from config import PLAYER_X, PLAYER_O


class AI:
    def __init__(self, game):
        self.game = game

    def make_move(self):
        """
        Makes a move for the AI player using the minimax algorithm.
        """
        best_score = float('-inf')
        best_move = None

        for i in range(9):
            if self.game.board_map[i] is False:
                self.game.board_map[i] = self.game.current_turn
                score = self.minimax(self.game.board_map, 0, False)
                self.game.board_map[i] = False  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board: list, depth: int, is_maximizing: bool):
        """
        Implementation of the minimax algorithm.
        """

        result = self.game.evaluate_board()

        if result != 0:
            return 10 - depth if result == self.game.current_turn else depth - 10

        if not self.game.are_fields_left():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] is False:
                    board[i] = self.game.current_turn
                    score = self.minimax(board, depth + 1, False)
                    board[i] = False
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            opponent = PLAYER_X if self.game.current_turn == PLAYER_O else PLAYER_O
            for i in range(9):
                if board[i] is False:
                    board[i] = opponent
                    score = self.minimax(board, depth + 1, True)
                    board[i] = False
                    best_score = min(score, best_score)
            return best_score
