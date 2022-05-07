from turtle import up
import pygame 

pygame.init()

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("第一个游戏")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedx = 13
        self.speedy = 10

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d] :
            self.rect.x += self.speedx

        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx

        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w] :
            self.rect.y -= self.speedy

        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            self.rect.y += self.speedy    
        
        if key_pressed[pygame.K_LEFT] and key_pressed[pygame.K_UP]:
            self.rect.x -= self.speedx
            self.rect.y -= self.speedy
        
        if key_pressed[pygame.K_LEFT] and key_pressed[pygame.K_DOWN]:
            self.rect.x -= self.speedx
            self.rect.y += self.speedy
        
        if key_pressed[pygame.K_RIGHT] and key_pressed[pygame.K_UP]:
            self.rect.x += self.speedx
            self.rect.y -= self.speedy
        
        if key_pressed[pygame.K_RIGHT] and key_pressed[pygame.K_DOWN]:
            self.rect.x += self.speedx
            self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 游戏循环
running = True
while running:
    # 取得输入
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏
    all_sprites.update()

    # 画面显示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()