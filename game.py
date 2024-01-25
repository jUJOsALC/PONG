from pygame import *

win_width = 900
win_height = 750
window = display.set_mode((win_width, win_height))
display.set_caption("PONG!")

game = True

class Player():
    def __init__(self, x_pos, up_key, down_key):
        self.x = x_pos
        self.y = win_height / 2 - 50
        self.up = up_key
        self.down = down_key
        self.image = Surface((10, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()


    def update(self):
        keys = key.get_pressed()
        if (keys[self.up]):
            self.y -= 0.5
        if (keys[self.down]):
            self.y += 0.5

        if self.y < 0:
            self.y = 0
        if self.y > win_height - 100:
            self.y = win_height - 100

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

playerR = Player(850, K_UP, K_DOWN)
playerL = Player(50, K_w, K_s)
ball = Ball()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(playerR, ball) or sprite.collide_rect(playerL, ball):
       print("ide")
       ball.x_vel = ball.x_vel * -1

    if ball.x < 0:
        playerL.y = win_height / 2 - 50
        playerR.y = win_height / 2 - 50
        ball.y = win_height / 2
        ball.x = win_width / 2
        ball.x_vel = ball.x_vel * -1
   
    window.fill((0, 0, 0))
    playerR.update()
    playerL.update()
    ball.update()

    display.update()