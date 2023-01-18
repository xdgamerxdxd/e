import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

vel = 20

# player stats

x = 1920 / 2
y = 1060

width = 20
height = 20

# Pretty self-explanatory
wants_jump = False
wants_down = False

# Which side is facing?
facing = ' '

# enemy stats

clock = pygame.time.Clock()
running = True
while running:

    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif keys[pygame.K_ESCAPE]:
            running = False

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        facing = 'left'

    if keys[pygame.K_RIGHT] and x < 1920 - width:
        x += vel
        facing = 'right'

    # Make thing go up (Jump up)
    if keys[pygame.K_UP] and y > 0 and wants_down == False:
        wants_jump = True
    if wants_jump == True and y > 900:
        y -= vel
    if wants_jump == True and y > 840:
        y -= vel / 2
    if wants_jump == True and y > 800:
        y -= vel / 4
    if y == 800:
        wants_jump = False
        wants_down = True

    # Make thing to down (Fall down)
    if wants_down == True and y < 1060:
        y += vel
        if y == 1060:
            wants_down = False

    player = pygame.draw.rect(screen, (255, 0, 0), (x, y, height, width))
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
