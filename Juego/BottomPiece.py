#this class derivates from Piece. Is just a type of piece and it has two states, can have a static or a crash state

from State import State
import State

class BottomPiece(Piece):

    def __init__(self, color , state):
        #create the state of the piece
        self.state = State(state)        

        #think about the color of the pieces.
        self.color = "red" #is an example.

    def getStateOfPiece():
        return self.state.getStateOfPiece()
