import sys, pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

def load_image(filename, transparent=False):  
    try:
        image = pygame.image.load(filename)    
    except pygame.error as message:   
        print("Cannot load image: " + filename)
        raise SystemExit(message)    
    return image.convert_alpha()
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
 
    background_image = load_image('images/fondo.jpg')
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()