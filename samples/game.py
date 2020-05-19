import random


throw_die = lambda : random.randint(1,6)


class Board:
    def __init__(self, snakes, ladders, max =100):
        self.max = 100
        self.snakes = snakes
        self.ladders = ladders

    def get_pos(self,x):
        print(x,self.snakes)
        for i in self.snakes:
            print(i)
            if i[0] == x:
                print( "sliding down from",x, "to", i[1])
                return i[1]
        for i in self.ladders:
            if i[0] == x:
                print( "jumping  up from",x, "to", i[1])
                return i[1]
        return x


class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.player_pos = [ 0 for x in range(len(self.players))]
        self.player_to_play = -1

    def get_next_player(self):
        self.player_to_play =  (self.player_to_play +1 ) % len(self.players)
        return self.player_to_play

    def game_over(self):
        for i in range(len(self.player_pos)):
            if self.player_pos[i] >= self.board.max:
                print( "player ", i, " won")
                return True
        return False

    def game_loop(self):
        while not self.game_over():
            player = self.get_next_player()
            jump = throw_die()
            pos = self.player_pos[ player ] + jump
            final_pos = self.board.get_pos(  pos)
            self.player_pos[ player ] = final_pos
            print( player,  " got " ,jump, "and is now at ", self.player_pos)


players =   [1]
snakes =    [ [10,4], [30,4], [40,2], [64,20] ]
ladders =   [ [2,20], [3,30], [10,90], [5,30], [4,40] ]
max = 100
board = Board( snakes, ladders, max)
game = Game( board, players)
game.game_loop()
