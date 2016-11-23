import pygame, random
pygame.init();

from pygame.locals import QUIT, K_ESCAPE, KEYDOWN, K_DOWN, K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL

X_MAX, Y_MAX = 800, 600

speed1 = [4,4]
speed2 = [5,5]
speed3 = [1,1]
speed4 = [3,3]
speed5 = [2,2]
speed6 = [6,6]

LEFT, RIGHT, UP, DOWN = 0, 1, 3, 4
START, STOP = 0, 1


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load("images/asteroid_lg_1.png").convert_alpha()
        #self.size = self.image.get_size()
        #self.image = pygame.transform.smoothscale(self.image, (int(self.size[0]/5), int(self.size[1]/5)))
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = init_x = random.randint(0+60, 800-60)
        self.y = init_y = random.randint(0+60,600-60)
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.left < 0 or self.rect.right > X_MAX:
            speed1[0] = -speed1[0]
        if self.rect.top < 0 or self.rect.bottom > Y_MAX:
            speed1[1] = -speed1[1]

        self.rect = self.rect.move(speed1)

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

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load("images/spaceship.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (55, 75))
        self.rect = self.image.get_rect() 
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.dx = self.dy = 0
        self.autopilot = False
        self.in_position = False
        self.velocity = 0
        self.health = 100
        self.score = 0


    def update(self):
        x, y = self.rect.center

        if not self.autopilot:
            self.rect.center = x + self.dx, y + self.dy

        else:
            if not self.in_position:
                if x != X_MAX/2:
                    x += (abs(X_MAX/2 - x)/(X_MAX/2 - x)) * 2
                if y != Y_MAX/2:
                    y += (abs(Y_MAX/2 - y)/(Y_MAX/2 - y)) * 2

                if x == X_MAX/2 and y == Y_MAX/2:
                    self.in_position = True
            else:
                y -= self.velocity
                self.velocity *= 1.5
                if y <= 0:
                    y = -30
            self.rect.center = x, y

            #edit so that spaceship can't hide out beyond the screen

    def steer(self, direction, operation):
        v = 10
        if operation == START:
            if direction in (UP, DOWN):
                self.dy = {UP: -v, DOWN: v}[direction]
                if direction == UP:
                    self.image = pygame.image.load("images/spaceship.png").convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (55, 75))

                if direction == DOWN:
                    self.image = pygame.image.load("images/spaceship_d.png").convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (55, 75))

            if direction in (LEFT, RIGHT):
                self.dx = {LEFT: -v, RIGHT: v}[direction]
                if direction == RIGHT:
                    self.image = pygame.image.load("images/spaceship_r.png").convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (75, 55))

                if direction == LEFT:
                    self.image = pygame.image.load("images/spaceship_l.png").convert_alpha()
                    self.image = pygame.transform.smoothscale(self.image, (75, 55))                    

        #edit this so that no movement can result from two or more keys pressed simultaneously

        if operation == STOP:
            if direction in (UP, DOWN):
                self.dy = 0
            if direction in (LEFT, RIGHT):
                self.dx = 0

    def shoot(self, operation):
        if operation == START:
            self.firing = True
        if operation == STOP:
            self.firing == False

#Bullet class

class Status(pygame.sprite.Sprite):
    def __init__(self, ship):
        super(Status, self).__init__()
        self.image = pygame.Surface((X_MAX, 30))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = 25, Y_MAX
        self.font = pygame.font.Font("ScreenMatrix.ttf", 22)
        self.ship = ship

    def update(self):
        score = self.font.render("Health : {} Score : {}".format(
            self.ship.health, self.ship.score), True, (255, 255, 255)) 
        self.image.fill((0, 0, 0))
        self.image.blit(score, (0, 0))
        self.image.set_colorkey((0, 0, 0))

class Lose(pygame.sprite.Sprite):
    def __init__(self, ship):
        super(Lose, self).__init__()
        self.image = pygame.Surface((200, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (X_MAX/2, Y_MAX/2)
        self.font = pygame.font.Font("ScreenMatrix.ttf", 33)
        self.ship = ship

    def update(self):
        sorry = self.font.render("GAME OVER", True, (255, 255, 255))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        if self.ship.health < 0:
            self.image.blit(sorry, (20, 40))
            self.ship.kill()
             
#in a similar fashion as the Lose and Status objects, I'll add Start and Win objects


def main():

    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    pygame.display.set_caption("Andromeda")  

    background = pygame.image.load('images/background1.jpg').convert()
    background = pygame.transform.scale(background, (X_MAX, Y_MAX))

    all_sprites = pygame.sprite.Group() #list of all sprites
    asteroids = pygame.sprite.Group() #list of all asteroids

    ship = Spaceship()
    status = Status(ship)
    lose = Lose(ship)

    asteroids.add(Asteroid(0,0), Asteroid2(0,0), Asteroid3(0,0), Asteroid4(0,0), Asteroid5(0,0), Asteroid6(0,0))

    all_sprites.add(ship, status, lose, asteroids)

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
                    if event.key == K_LCTRL:
                        ship.shoot(START)

                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        ship.steer(DOWN, STOP)
                    if event.key == K_LEFT:
                        ship.steer(LEFT, STOP)
                    if event.key == K_RIGHT:
                        ship.steer(RIGHT, STOP)
                    if event.key == K_UP:
                        ship.steer(UP, STOP)
                    #modify so that pressing two or more keys results in no movement
                    if event.key == K_LCTRL:
                        ship.shoot(STOP)

        hits = pygame.sprite.spritecollide(ship, asteroids, True)
        for hit in hits:
            ship.health -= 20

        # hits = pygame.sprite.spritecollide(asteroids, weaponfire, True)
        # for hit in hits:
        #     ship.score += 10

        screen.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

main()
