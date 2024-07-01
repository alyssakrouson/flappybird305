class Gravity():
# Method used for having the character fall on screen
    def gravityEffect(self,characterY, dt, gravityMagnitude):
        topOfScreen = -6
        if(characterY <= 415):
            gravityMagnitude += 0.2 * dt
            characterY = characterY + gravityMagnitude
            if characterY > 415:
                characterY = 415
        if(characterY < topOfScreen):
            characterY = topOfScreen
            gravityMagnitude = -0.2 * dt
        # else call restart screen
        return characterY, gravityMagnitude