import unittest
from board import Board

class TestMarkSquare(unittest.TestCase):
    def test_upper_left_player_1_marking(self):
        board = Board()
        valid = board.mark_square(0, 0, 'X')
        self.assertEqual(board.board[0][0], "X")


class TestWinnerChecks(unittest.TestCase):
    def test_row_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', 'X', 'X'],
            [0, 0, 0],
            [0, 0, 0]
        ]
        winner = board.winner_in_row()
        self.assertEqual(winner, player1)

    def test_row_no_winner(self):
        board = Board()
        board.board = [
            ['X', 'O', 'X'],
            [0, 0, 0],
            [0, 0, 0]
        ]
        winner = board.winner_in_row()
        self.assertIsNone(winner)

    def test_column_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', 0, 0],
            ['X', 0, 0],
            ['X', 0, 0]
        ]
        winner = board.winner_in_column()
        self.assertEqual(winner, player1)

    def test_column_no_winner(self):
        board = Board()
        board.board = [
            ['X', 0, 0],
            ['O', 0, 0],
            ['X', 0, 0]
        ]
        winner = board.winner_in_column()
        self.assertIsNone(winner)

    def test_check_diag_left_diag_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', 0, 0],
            [0, 'X', 0],
            [0, 0, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertEqual(winner, player1)

    def test_check_diag_left_diag_not_winner_player1(self):
        board = Board()
        board.board = [
            ['X', 0, 0],
            [0, 'O', 0],
            [0, 0, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertIsNone(winner)

    def test_check_diag_right_diag_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            [0, 0, 'X'],
            [0, 'X', 0],
            ['X', 0, 0]
        ]
        reversed_board = board.board[::-1]
        winner = board.check_diag(reversed_board, 3)
        self.assertEqual(winner, player1)

    def test_check_diag_right_diag_no_winner_player1(self):
        board = Board()
        board.board = [
            [0, 0, 'X'],
            [0, 'O', 0],
            ['X', 0, 0]
        ]
        reversed_board = board.board[::-1]
        winner = board.check_diag(reversed_board, 3)
        self.assertIsNone(winner)


if __name__ == "__main__":
    unittest.main()