from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,
                 width=55, height=55):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (width, height))

        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    side = 'left'

    def __init__(self, enemy_image, x, y, speed):
        super().__init__(enemy_image, x, y, speed, 65, 65)
        self.alive = True

    def die(self):
        self.kill()
        self.alive = False

    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed   

win_width = 700
win_height = 500

                                    

window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.jpg") , (700, 500))
sprite1 = transform.scale(image.load("sobaka.png") , (100, 100))
sprite2 = transform.scale(image.load("svin.webp") , (100, 100))
x1 = 100
y1 = 300

x2 = 300
y2 = 300

speed = 10
window.blit(background,(0, 0))
game = True 

clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()

money_sound = mixer.Sound('final_point.mp3')
kick_sound = mixer.Sound('kick.ogg')
gun_sound = mixer.Sound('gun.mp3')
voice_sound = mixer.Sound('voice.mp3')



while game:
    window.blit(background,(0, 0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))


    for e in event.get():
        if e. type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
                


                


                





    display.update()   
    clock.tick(FPS)     


