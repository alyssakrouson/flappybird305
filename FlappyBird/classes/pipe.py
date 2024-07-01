from classes.draw import Draw
import random

class Pipe():
    def __init__(self, screenHeight, screenWidth) -> None:
        self.startPos = 1000
        self.pipeX = screenWidth
        self.screenY = screenHeight
        self.movement = 0
        self.gapPos = random.randint(screenHeight/2 - 370, screenHeight/2 - 120)
        self.gapStartStop = ((self.screenY - 750 + self.gapPos) +420, (self.screenY - 225 + self.gapPos))
        self.speedOfObjects = 0
        pass

    def generatePipeGraphic(self, drawOnScreen) -> None:
        Draw.drawObstacle(drawOnScreen, self.pipeX, self.screenY, self.gapPos)
        Draw.drawGround(drawOnScreen, self.movement, self.screenY)

    def moveGraphic(self, dt) -> int:
        self.speedOfObjects = 3 * dt
        self.pipeX = self.pipeX - self.speedOfObjects
        self.movement = (self.movement - self.speedOfObjects)
        return self.pipeX

    def resetGraphic(self) -> bool:
        if self.pipeX <= -50:
            self.pipeX = self.startPos
            self.movement = 0
            self.gapPos = random.randint(self.screenY/2 -370, self.screenY/2 -120)
            self.GapStartStop()
            return True
        return False
    def GapStartStop(self):
        self.gapStartStop = ((self.screenY - 750 + self.gapPos) +420, (self.screenY - 225 + self.gapPos))
        return self.gapStartStop
    def getSpeedOfObjects(self):
        return self.speedOfObjects
