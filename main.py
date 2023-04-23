import pygame
import os

#need a main surface 


WIDTH, HEIGHT = 900, 500 
#make new window of height and width
#constant values in all capitals 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#change window name
pygame.display.set_caption("First Game!")

WHITE = (255,255,255)

#how many frames to update at 
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

def draw_window(red, yellow):
    #draw on screen new color (doesnt update)
    WIN.fill((WHITE))
    #blit is for text or images
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #x and y from rect
    WIN.blit(RED_SPACESHIP, (red.x , red.y))
    #update display manual
    pygame.display.update()


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#scale image
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
def main(): 
    #x,y,width,height for Rect
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT )
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT )

    clock = pygame.time.Clock()
    run = True
    while run: 
        #control speed of while loop, 60 times per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #end while loop and end game
                run = False
        keys_pressed = pygame.key.get_pressed
         
        draw_window(red, yellow)

    pygame.quit() 

#make sure that when file runs, it only runs
#main function if only ran this func directly

if __name__ == "__main__":
	main()