import board, player


class Game:
    def __init__(self, p1_name, p2_name):
        board = board.Board()
        players = [
            player.Player(p1_name, "X"),
            player.Player(p2_name, "O")
        ]

    def play(self):
        winner = None
        while not winner:
            winner = self.__run()
        self.end_game(winner)

    def run(self):
        winner = self.run_player(self.players[0])
        if not winner:
            winner = self.run_player(self.players[1])
        return winner
    
    def run_player(self, player):
        self.board.draw_board()
        while not self.check_move(player):
            pass
        return self.board.check_for_winner()

    def check_move(self, player):
        move = self.get_move(player)
        if not self.board.mark_square(move[0], move[1], player.symbol):
            print("Invalid move, try again...")
            return False
        return True
            
    def end_game(self, winner):
        if winner in self.players:
            print(f"{winner.name} has won the game!")
        else:
            print("Cat's game...")
            
    def get_move(self, player):
        move = input(f"{player.name}'s turn: enter your move (x, y): ")
        return move

    def is_valid_player(self, player):
        return player in (self.player1, self.player2)
    