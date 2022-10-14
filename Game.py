# random imported to use the Random function
# that computer uses to pick value randomly
import random


class Game:

    def __init__(self):
        self.playerWinsCount = 0
        self.computerWinsCount = 0

    def take_player_computer_inputs(self):

        player_input = int(input("Enter player choice: "))
        print("Player choice is ", player_input)

        if player_input == 1:
            player_choice_name = 'Rock'
        elif player_input == 2:
            player_choice_name = 'paper'
        else:
            player_choice_name = 'scissor'

        print("Player choice Name is ", player_choice_name)

        computer_input = random.randint(1, 3)

        while computer_input == player_input:
            computer_input = random.randint(1, 3)

        print("Computer choice is ", computer_input)

        if computer_input == 1:
            computer_Choice_Name = 'Rock'
        elif computer_input == 2:
            computer_Choice_Name = 'paper'
        else:
            computer_Choice_Name = 'scissor'

        print("Computer Choice Name is: ", computer_Choice_Name + " " + str(computer_input))
        self.compareAndCountWins(player_input, computer_input, player_choice_name, computer_Choice_Name)

    def takeComputerInput(self):

        # if computerInput == '':
        computerInput = random.randint(1, 3)

        # while computerInput == playerInput:
        #     computerInput = random.randint(1, 3)

        print("Computer choice is ", computerInput)

        if computerInput == 1:
            computerChoiceName = 'Rock'
        elif computerInput == 2:
            computerChoiceName = 'paper'
        else:
            computerChoiceName = 'scissor'

        print("Computer Choice is: ", computerChoiceName + " " + str(computerInput))
        # self.compareChoices(playerInput, computerInput, playerChoiceName, computerChoiceName)

    def compareAndCountWins(self, pl, co, player_Choice_Name, computer_Choice_Name):

        print(player_Choice_Name + "  " + str(pl) + " V/s " + computer_Choice_Name + " " + str(co))
        # we need to check of a draw
        if pl == co:
            print("Draw=> ", end="")
            result = "Draw"

        # condition for winning
        if ((pl == 1 and co == 2) or
                (pl == 2 and co == 1)):
            print("paper wins => ", end="")
            result = "paper"

        elif ((pl == 1 and co == 3) or
              (pl == 3 and co == 1)):
            print("** Rock wins this round **", end="")
            result = "Rock"

        elif ((pl == 2 and co == 3) or
              (pl == 3 and co == 2)):
            print("** Scissor wins this round **", end="")
            result = "scissor"
        # Printing who wins or draw
        if result == "Draw":
            print("Its a draw")

        if result == player_Choice_Name:
            self.playerWinsCount = self.playerWinsCount + 1
            print("Player wins this round", self.playerWinsCount)
        else:
            self.computerWinsCount = self.computerWinsCount + 1
            print("Computer wins this round", self.computerWinsCount)

    def runGameLogic(self):
        print("inside game")

        while self.playerWinsCount < 5 and self.computerWinsCount < 5:

            self.take_player_computer_inputs()
            if self.playerWinsCount >= 5 or self.computerWinsCount >= 5:
                break
            print("Do you want to play again? (Y/N)")
            ansSub = input().casefold()
            if ansSub != 'y':
                print("Thanks for playing..Have a good time")
                break

        if self.playerWinsCount >= 5 or self.computerWinsCount >= 5:
            if self.playerWinsCount >= 5:
                print("Player wins the game")
            elif self.computerWinsCount >= 5:
                print("Computer wins the game")

            print("Do you want to Quit or Restart the game? "
                  "Please enter Q or R !")
            ansMain = input().casefold()

            if ansMain != 'r':
                print("Thanks for playing.")
                exit()
            else:
                self.playerWinsCount = 0
                self.computerWinsCount = 0
                self.runGameLogic()

    def is_Win(self):

        if self.playerWinsCount >= 5 or self.computerWinsCount >= 5:
            return True
        return False


if __name__ == '__main__':
    object1 = Game()
    object1.runGameLogic()
