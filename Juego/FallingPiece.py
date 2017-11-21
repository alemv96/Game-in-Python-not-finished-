import Piece

class FallingPiece(Piece):

    def __init__(self, color , state):
        #create the state of the piece
        self.state = State()
        self.state.setState("Falling")
