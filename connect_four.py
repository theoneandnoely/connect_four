import random

class AI():
    def __init__(self, mode):
        self.mode = mode

    def turn(self, board, marker):
        valid_move = False
        while valid_move == False:
            move = self.eval_move(board, marker)
            if board[0][move-1] == ' ':
                valid_move = True
        if board[5][move-1] == ' ':
            board[5][move-1] = marker
        else:
            for i in range(6):
                if board[i][move-1] != ' ':
                    board[i-1][move-1] = marker
                    break
        return board
    
    def eval_move(self, board, marker):
        if self.mode == "EASY":
            return round(random.uniform(1,7))
        elif self.mode == "MEDIUM":
            for i in range(len(board)):
                for j in range(len(board[i])):
                    pass
            return round(random.uniform(1,7))
        else:
            return round(random.uniform(1,7))

class ConnectFour():
    def __init__(self):
        self.board = [[' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ']]
        self.state = "in_play"
        self.player_one = 'x'
        self.player_two = 'o'

    def turn(self, player):
        for i in range(len(self.board)):
            print(self.board[i])
        print("  1    2    3    4    5    6    7\n")
        print("Player {} to move...".format(player))
        valid_move = False
        while valid_move == False:
            chosen_move = int(input("Select Column (1-7) To Play: "))
            if chosen_move < 1 or chosen_move > 7:
                print("Input must be a column number (1-7)!")
            elif self.board[0][chosen_move-1] != ' ':
                print("Column Full! Please select a different column: ")
            else:
                valid_move = True
        if self.board[5][chosen_move-1] == ' ':
            if player == 1:
                self.board[5][chosen_move-1] = self.player_one
            else:
                self.board[5][chosen_move-1] = self.player_two
        else:
            for i in range(6):
                if self.board[i][chosen_move-1] != ' ':
                    if player == 1:
                        self.board[i-1][chosen_move-1] = self.player_one
                    else:
                        self.board[i-1][chosen_move-1] = self.player_two
                    break
    
    def eval_state(self) -> str:
        if self.board[0].count(' ') == 0:
            return "draw"
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    connect = 0
                    if self.board[i][j] != ' ':
                        connect = 1
                        for x in [-1,0,1]:
                                for y in [-1,0,1]:
                                    still_connected = True
                                    while still_connected == True and connect < 4:
                                        if (x==0 and y==0) or ((i+(y*connect)) < 0) or ((i+(y*connect)) > 5) or ((j+(x*connect)) < 0) or ((j+(x*connect)) > 6):
                                            still_connected = False
                                            connect = 1
                                        elif self.board[i+(y*connect)][j+(x*connect)] == self.board[i][j]:
                                            connect += 1
                                        else:
                                            still_connected = False
                                            connect = 1
                                    if connect == 4:
                                        if self.board[i][j] == self.player_one:
                                            return "p1"
                                        else:
                                            return "p2"
            return "in_play"
        
    def play(self, mode):
        player = 1
        player_2 = None
        if mode != "2-PLAYER":
            player_2 = AI(mode)
        while self.state == "in_play":
            if player == 2 and player_2:
                self.board = player_2.turn(self.board, self.player_two)
            else:
                self.turn(player)
            self.state = self.eval_state()
            if player == 1:
                player = 2
            else:
                player = 1
        for i in range(len(self.board)):
            print(self.board[i])
        print("\nGAME OVER:")
        if self.state == "draw":
            print("Game ended in a draw!")
        elif self.state == "p1":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")

if __name__ == "__main__":
    valid_game_mode = False
    while valid_game_mode == False:
        game_mode = input("Select Game Mode (EASY/MEDIUM/HARD/2-PLAYER):\n")
        if game_mode in ["EASY", "easy", "Easy", "E", "e"]:
            valid_game_mode = True
            game_mode = "EASY"
        elif game_mode in ["MEDIUM", "Medium", "medium", "M", "m"]:
            valid_game_mode = True
            game_mode = "MEDIUM"
        elif game_mode in ["HARD", "Hard", "hard", "H", "h"]:
            valid_game_mode = True
            game_mode = "HARD"
        elif game_mode in ["2-PLAYER", "2 Player", "2-player", "2 player", "2P", "2p", "2"]:
            valid_game_mode = True
            game_mode = "2-PLAYER"
        else:
            print("Invalid Game Mode!")
    game = ConnectFour()
    game.play(game_mode)