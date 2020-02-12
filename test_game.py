import unittest
import game, player, board


class TestGameRun(unittest.TestCase):
    def test_run_no_winner(self):
        # test_game = game.Game("Player1", "Player2")
        # winner = test_game.run()
        winner = None
        self.assertIsNone(winner)


class TestGameCheckMove(unittest.TestCase):
    def test_check_move_valid(self):
        pass

    def test_check_move_invalid(self):
        pass


class TestGameEndGame(unittest.TestCase):
    def test_end_game_no_winner(self):
        pass

    def test_end_game_winner(self):
        pass


class TestGameIsValidPlayer(unittest.TestCase):
    def test_player_is_valid(self):
        pass

    def test_player_not_valid(self):
        pass


if __name__ == "__main__":
    unittest.main()