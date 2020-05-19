from game import Board,Game



players =   [1]
snakes =    [ [10,4], [30,4], [40,2], [64,20] ]
ladders =   [ [2,20], [3,30], [10,90], [5,30], [4,40] ]
max = 100
board = Board( snakes, ladders, max)
game = Game( board, players)
game.game_loop()
