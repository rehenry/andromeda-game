import pygame, random
pygame.init()

X_MAX = 800
Y_MAX = 600
size = (800, 600)
speed = [5,5]


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load("images/spaceship.png").convert_alpha()
        self.size = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/4), int(self.size[1]/4)))
        #self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect() 
        self.rect.center = (X_MAX/2, Y_MAX/2)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_1.png").convert_alpha()
        self.size = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        #self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (X_MAX/2, Y_MAX - 400)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed[0] = -speed[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed[1] = -speed[1]

        self.rect = self.rect.move(speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, size)
    # screen.blit(background, (0,0))

    all_sprites_list = pygame.sprite.Group()
    asteroid = Asteroid()
    ship = Spaceship()
    all_sprites_list.add(ship, asteroid)

    while True:
        event = pygame.event.poll()    
        if event.type == pygame.QUIT:  
            break 

        screen.blit(background, (0,0))
        all_sprites_list.draw(screen)
        all_sprites_list.update()
        pygame.display.flip()

    pygame.quit()     

main()
