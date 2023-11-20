import pygame
from sys import exit
## starts pygame engine
pygame.init()
## display service: window/screen players going to see
## default w=800, h=400
start_time = 0
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (450, 50))
    screen.blit(score_surf, score_rect)

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

# text_surface = test_font.render('My game', False, 'Green')
# text_rect = text_surface.get_rect(center = (screen.get_width()*.5, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (600, 300))

# player surfaces
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50,300))
## runs the game while true, 
gravity = 0
force = 0
speed = 0
game_active = True
active_keys = {
    'a': False,
    'd': False
}
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    force = 10
                if event.key == pygame.K_d:
                    speed = 5
                    active_keys['d'] = True
                if event.key == pygame.K_a:
                    speed = -5
                    active_keys['a'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    force = 0
                if event.key == pygame.K_d:
                    if not active_keys['a']:
                        speed = 0
                    active_keys['d'] = False
                if event.key == pygame.K_a:
                    if not active_keys['d']:
                        speed = 0
                    active_keys['a'] = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                player_rect.bottom = 300
                player_rect.left = 50
                start_time = int(pygame.time.get_ticks() / 1000)
                game_active = True
                
    if game_active:
        if force > 0:
            gravity += force
            force -= 1
        if gravity > -3:
            gravity = max(-3, gravity - 3)
        screen.blit(test_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # screen.blit(text_surface,text_rect)
        display_score()
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)
        ## player
        # needs updating
        player_rect = player_rect.move(speed, -gravity)
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > width:
            player_rect.right = width
        screen.blit(player_surface,player_rect)
        if snail_rect.colliderect(player_rect):
            game_active = False


    # draw all element
    # update everything
    pygame.display.update()
    clock.tick(60)
