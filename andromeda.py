import pygame

X_MAX = 800
Y_MAX = 600

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
        
def main():
 
    pygame.init() 
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0,0))

    ship = Spaceship()
    asteroid = Asteroid()
    obj_group = pygame.sprite.Group(ship, asteroid)

    while True:
        event = pygame.event.poll()    
        if event.type == pygame.QUIT:  
            break 

        obj_group.update()
        obj_group.draw(screen)
        pygame.display.flip()

    pygame.quit()     

main()
