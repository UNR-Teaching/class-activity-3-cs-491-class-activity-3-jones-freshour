import unittest
import tictactoe


class TestInBounds(unittest.TestCase):
    def test_in_bounds_valid(self):
        board = tictactoe.Board()
        valid = board.in_bounds(0, 0)
        self.assertTrue(valid)
    
    def test_in_bounds_invalid_column(self):
        board = tictactoe.Board()
        valid = board.in_bounds(3, 0)
        self.assertFalse(valid)

    def test_in_bounds_invalid_row(self):
        board = tictactoe.Board()
        valid = board.in_bounds(0, 3)
        self.assertFalse(valid)

    def test_in_bounds_invalid_both(self):
        board = tictactoe.Board()
        valid = board.in_bounds(3, 3)
        self.assertFalse(valid)

    def test_in_bounds_invalid_too_small_column(self):
        board = tictactoe.Board()
        valid = board.in_bounds(-1, 0)
        self.assertFalse(valid)

    def test_in_bounds_invalid_too_small_row(self):
        board = tictactoe.Board()
        valid = board.in_bounds(0, -1)
        self.assertFalse(valid)

    def test_in_bounds_invalid_string_passed(self):
        board = tictactoe.Board()
        with self.assertRaises(TypeError):
            valid = board.in_bounds("5", 0)


class TestValidPlayer(unittest.TestCase):
    def test_player_valid_string_x(self):
        board = tictactoe.Board()
        valid = board.is_valid_player("X")
        self.assertTrue(valid)

    def test_player_valid_player_object(self):
        board = tictactoe.Board()
        valid = board.is_valid_player(board.player1)
        self.assertTrue(valid)

    def test_player_invalid_string_a(self):
        board = tictactoe.Board()
        valid = board.is_valid_player("A")
        self.assertFalse(valid)

    def test_player_invalid_number_1(self):
        board = tictactoe.Board()
        valid = board.is_valid_player(1)
        self.assertFalse(valid)


class TestMarkSquare(unittest.TestCase):
    def test_upper_left_player_1_marking(self):
        board = tictactoe.Board()
        valid = board.mark_square(0, 0, board.player1)
        self.assertEqual(board.board[0][0], "X")


class TestWinnerChecks(unittest.TestCase):
    def test_row_winner_player1(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 'X', 'X'],
            [0, 0, 0],
            [0, 0, 0]
        ]
        winner = board.winner_in_row()
        self.assertEqual(winner, board.player1)

    def test_row_no_winner(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 'O', 'X'],
            [0, 0, 0],
            [0, 0, 0]
        ]
        winner = board.winner_in_row()
        self.assertIsNone(winner)

    def test_column_winner_player1(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 0, 0],
            ['X', 0, 0],
            ['X', 0, 0]
        ]
        winner = board.winner_in_column()
        self.assertEqual(winner, board.player1)

    def test_column_no_winner(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 0, 0],
            ['O', 0, 0],
            ['X', 0, 0]
        ]
        winner = board.winner_in_column()
        self.assertIsNone(winner)

    def test_check_diag_left_diag_winner_player1(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 0, 0],
            [0, 'X', 0],
            [0, 0, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertEqual(winner, board.player1)

    def test_check_diag_left_diag_not_winner_player1(self):
        board = tictactoe.Board()
        board.board = [
            ['X', 0, 0],
            [0, 'O', 0],
            [0, 0, 'X']
        ]
        winner = board.check_diag(board.board, 3)
        self.assertIsNone(winner)

    def test_check_diag_right_diag_winner_player1(self):
        board = tictactoe.Board()
        board.board = [
            [0, 0, 'X'],
            [0, 'X', 0],
            ['X', 0, 0]
        ]
        reversed_board = board.board[::-1]
        winner = board.check_diag(reversed_board, 3)
        self.assertEqual(winner, board.player1)

    def test_check_diag_right_diag_no_winner_player1(self):
        board = tictactoe.Board()
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