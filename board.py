class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
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

    # Functions to manipulate the board

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        if self.in_bounds(column, row):
            self.board[column][row] = player
            return True
        else:
            return False

    # Check winners

    def __winner_in_row__(self):
        row_length = len(self.board[0])
        for row in self.board:
            # get first element in the row (i.e. X or O)
            firstElem = row[0]

            # if first element is None then bail out
            if firstElem == None:
                continue

            # Check if there is three of said element
            if row.count(firstElem) == row_length:
                return firstElem

        return None
                

    def __winner_in_column__(self):
        column_length = len(self.board)
        values = []
        for column in range(column_length):
            values.clear()
            for row in range(column_length):
                values.append(self.board[row][column])

            # get first element in the row (i.e. X or O)
            firstElem = row[0]

            # if first element is None then bail out
            if firstElem == None:
                continue

            # Check if there is three of said element
            if row.count(firstElem) == row_length:
                return firstElem

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

    def __winner_in_diag__(self):
        column_length = len(self.board)
        winner = self.check_diag(self.board, column_length)
        if winner:
            return winner
        reversed_board = self.board[::-1]
        winner = self.check_diag(reversed_board, column_length)
        return winner        

    def check_for_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """

        winner = self.__winner_in_row__()
        winner = self.__winner_in_column__()
        winner = self.__winner_in_diag__()
        return winner