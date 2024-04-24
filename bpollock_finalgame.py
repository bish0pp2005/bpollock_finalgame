import pygame, simpleGE, random
pygame.mixer.music.load('scarysong.mp3')
pygame.mixer.music.play()
class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("red", (40, 40))
        self.setBoundAction(self.HIDE)
        self.hide()        
    def fire(self):
        self.show()
        self.moveAngle = self.parent.imageAngle
        self.position = self.parent.position
        self.speed = 35     
class Ghost(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ghost.png")
        self.setSize(60, 60)
        self.movement()
        self.setBoundAction(self.BOUNCE)        
    def movement(self):
        self.x = 30
        self.y = random.randint(0, self.screenWidth)
        self.dy = random.randint(-8, 8)
        if self.dy == 0:
            self.dy = random.randint(-8, 8)

class Knight(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("knight.png")
        self.setSize(40, 40)
        self.position = (550, 76)
        self.moveSpeed = 8
        
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_s):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_w):
            self.y -= self.moveSpeed
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.fgColor = "white"
        self.bgColor = "black"
        self.text = "Score"
        self.clearBack = True
        self.center = (50, 20)
        self.size = (150, 30)
class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time"
        self.center = (550, 20)
        self.size = (150, 30)  
        self.clearBack = True


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("castleinthedark.gif")     
        
        self.sndBullet = simpleGE.Sound("hitsound.mp3")
        
        self.ghost = Ghost(self)     
        self.bullet = Bullet(self, self.ghost)
        self.knight = Knight(self)
        self.lblScore = LblScore()
        self.lblTimer = LblTimer()
        
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 18
        

        self.sprites = [self.ghost,
                        self.bullet,
                        self.knight,
                        self.lblScore,
                        self.lblTimer
                        ]
    def process(self):
        self.bullet.fire()
        if self.knight.collidesWith(self.bullet):
            self.score += 1
            self.lblScore.text = f"Score {self.score}"
            self.sndBullet.play()
        timeLeft = self.timer.getTimeLeft()
        self.lblTimer.text = f"Time Left: {timeLeft:.2f}"
        if timeLeft < 0:
            self.stop()
            if self.score == 0:
                print("Hey... You're supposed to hit the ghost. (Stand in the red box)")
            if self.score < 200:
                print("You hit that ghost quite a bit!")
            if self.score > 200:
                print("You killed the ghost!")
            
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (400, 300)
        self.lblInstructions.textLines = [
            "Move with WASD",
            "Stand in the red box to hurt the ghost!",
            "Click to start."
        ]
        
        self.sprites = [self.lblInstructions]
    def process(self):
        if self.lblInstructions.clicked:
            self.stop()
class GameOver(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Score: {self.score}"
        self.lblScore.center = (320, 140)

        self.btnAgain = simpleGE.Button()
        self.btnAgain.text = "Play again"
        self.btnAgain.center = (150, 250)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (450, 250)

        self.sprites = [self.lblScore, self.btnAgain, self.btnQuit]

        
    def setScore(self, score):
        self.score = score
        self.lblScore.text = f"Score: {self.score}"

    def process(self):
        if self.btnAgain.clicked:
            self.next = "again"
            self.stop()
            
        if self.btnQuit.clicked:
            self.next = "quit"
            self.stop()

def main():
    
    keepGoing = True
    while (keepGoing):
        instructions = Instructions()
        instructions.start()
        
        game = Game()
        game.start()
        
        gameOver = GameOver()
        gameOver.setScore(game.score)
        gameOver.start()

        if gameOver.next == "quit":
            keepGoing = False

if __name__ == "__main__":
    main()