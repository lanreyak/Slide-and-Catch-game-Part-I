# Lanre Yakubu
# Slide and Catch game Part I
"""
Created on Sun Nov  1, 2024

"""

import pygame
import simpleGE
import random

class Ball(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("soccerBall.png")
        self.setSize(25, 25)
        self.reset()
        self.ballSound = simpleGE.Sound("sound.mp3")
        
        
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)

    def process(self):
        self.y += self.dy
        self.checkBounds()

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Bike(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("player_0.png")
        self.setSize(60, 60)
        self.position = (300, 380)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("storyboard.png")
        self.bike = Bike(self)
        
        #self.balls = [Ball(self) for _ in range(10)]
        self.balls = []
        for i in range(3):
            self.balls.append(Ball(self))

        self.sprites = [self.bike, self.balls]
        
        
    def process(self):
        for ball in self.balls:
            if ball.collidesWith(self.bike):
                ball.ballSound.play()
                ball.reset()
                    
                
        

def main():
    pygame.init()
    game = Game()
    game.start()

if __name__ == "__main__":
    main()