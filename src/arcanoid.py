import sys, pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 1.2
        self.speed = [0.5, -0.5]
        
    def actualizar(self, time, pala_jug):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
            
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            

            
def load_image(filename, transparent=False):  
    try:
        image = pygame.image.load(filename)    
    except pygame.error as message:   
        print("Cannot load image: " + filename)
        raise SystemExit(message)    
    return image.convert_alpha()

class ovnis(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.image=pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y

class Pala(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.image=pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y
        self.speed = 0.5
 
    def mover(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcanoid")
 
    background_image = load_image('images/fondo.jpg')
    bola = Bola()
    pala_jug = Pala(2,1.1)
    ovni = ovnis(2,3)
 
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        bola.actualizar(time, pala_jug)
        pala_jug.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
        screen.blit(ovni.image, ovni.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()