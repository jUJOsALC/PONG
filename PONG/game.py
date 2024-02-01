from pygame import *

win_width = 900
win_height = 750
window = display.set_mode((win_width, win_height))
display.set_caption("PONG!")

game = True

def slp(numofccls):
    i = 0
    while i < numofccls:
        i += 1
        print(i)

class Player():
    def __init__(self, x_pos, up_key, down_key):
        self.x = x_pos
        self.y = win_height / 2 - 50
        self.up = up_key
        self.down = down_key
        self.image = Surface((10, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.unableToMove = False

    def update(self):
        if not(self.unableToMove):
            keys = key.get_pressed()
            if (keys[self.up]):
                self.y -= 0.5
            if (keys[self.down]):
                self.y += 0.5

            if self.y < 0:
                self.y = 0
            if self.y > win_height - 100:
                self.y = win_height - 100
        else:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y

        window.blit(self.image, (self.x, self.y))

class Ball():
    def __init__(self):
        self.x = win_width / 2
        self.y = win_height / 2
        self.x_vel = 0.2
        self.y_vel = 0.2
        self.image = Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        if self.y < 0 or self.y > win_height:
            self.y_vel = self.y_vel * -1

        self.y += self.y_vel
        self.x += self.x_vel

        self.rect.x = self.x
        self.rect.y = self.y

        window.blit(self.image, (self.x, self.y))

font.init()
pismo = font.SysFont("Arial", 36)

plrRscr = 0
plrLscr = 0

playerR = Player(860, K_UP, K_DOWN)
playerL = Player(40, K_w, K_s)
ball = Ball()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    playerRscore = pismo.render(str(plrRscr), 1, (255, 255, 255))
    playerLscore = pismo.render(str(plrLscr), 1, (255, 255, 255))


    if sprite.collide_rect(playerR, ball) or sprite.collide_rect(playerL, ball):
       print("ide")
       ball.x_vel = ball.x_vel * -1
       if playerL.unableToMove and sprite.collide_rect(playerR, ball):
           plrLscr += 1


    if ball.x < 0:
        slp(5000)
        plrLscr += 1
        playerL.y = win_height / 2 - 50
        playerR.y = win_height / 2 - 50
        ball.y = win_height / 2
        ball.x = win_width / 2
        ball.x_vel = ball.x_vel * -1

    if ball.x > win_width:
        slp(5000)
        plrRscr += 1
        playerL.y = win_height / 2 - 50
        playerR.y = win_height / 2 - 50
        ball.y = win_height / 2
        ball.x = win_width / 2
        ball.x_vel = ball.x_vel * -1

    keys = key.get_pressed()
    if (keys[K_1]):
        playerL.unableToMove = False
        playerL.image = Surface((10, 100))
        playerL.image.fill((255, 255, 255))
        playerL.rect = playerL.image.get_rect()
    elif (keys[K_2]):
        playerL.unableToMove = True
        playerL.image = Surface((10, 10000))
        playerL.image.fill((255, 255, 255))
        playerL.rect = playerL.image.get_rect()

    window.fill((0, 0, 0))
    window.blit(playerRscore, (200, 100))
    window.blit(playerLscore, (700, 100))
    playerR.update()
    playerL.update()
    ball.update()

    display.update()