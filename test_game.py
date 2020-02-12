import unittest
import game, player, board


class TestGameCheckMove(unittest.TestCase):
    def test_check_move_valid(self):
        test_game = game.Game("Player1", "Player2")
        valid = test_game.check_move((0, 0), test_game.players[0])
        self.assertTrue(valid)

    def test_check_move_invalid(self):
        test_game = game.Game("Player1", "Player2")
        valid = test_game.check_move((0, 5), test_game.players[0])
        self.assertFalse(valid)


class TestGameEndGame(unittest.TestCase):
    def test_end_game_no_winner(self):
        test_game = game.Game("Player1", "Player2")
        winner = 'boardfull'
        win = test_game.end_game(winner)
        self.assertFalse(win)

    def test_end_game_winner(self):
        test_game = game.Game("Player1", "Player2")
        winner = test_game.players[0]
        win = test_game.end_game(winner)
        print(win)
        self.assertTrue(win)


class TestGameIsValidPlayer(unittest.TestCase):
    def test_player_is_valid(self):
        test_game = game.Game("Player1", "Player2")
        test_player = test_player.players[0]
        valid = test_game.is_valid_player(test_player)
        self.assertTrue(valid)

    def test_player_not_valid(self):
        test_game = game.Game("Player1", "Player2")
        test_player = player.Player("Player3", "Y")
        valid = test_game.is_valid_player(test_player)
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()