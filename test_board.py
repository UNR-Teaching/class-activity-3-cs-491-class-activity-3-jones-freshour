import unittest
from board import Board

class TestMarkSquare(unittest.TestCase):
    def test_upper_left_player_1_marking(self):
        board = Board()
        valid = board.mark_square(0, 0, 'X')
        self.assertEqual(board.board[0][0], 'X')

    def test_position_not_marked(self):
        board = Board()
        board.board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertFalse(board.positionAlreadyMarked(0, 2))

    def test_position_is_marked(self):
        board = Board()
        board.board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None]
        ]
        self.assertTrue(board.positionAlreadyMarked(0, 0))


class TestWinnerChecks(unittest.TestCase):
    def test_row_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None]
        ]
        winner = board.__winner_in_row__()
        self.assertEqual(winner, player1)

    def test_row_no_winner(self):
        board = Board()
        board.board = [
            ['X', 'O', 'X'],
            [None, None, None],
            [None, None, None]
        ]
        winner = board.__winner_in_row__()
        self.assertIsNone(winner)

    def test_column_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', None, None],
            ['X', None, None],
            ['X', None, None]
        ]
        winner = board.__winner_in_column__()
        self.assertEqual(winner, player1)

    def test_column_no_winner(self):
        board = Board()
        board.board = [
            ['X', None, None],
            ['O', None, None],
            ['X', None, None]
        ]
        winner = board.__winner_in_column__()
        self.assertIsNone(winner)

    def test_check_diag_left_diag_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            ['X', None, None],
            [None, 'X', None],
            [None, None, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertEqual(winner, player1)

    def test_check_diag_left_diag_not_winner_player1(self):
        board = Board()
        board.board = [
            ['X', None, None],
            [None, 'O', None],
            [None, None, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertIsNone(winner)

    def test_check_diag_right_diag_winner_player1(self):
        player1 = 'X'
        board = Board()
        board.board = [
            [None, None, 'X'],
            [None, 'X', None],
            ['X', None, None]
        ]
        reversed_board = board.board[::-1]
        winner = board.check_diag(reversed_board, 3)
        self.assertEqual(winner, player1)

    def test_check_diag_right_diag_no_winner_player1(self):
        board = Board()
        board.board = [
            [None, None, 'X'],
            [None, 'O', None],
            ['X', None, None]
        ]
        reversed_board = board.board[::-1]
        winner = board.check_diag(reversed_board, 3)
        self.assertIsNone(winner)

    def test_boardFull(self):
        board = Board()
        board.board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']
        ]
        
        self.assertTrue(board.__boardFull__())

if __name__ == "__main__":
    unittest.main()