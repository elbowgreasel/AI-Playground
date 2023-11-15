import pygame
from sys import exit
## starts pygame engine
pygame.init()
## display service: window/screen players going to see
## default w=800, h=400
width = 800
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('THE_GREASE')
## creats a clock to keep track of frames per second
clock = pygame.time.Clock()

surface_width = 100
surface_height = 200

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
test_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = test_font.render('My game', False, 'Green')
text_rect = text_surface.get_rect(center = (screen.get_width()*.5, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50,300))
## runs the game while true, 
gravity = 0
force = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                force = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                force = 0
    ## LOST IN THE SAUCE, MIGHT NEED TO CHANGE A FEW THINGS RIGHT NOW KEYUP IS CHANGING THE GAIN
    ## THINKING ABOUT LOOPING OVER EVERY STATUS, BUT ACTIONS ARE IN STATUS MIGHT NEED TO SEPERATE AGAIN...
    if force > 0:
        gravity += force
        force -= 1
    if gravity > -4:
        gravity = max(-4, gravity - 4)
    screen.blit(test_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,text_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    ## player
    if player_rect.bottom <= 300:
        if player_rect.bottom + -gravity > 300:
            player_rect.y = player_rect.y = 300 - player_rect.height
        else:
            player_rect = player_rect.move(0, -gravity)
    screen.blit(player_surface,player_rect)
    # draw all element
    # update everything
    pygame.display.update()
    clock.tick(60)
