from itertools import cycle
import sys

class SnakesLadders():
    #class object attributes here (common to all instances of clases)

    def __init__(self):
        self.snake_dict = {16:6, 46:25, 49:11, 64:60, 62:19, 74:53,
                           89:68, 92:88, 95:75, 99:80}
        self.ladder_dict = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84,
                            36:44, 51:67, 71:91, 78:98, 87:94}
        self.current_pos = [0,0]
        self.win_flag = 0
        self.playerIterator = cycle(["player1", "player2"])
        self.current_player = self.playerIterator.next() #initialize the current player1

    def play(self, die1, die2):
        if self.win_flag == 1:
            return ("Game over!")
        current_player = self.get_currentPlayer()
        current_pos = self.update_position(current_player, die1, die2)
        #self.update_posOverflow(current_player, current_pos)
        win_state = self.check_win(current_player, self.current_pos)
        if win_state[1]:
            if (self.win_flag == 0 and current_player == "player1"):
                self.win_flag = 1
                return ("Player 1 Wins!")
            elif (self.win_flag == 0 and current_player == "player2"):
                self.win_flag = 1
                return ("Player 2 Wins!")
        if self.check_repeatPlay(die1, die2):
                self.current_player = current_player
        else:
            self.current_player = self.playerIterator.next()
        if current_player == "player1":
            return ("Player 1 is on square {}".format(self.current_pos[0]))
        elif current_player == "player2":
            return ("Player 2 is on square {}".format(self.current_pos[1]))


    def get_currentPos(self):
        """Return the current postion of player1 and player2"""
        pass

    def get_currentPlayer(self):
        """Return who is the current player"""
        return self.current_player

    def update_position(self, current_player, die1, die2):
        """update the position the players"""
        if (current_player == "player1"):
                self.current_pos = [self.current_pos[0]+die1+die2, self.current_pos[1]]

        elif current_player == "player2":
                self.current_pos = [self.current_pos[0], self.current_pos[1]+die1+die2]
        #control what happens when the move is beyond 100
        self.update_posOverflow(current_player, self.current_pos)
        self.check_ladder(current_player, self.current_pos)
        self.check_snake(current_player, self.current_pos)
        return self.current_pos

    def update_posOverflow(self, current_player, current_pos):
        """update the current position if greater than 100"""
        if(current_player == "player1" and current_pos[0] > 100):
            self.current_pos[0] = 200 - current_pos[0]
        if(current_player == "player2" and current_pos[1] > 100):
            self.current_pos[1] = 200 - current_pos[1]


    def update_player(self):
        """update the player who will go next"""
        pass

    def check_repeatPlay(self, die1, die2):
        "check if die1 and die2 are equal and the player has to repeat the play"
        if die1 == die2:
            return True
        else:
            return False

    def check_ladder(self, current_player, current_pos):
        """updates the current position based on the position and ladder dictionary"""
        if (current_player == "player1"):
            if current_pos[0] in self.ladder_dict.keys():
                self.current_pos = [self.ladder_dict[current_pos[0]], current_pos[1]]
        elif (current_player == "player2"):
            if current_pos[1] in self.ladder_dict.keys():
                self.current_pos = [current_pos[0], self.ladder_dict[current_pos[1]]]

    def check_snake(self, current_player, current_pos):
        """updates the current position based on the position and snake dictionary"""
        if (current_player == "player1"):
            if current_pos[0] in self.snake_dict.keys():
                self.current_pos = [self.snake_dict[current_pos[0]], current_pos[1]]
        elif (current_player == "player2"):
            if current_pos[1] in self.snake_dict.keys():
                self.current_pos = [current_pos[0], self.snake_dict[current_pos[1]]]

    def check_win(self, current_player, current_pos):
        """chenk if a winning situation occurs"""
        if (current_player == "player1" and current_pos[0] == 100):
            win_state = ("player1", True)
        elif ( current_player == "player2" and current_pos[1] == 100):
            win_state = ("player2", True)
        else:
            win_state = (current_player, False)
        return win_state

game = SnakesLadders()
game.play(1,1)
game.play(3,4)
game.play(4,5)
#assert game.play(1, 1), "Player 1 is on square 38"
#assert game.play(1, 5), "Player 1 is on square 44"
#print(game.play(6, 2))
#assert game.play(6, 2), "Player 2 is on square 31"
#assert game.play(1, 1), "Player 1 is on square 25"
