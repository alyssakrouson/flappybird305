class Fly:
    def fly(self, characterY, dt):
        # Variables used for flight, flightMagnitude determines how many pixels the character will fly up on the screen
        # characterHeight is used to make sure the character does not fly off screen in the below conditional
        self.flightMagnitude = 25 * dt ** 2
        self.characterHeight = 20

        if characterY - self.flightMagnitude > self.characterHeight:
            characterY -= self.flightMagnitude
        else:
            characterY = self.characterHeight
        return characterY
    
"""Gravity() is used to make the player fall on the Y-axis when the player is not in the state of flying
   Gravity has one method, gravityEffect. gravityEffect is used to apply gravity to the player, it takes
   in 2 parameters, the characterY (Y postion of player) and dt. dt stands for delta time and is used to
   create a framerate cap so the game runs consistantly on different machine. The gravity magnitude is 
   defined by multiplying a number by dt. this creates a constant rate of falling for the player that 
   we could change if we want the difficulty to increase/decrease. The conditional withing the gravityEffect
   method is used to ensure that the player does not fall off screen, if that conditional is met then the
   characterY will increase by the gravityMagnitude, making it fall down the screen.
"""

class Gravity():
    # Method used for having the character fall on screen
    def gravityEffect(self, characterY, dt):
        self.gravityMagnitude = 1.2 * dt ** 2
        if characterY + self.gravityMagnitude < 700:
            characterY += self.gravityMagnitude
        return characterY