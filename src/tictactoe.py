""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""
import game

        
if __name__ == '__main__':
    game = game.Game()
    game.board.draw()
    winner = game.play()
    print("{} has won!".format(winner))

"""
Three classes:
Game - Rules/checking for valid moves, win condition
Board - Current state of all positions (data)
Player - Name, method to attempt move, symbol (x/o)

game()
game has a board object
object for each player
game.player1.move(0, 1)

"""