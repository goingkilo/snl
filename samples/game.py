import random

import logging

throw_die = lambda : random.randint(1,6)


class Board:
    def __init__(self, snakes, ladders, max =100):
        self.max = 100
        self.snakes = snakes
        self.ladders = ladders

    def get_pos(self,x):
        for i in self.snakes:
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
            a = self.player_pos[ player]
            pos = self.player_pos[ player ] + jump
            final_pos = self.board.get_pos(  pos)
            print(a ," + ", jump, " = ", final_pos)
            self.player_pos[ player ] = final_pos


