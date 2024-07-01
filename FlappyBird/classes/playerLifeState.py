'''
This is the PlayerLifeState class in which the class takes 4 integer values, being the x and y coordinates of the player character
and the x and y coordinates for the open gap of the Pipe(s)
The class has an "evaluateState" feature in which it takes in the 4 input functions and evuates if the player has made a collision or not.
'''
class playerLifeState:
    # currentState is meant to be used as the only input to determine if the player has made a collision or not (assuming the player class can send a numeric signal: 1 or 0).
    def __init__(self,PlayerX) -> int:
        self.PlayerX = PlayerX

    
    def evaluateState(self,PlayerY, pipeX, gapPos):
        self.PlayerY = PlayerY
        self.PipeGap = gapPos
        if(self.PlayerX >= pipeX - 20 and self.PlayerX <= pipeX + 30):
            if(self.PlayerY < gapPos[0]-18 or self.PlayerY > gapPos[1]-35):
               return False #Player is no longer alive
        if(self.PlayerX +28 >= pipeX - 20 and self.PlayerX + 28 <= pipeX + 30):
            if (self.PlayerY < gapPos[0] - 30 or self.PlayerY > gapPos[1] - 25):
                return False
        if(PlayerY >= 415):
            return False
        return True  # Player is Alive and also gets a point, implement that here