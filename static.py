



class Board(object):
    _game_tiles = []

    def __init__(self,length,width):
        if not Board._game_tiles:
            for _ in xrange(length * width):
                Board._game_tiles.append(Tile())

    @staticmethod
    def move_together(x_amount,y_amount):

        for tile in Board._game_tiles:
            tile.move(x_amount,y_amount)
    @staticmethod
    def print_locations():
        for tile in Board._game_tiles:
            print tile.a ,tile.b



class Tile(object):


    def __init__(self):
        self.a = 0
        self.b = 0

    def move(self,a,b):
        self.a += a
        self.b += b


my_board = Board(4,4)
Board.print_locations()
Board.move_together(10,20)
Board.print_locations()

