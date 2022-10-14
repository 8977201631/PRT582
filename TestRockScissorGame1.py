import unittest
from enum import IntEnum

from Game import Game


class Input(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


# @patch('builtins.print')
class UnitTestMainGame(unittest.TestCase):

    def test_unitTestPaperWinsVsRock(self):
        # rock[0], paper[1], scissors[2]
        game = Game()
        userInput = 2
        computerInput = 1
        game.compareAndCountWins(userInput, computerInput, 'paper', 'Rock')
        assert game.playerWinsCount == 1

    def test_unitTestRockWinsVsScissor(self):
        game = Game()
        userInput = 1
        computerInput = 3
        game.compareAndCountWins(userInput, computerInput, 'Rock', 'scissor')
        assert game.playerWinsCount == 1


if __name__ == "__main__":
    unittest.main()
