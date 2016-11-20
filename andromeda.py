import pygame, random

# from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
#     K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN

# LEFT, RIGHT, UP, DOWN = 0, 1, 3, 4
# START, STOP = 0, 1

X_MAX, Y_MAX = 800, 600

#still playing with speeds
speed = [4,4]
speed2 = [5,5]
speed3 = [6,6]
speed4 = [3,3]
speed5 = [2,2]
speed6 = [6,6]


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load("images/spaceship.png").convert_alpha()
        self.size = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/4), int(self.size[1]/4)))
        self.rect = self.image.get_rect() 
        self.rect.center = (X_MAX/2, Y_MAX/2)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_1.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed[0] = -speed[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed[1] = -speed[1]

        self.rect = self.rect.move(speed)

class Asteroid2(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid2, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_2.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed2[0] = -speed2[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed2[1] = -speed2[1]

        self.rect = self.rect.move(speed2)

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid3, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_3.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed3[0] = -speed3[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed3[1] = -speed3[1]

        self.rect = self.rect.move(speed3)

class Asteroid4(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid4, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_1.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed4[0] = -speed4[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed4[1] = -speed4[1]

        self.rect = self.rect.move(speed4)

class Asteroid5(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid5, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_2.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed5[0] = -speed5[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed5[1] = -speed5[1]

        self.rect = self.rect.move(speed5)

class Asteroid6(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid6, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_3.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+70, 800-70)
        self.y = init_y = random.randint(0+70,600-70)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed6[0] = -speed6[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed6[1] = -speed6[1]

        self.rect = self.rect.move(speed6)

def main():

    pygame.init()
    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (X_MAX, Y_MAX))

    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    ship = Spaceship()
    asteroids.add(Asteroid(0,0), Asteroid2(0,0), Asteroid3(0,0), Asteroid4(0,0), Asteroid5(0,0), Asteroid6(0,0))

    all_sprites.add(ship, asteroids)


    while True:
        event = pygame.event.poll()    
        if event.type == pygame.QUIT:  
            break 

        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

    pygame.quit()

main()
