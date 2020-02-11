class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """

        self.player1 = "X"
        self.player2 = "O"
        self.board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]

    def draw_board(self):
        for row in self.board:
            print(row)

    # Functions to check validity of input

    @staticmethod
    def in_bounds(column, row):
        return 0 <= column < 3 and 0 <= row < 3

    def is_valid_player(self, player):
        return player in (self.player1, self.player2)

    # Functions to manipulate the board

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        if self.in_bounds(column, row) and self.is_valid_player(player):
            self.board[column][row] = player
            return True
        else:
            return False

    def winner_in_row(self):
        row_length = len(self.board[0])
        for row in self.board:
            if row.count(self.player1) == row_length:
                return self.player1
            elif row.count(self.player2) == row_length:
                return self.player2
        return None
                

    def winner_in_column(self):
        column_length = len(self.board)
        values = []
        for column in range(column_length):
            values.clear()
            for row in range(column_length):
                values.append(self.board[row][column])
            if values.count(self.player1) == column_length:
                return self.player1
            elif values.count(self.player2) == column_length:
                return self.player2
        return None

    @staticmethod
    def check_diag(board, column_length):
        found = True
        player = board[0][0]
        for index in range(1, column_length):
            if board[index][index] != player:
                found = False
                break
        if found:
            return player
        else:
            return None

    def winner_in_diag(self):
        column_length = len(self.board)
        winner = self.check_diag(self.board, column_length)
        if winner:
            return winner
        reversed_board = self.board[::-1]
        winner = self.check_diag(reversed_board, column_length)
        return winner        

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        winner = self.winner_in_row()
        winner = self.winner_in_column()
        winner = self.winner_in_diag()
        return winner

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """
        
        pass
