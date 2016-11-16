import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load("images/dirt.jpg").convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect() 

def main():
    pygame.init() 
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0,0))

    my_Sprite = Spaceship()
    my_group = pygame.sprite.Group(my_Sprite)

    while True:
        event = pygame.event.poll()    
        if event.type == pygame.QUIT:  
            break                   

        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

    pygame.quit()     

main()
