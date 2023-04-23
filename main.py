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
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2 - 5 , 0, 10, HEIGHT, ) # -5 to have rect in middle of screen

#how many frames to update at 
FPS = 60
VEL = 5 #velocity
BULLET_VEL = 7 
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

def yellow_handle_movement(keys_pressed, yellow):
    #check if move off screen 
    if keys_pressed[pygame.K_a] and yellow.x - VEL > BORDER.x + BORDER.width: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH: #right
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL

def draw_window(red, yellow):
    #draw on screen new color (doesnt update)
    WIN.fill((WHITE))
    pygame.draw.rect(WIN,BLACK, BORDER)
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

    bullets = [] #empty list
    
    clock = pygame.time.Clock()
    run = True
    while run: 
        #control speed of while loop, 60 times per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #end while loop and end game
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        draw_window(red, yellow)

    pygame.quit() 

#make sure that when file runs, it only runs
#main function if only ran this func directly

if __name__ == "__main__":
	main()