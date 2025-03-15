from random import randint
from pygame import *

window_width = 400
window_height = 600

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < window_width - 80:
            self.rect.x += self.speed

class Components(GameSprite):

    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= window_height:
            self.rect.x = randint(80, window_width - 80)
            self.rect.y = 0
            lost += 1

lost = 0
window_width, window_height = 700, 500
window = display.set_mode((window_width, window_height))
display.set_caption("PC BUILDER")

component_img = ["KARTA PAMATI.png","MONITOR.png", "PROCESOR.png", "VIDEOCARTA.png"]

background = transform.scale(image.load("1679381547_zefirka-club-p-krasivii-fon-dlya-strima-16.jpg"), (window_width, window_height))
player = Player("GLAVNY GEROI.png", 5, window_height - 100, 80, 100, 10)
components = sprite.Group()
for i in range(4):
    enemy = Components(component_img[i], randint(80, window_width - 80), -40, 80, 50, randint(1, 5))
    components.add(enemy)

finish = False
run = True
score = 0

clock = time.Clock()
FPS = 60

font.init()
font2 = font.Font(None, 40)

while run:

    if not finish:
        window.blit(background, (0, 0))

        text = font2.render(f"Рахунок: {score}", 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render(f"СКІПНУТІ: {lost}", 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        player.update()

        components.update()
        components.draw(window)


        player.reset(window)



    display.update()
    clock.tick(FPS)