import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos + 288,450))

def create_pipe():
    new_pipe = pipe_surface.get_rect( midtop = (600,256))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes 

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)


pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

 
# Game Variables 
gravity = 0.20
bird_movement = 0


bg_surface = pygame.image.load('assets/background-day.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
#floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
#bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface = pygame.image.load('assets/pipe-green.png')
#pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

                



    screen.blit(bg_surface,(0,0))

    # bird

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)
    
    # pipes 
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)


    # floor 
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0
    
    
    pygame.display.update()
    clock.tick(120)
