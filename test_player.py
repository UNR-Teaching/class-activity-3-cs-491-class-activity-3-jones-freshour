import unittest
import player

class TestPlayerConstruction(unittest.TestCase):
    def test_constructor_name(self):
        test_player = player.Player("Player1", "X")
        self.assertEqual(test_player.name, "Player1")

    def test_constructor_symbol(self):
        test_player = player.Player("Player1", "X")
        self.assertEqual(test_player.symbol, "X")

if __name__ == "__main__":
    unittest.main()
