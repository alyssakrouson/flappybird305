class Fly:
    def fly(self,characterY, dt, startGrav):
# Variables used for flight, flightMagnitude determins how many pixels the character will fly up on the screen
# characterHeight is used to make sure the character does not fly off screen in the below conditional
        self.flightMagnitude = 25 * dt
        self.characterHeight = 50
        newGravity = -3.6 * dt
        return newGravity

