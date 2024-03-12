import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.flip()
all_sprites_list = pygame.sprite.Group()
# game var
gravity = 1
#colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
# Floors
floorList = pygame.sprite.Group()
class Floor(pygame.sprite.Sprite):
    def __init__(self,x,y,width, height,color):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

floor = Floor(0,0,600,50,BLACK)
floor.rect.x,floor.rect.y = 0,550
floorList.add(floor)
all_sprites_list.add(floor)
# player
playerList = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,width, height,color):
        super().__init__()
        self.x,self.y = x,y
        self.width,self.height = width, height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        # gravity
        self.hitground = False
        self.jumpHeight = 20
        self.jumping = False
        self.vel_y = self.jumpHeight
        pygame.draw.rect(self.image,self.color,pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height))

    def Movement(self):
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_a] or userInput[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 5
        if userInput[pygame.K_d] or userInput[pygame.K_RIGHT] and self.rect.x <= screen.get_width() - self.rect.width:
            self.rect.x += 5
        # jumping
        if self.hitground == True:
            if userInput[pygame.K_SPACE]:
                self.jumping = True
        else:
            self.rect.y += self.vel_y # fix this

        if self.jumping:
            self.rect.y -= self.vel_y
            self.vel_y -= gravity
            if self.vel_y < -self.jumpHeight:
                self.jumping = False
                self.vel_y = self.jumpHeight

player = Player(0,0,50,50,RED)
player.rect.x,player.rect.y = 300,300
playerList.add(player)
all_sprites_list.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    for player in playerList:
        player.Movement()
    if pygame.sprite.collide_mask(player, floor):
        player.hitground = True
    pygame.display.update()
    clock.tick(60)
