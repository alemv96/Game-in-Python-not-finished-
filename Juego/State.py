#this class will contain every state of the pieces
#We have 3 types of states:
#1) static: for the bottom pieces
#2) fallen: for the fallen pieces
#3) crash: this state will indicate when both pieces have a collision

class State:

    typeState

    def __init__(self):
        self.typeState = ' ' #declare this variable as an empty state

    def setState(self, newState):
        self.typeState = newState

    def getState():
        return self.typeState
