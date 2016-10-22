import sys, pygame
from pygame.locals import *
from string import punctuation
import time
WIDTH = 640
HEIGHT = 480
def Ganar(self):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcanoid")
    pygame.display.set_icon(pygame.image.load('images/ball.png'))
 
    background_image = load_image('images/win.png')
    sonido = pygame.mixer.Sound("images/gameover.mp3")
    sonido.play()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        p_jug, p_jug_rect = texto('Has ganado para volver a jugar presiona enter', WIDTH/2, HEIGHT/1.1)
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
            pygame.init()
            main()
        screen.blit(p_jug, p_jug_rect)
        pygame.display.flip()
    pygame.init()
    main()
def Menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcanoid")
    pygame.display.set_icon(pygame.image.load('images/ball.png'))
 
    background_image = load_image('images/start.png')
    sonido = pygame.mixer.Sound("images/gameover.mp3")
    sonido.play()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        p_jug, p_jug_rect = texto('Para jugar presiona enter', WIDTH/2, HEIGHT/1.1)
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
            pygame.init()
            main()
        screen.blit(p_jug, p_jug_rect)
        pygame.display.flip()
    pygame.init()
    main()
def gameover(self):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcanoid")
    pygame.display.set_icon(pygame.image.load('images/ball.png'))
 
    background_image = load_image('images/gameover.jpg')
    sonido = pygame.mixer.Sound("images/gameover.mp3")
    sonido.play()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        p_jug, p_jug_rect = texto('Para volver a jugar Porfavor presiona enter', WIDTH/2, HEIGHT/1.1)
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
            pygame.init()
            main()
        screen.blit(p_jug, p_jug_rect)
        pygame.display.flip()
    pygame.init()
    main()
    
class Bola(pygame.sprite.Sprite):
    suma=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 1.2
        self.speed = [0.4, -0.4]
        
    def actualizar(self,time, pala_jug, ovni1,ovni2,ovni3,ovni4,ovni5,ovni6,ovni7,ovni8,ovni9,ovni10,ovni11,ovni12,ovni13,ovni14,ovni15,punto):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        
        if self.rect.bottom >= 470:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
            punto = punto-1
            if punto==0:
                pygame.mixer.music.stop()
                gameover(self)

                
        
        if self.rect.left <= 10 or self.rect.right >= 490:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 10:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
            
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            
            
        if pygame.sprite.collide_rect(self, ovni1):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni1.move(10000,10000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self)            
                        
        if pygame.sprite.collide_rect(self, ovni2):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni2.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni3):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni3.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 

        if pygame.sprite.collide_rect(self, ovni4):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni4.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni5):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni5.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni6):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni6.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni7):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni7.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni8):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni8.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 

        if pygame.sprite.collide_rect(self, ovni9):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni9.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni10):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni10.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
        
        if pygame.sprite.collide_rect(self, ovni11):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni11.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni12):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni12.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni13):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni13.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 

        if pygame.sprite.collide_rect(self, ovni14):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni14.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
            
        if pygame.sprite.collide_rect(self, ovni15):
            self.speed[1] = -self.speed[1]
            self.rect.centerx += -self.speed[0] * time
            ovni15.move(1000,1000)
            self.suma=self.suma+1;
            if self.suma==15:
                Ganar(self) 
        return punto
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
        self.image = load_image("images/ovni.gif")
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y
        
    def move(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

class Pala(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/plataforma.gif")
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y
        self.speed = 0.5
 
    def mover(self, time, keys):
        if self.rect.left >= 10:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= 488:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
                
def texto(texto, posx, posy, color=(255, 0, 0)):
    fuente = pygame.font.Font('images/DroidSans.ttf', 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcanoid")
 
    background_image = load_image('images/fondo.png')
    pygame.display.set_icon(pygame.image.load('images/ball.png'))
    bola = Bola()
    pala_jug = Pala(2.7,1.1)
    
    ovni1 = ovnis(10,3)
    ovni2 = ovnis(10,4)
    ovni3 = ovnis(10,6)
    
    ovni4 = ovnis(4,3)
    ovni5 = ovnis(4,4)
    ovni6 = ovnis(4,6)
    
    ovni7 = ovnis(2.5,3)
    ovni8 = ovnis(2.5,4)
    ovni9 = ovnis(2.5,6)
 
    ovni10 = ovnis(1.8,3)
    ovni11 = ovnis(1.8,4)
    ovni12 = ovnis(1.8,6)
    
    ovni13 = ovnis(1.45,3)
    ovni14 = ovnis(1.45,4)
    ovni15 = ovnis(1.45,6)
    
    clock = pygame.time.Clock()
    global punto
    punto = 3
    pygame.mixer.music.load("images/arcanoid.mp3")
    pygame.mixer.music.play(10000)
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        punto=bola.actualizar(time, pala_jug, ovni1,ovni2,ovni3,ovni4,ovni5,ovni6,ovni7,ovni8,ovni9,ovni10,ovni11,ovni12,ovni13,ovni14,ovni15,punto)
        pala_jug.mover(time, keys)
        
        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
        screen.blit(ovni1.image, ovni1.rect)
        screen.blit(ovni2.image, ovni2.rect)
        screen.blit(ovni3.image, ovni3.rect)
        screen.blit(ovni4.image, ovni4.rect)
        screen.blit(ovni5.image, ovni5.rect)
        screen.blit(ovni6.image, ovni6.rect)
        screen.blit(ovni7.image, ovni7.rect)
        screen.blit(ovni8.image, ovni8.rect)
        screen.blit(ovni9.image, ovni9.rect)
        screen.blit(ovni10.image, ovni10.rect)
        screen.blit(ovni11.image, ovni11.rect)
        screen.blit(ovni12.image, ovni12.rect)
        screen.blit(ovni13.image, ovni13.rect)
        screen.blit(ovni14.image, ovni14.rect)
        screen.blit(ovni15.image, ovni15.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        p_jug, p_jug_rect = texto('vidas: '+str(punto), WIDTH/1.15, 60)
        screen.blit(p_jug, p_jug_rect)
        
        pygame.display.flip()

    return 0
 
if __name__ == '__main__':
    pygame.init()
    Menu()