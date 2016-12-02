import pygame, random
pygame.init()

from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_SPACE, K_RETURN, K_LSHIFT

X_MAX, Y_MAX = 800, 600

speed1 = [3,3]
speed2 = [5,5]
speed3 = [7,7]
speed4 = [5,5]
speed5 = [4,4]
speed6 = [6,6]
speed7 = [10,10]
speed8 = [11,11]
speed9 = [9,9]

LEFT, RIGHT, UP, DOWN = 0, 1, 3, 4
START, STOP = 0, 1

class Start(pygame.sprite.Sprite):
    def __init__(self):
        super(Start, self).__init__()
        self.image = pygame.Surface((500, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.font = pygame.font.Font("fonts/ScreenMatrix.ttf", 25)
        self.font2 = pygame.font.Font("fonts/ScreenMatrix.ttf", 55)

    def update(self):
        self.logo = pygame.image.load("images/andromeda.png").convert_alpha()
        self.logo = pygame.transform.smoothscale(self.logo, (100, 200))
        title = self.font2.render("ANDROMEDA", True, (3, 168, 158))
        begin = self.font.render("Press Enter To Start", True, (255, 255, 255))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.logo, (10, 0))
        self.image.blit(title, (135, 60))
        self.image.blit(begin, (145, 130))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_1.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = random.randint(0+60, 800-60)
        self.y = random.randint(0+60,600-60)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed1[0] = -speed1[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed1[1] = -speed1[1]

        self.rect = self.rect.move(speed1)

class Asteroid2(Asteroid):
    def __init__(self):
        super(Asteroid2, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_2.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (60, 60))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed2[0] = -speed2[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed2[1] = -speed2[1]

        self.rect = self.rect.move(speed2)

class Asteroid3(Asteroid):
    def __init__(self):
        super(Asteroid3, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_3.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (60, 60))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed3[0] = -speed3[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed3[1] = -speed3[1]

        self.rect = self.rect.move(speed3)

class Asteroid4(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid4, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_1.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.x = random.randint(0+45, 800-45)
        self.y = random.randint(0+45,600-45)
        self.rect.center = (self.x, self.y)        

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed4[0] = -speed4[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed4[1] = -speed4[1]

        self.rect = self.rect.move(speed4)

class Asteroid5(Asteroid4):
    def __init__(self):
        super(Asteroid5, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_2.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (45, 45))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed5[0] = -speed5[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed5[1] = -speed5[1]

        self.rect = self.rect.move(speed5)

class Asteroid6(Asteroid4):
    def __init__(self):
        super(Asteroid6, self).__init__()
        self.image = pygame.image.load("images/asteroid_md_3.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (45, 45))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed6[0] = -speed6[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed6[1] = -speed6[1]

        self.rect = self.rect.move(speed6)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, all_group, weapon_group):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load("images/spaceship.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (55, 75))
        self.rect = self.image.get_rect() 
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.dx = self.dy = 0
        self.groups = [all_group, weapon_group]
        self.in_position = False
        self.firing = self.shot = False
        self.health = 100
        self.score = 0
        self.shotsfired = pygame.mixer.Sound("sounds/shotsfired.wav")
        self.shotsfired.set_volume(0.3)

    def update(self):
        x, y = self.rect.center

        if not self.in_position:
            self.rect.center = x + self.dx, y + self.dy
            
        if self.firing:
            self.shot = Particle(x,y)
            self.shotsfired.play(maxtime= 1000)
            self.shot.add(self.groups)

    def steer(self, direction, operation):
        v = 5
        if operation == START:
            if direction in (UP, DOWN):
                self.dy = {UP: -v, DOWN: v}[direction]
            if direction in (LEFT, RIGHT):
                self.dx = {LEFT: -v, RIGHT: v}[direction]                  

        if operation == STOP:
            if direction in (UP, DOWN):
                self.dy = 0
            if direction in (LEFT, RIGHT):
                self.dx = 0

    def shoot(self, operation):
        if operation == START:
            self.firing = True
        if operation == STOP:
            self.firing = False

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Particle, self).__init__()
        self.image = pygame.Surface((2, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y-40)

    def update(self):
        self.rect.y -=10 
        if self.rect.y < -10:
            self.kill()

class Bits(pygame.sprite.Sprite):
    def __init__(self):
        super(Bits, self).__init__()
        self.image = pygame.image.load("images/asteroid_sm_2.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.x = random.randint(0+30, 800-30)
        self.y = random.randint(0+30,600-30)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed7[0] = -speed7[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed7[1] = -speed7[1]

        self.rect = self.rect.move(speed7)

class Bits2(Bits):
    def __init__(self):
        super(Bits2, self).__init__()
        self.image = pygame.image.load("images/asteroid_sm_3.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (30, 30))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed8[0] = -speed8[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed8[1] = -speed8[1]

        self.rect = self.rect.move(speed8)

class Bits3(Bits):
    def __init__(self):
        super(Bits3, self).__init__()
        self.image = pygame.image.load("images/asteroid_sm_1.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (30, 30))

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed9[0] = -speed9[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed9[1] = -speed9[1]

        self.rect = self.rect.move(speed9)

class Status(pygame.sprite.Sprite):
    def __init__(self, ship):
        super(Status, self).__init__()
        self.image = pygame.Surface((X_MAX, 30))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = 25, Y_MAX
        self.font = pygame.font.Font("fonts/ScreenMatrix.ttf", 24)
        self.ship = ship

    def update(self):
        score = self.font.render("Health : {} Score : {}".format(
            self.ship.health, self.ship.score), True, (255, 255, 255)) 
        self.image.fill((0, 0, 0))
        self.image.blit(score, (0, 0))
        self.image.set_colorkey((0, 0, 0))

class Lose(pygame.sprite.Sprite):
    def __init__(self, ship, asteroids, asteroid_spawns, status):
        super(Lose, self).__init__()
        self.image = pygame.Surface((500, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.font = pygame.font.Font("fonts/ScreenMatrix.ttf", 45)
        self.font2 = pygame.font.Font("fonts/ScreenMatrix.ttf", 30)
        self.ship = ship
        self.asteroids = asteroids
        self.asteroid_spawns = asteroid_spawns
        self.status = status
        self.check = 0
        
    def update(self):
        sorry = self.font.render("GAME OVER", True, (255, 255, 255))
        score = self.font2.render("High Score: {}".format(
            self.ship.score), True, (255, 255, 255))
        #play_again = self.font2.render("Press Enter to Play Again", True, (255, 255, 255))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        if self.ship.health <= 0:
            if self.check == 0:
                pygame.mixer.Sound("sounds/defeat.wav").play()
                self.check = 1

        if self.check == 1:
            self.ship.kill()
            for asteroid in self.asteroids:
                asteroid.kill()
            for asteroid in self.asteroid_spawns:
                asteroid.kill()
            self.status.kill()
            self.image.blit(sorry, (128, 80))
            self.image.blit(score, (132, 120)) 
            #self.image.blit(play_again, (60, 160))

        if self.ship.health > 0:
            if self.ship.score <= 0:
                if len(self.asteroids) == 0:
                    if len(self.asteroid_spawns) == 0:
                        if self.check == 0:
                            pygame.mixer.Sound("sounds/defeat.wav").play()
                            self.check = 1
        
        if self.check == 1:
            self.ship.kill()
            self.status.kill()
            self.ship.kill()
            self.image.blit(sorry, (128, 80))
            self.image.blit(score, (132, 120))
            #self.image.blit(play_again, (60, 160))
                  
class Win(pygame.sprite.Sprite):
    def __init__(self, ship, asteroids, asteroid_spawns, status):
        super(Win, self).__init__()
        self.image = pygame.Surface((500, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.font = pygame.font.Font("fonts/ScreenMatrix.ttf", 45)
        self.font2 = pygame.font.Font("fonts/ScreenMatrix.ttf", 30)
        self.ship = ship
        self.asteroids = asteroids
        self.asteroid_spawns = asteroid_spawns
        self.status = status
        self.check = 0
        
    def update(self):
        hurray = self.font.render("YOU WIN!", True, (255, 255, 255))
        score = self.font2.render("High Score: {}".format(
            self.ship.score), True, (255, 255, 255))
        #play_again = self.font2.render("Press Enter to Play Again", True, (255, 255, 255))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        if self.ship.score >= 60:
            if self.check == 0:
                pygame.mixer.Sound("sounds/victory.wav").play()
                self.check = 1
                       
        if self.check == 1:
            self.ship.kill()
            for asteroid in self.asteroids:
                asteroid.kill()
            for asteroid in self.asteroid_spawns:
                asteroid.kill()
            self.status.kill()
            self.image.blit(hurray, (155, 80))
            self.image.blit(score, (132, 120))
            #self.image.blit(play_again, (60, 160))
              
def intro():

    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (X_MAX, Y_MAX))
    #theme = pygame.mixer.Sound("sounds/andromeda.wav").play(loops= 10)
    #theme.set_volume(0.2)

    start = Start()
    letsplay = pygame.sprite.Group()
    letsplay.add(start)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if not game_over:
                if event.type == KEYDOWN and event.key == K_RETURN:
                    theme.pause()
                    letsgo = pygame.mixer.Sound("sounds/enteringgalaxy.wav").play()
                    letsgo.set_volume(0.7)
                    return

        screen.blit(background, (0, 0))
        letsplay.update()
        letsplay.draw(screen)
        pygame.display.flip()

    pygame.quit()

intro()

def main():

    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (X_MAX, Y_MAX))
    #theme = pygame.mixer.Sound("sounds/andromeda.wav").play(loops= 100)
    #theme.set_volume(0.2)

    all_sprites = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    asteroid_spawns = pygame.sprite.Group() 
    weaponfire = pygame.sprite.Group()

    ship = Spaceship(all_sprites, weaponfire)
    status = Status(ship)
    lose = Lose(ship, asteroids, asteroid_spawns, status)
    win = Win(ship, asteroids, asteroid_spawns, status)
    
    asteroids.add(Asteroid(), Asteroid2(), Asteroid3(), Asteroid4(), Asteroid5(), Asteroid6())
    asteroid_spawns.add(Bits(), Bits2(), Bits3())

    all_sprites.add(ship, status, asteroids, lose, win)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True 
            if not game_over:

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        ship.steer(DOWN, START)
                    if event.key == K_LEFT:
                        ship.steer(LEFT, START)
                    if event.key == K_RIGHT:
                        ship.steer(RIGHT, START)
                    if event.key == K_UP:
                        ship.steer(UP, START)
                    if event.key == K_SPACE:
                        ship.shoot(START)
                    # if event.key == K_RETURN and not ship.alive():
                    #     main()

                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        ship.steer(DOWN, STOP)
                    if event.key == K_LEFT:
                        ship.steer(LEFT, STOP)
                    if event.key == K_RIGHT:
                        ship.steer(RIGHT, STOP)
                    if event.key == K_UP:
                        ship.steer(UP, STOP)
                    if event.key == K_SPACE:
                        ship.shoot(STOP)

        hits = pygame.sprite.spritecollide(ship, asteroids, True)
        for hit in hits:
            pygame.mixer.Sound("sounds/houstonwearedown.wav").play() #change sound
            ship.health -= 10

        hits = pygame.sprite.spritecollide(ship, asteroid_spawns, True)
        for hit in hits:
            pygame.mixer.Sound("sounds/houstonwearedown.wav").play() #change sound
            ship.health -= 20

        for particle in weaponfire:
            hits = pygame.sprite.spritecollide(particle, asteroids, True)
            for hit in hits:
                pygame.mixer.Sound("sounds/greatshot.wav").play()
                weaponfire.remove(particle)
                all_sprites.remove(particle)
                ship.score += 10
                all_sprites.add(asteroid_spawns)

        for particle in weaponfire:
            hits = pygame.sprite.spritecollide(particle, asteroid_spawns, True)
            for hit in hits:
                pygame.mixer.Sound("sounds/greatshot.wav").play()
                weaponfire.remove(particle)
                all_sprites.remove(particle)
                ship.score += 15

        screen.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
