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

ex = 1700
ey = 1050

ewidth = 30
eheight = 30

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

    enemy = pygame.draw.rect(screen, (20, 70, 230), (ex, ey, eheight, ewidth))

    if keys[pygame.K_z]:
        if facing == 'right':
            attack = pygame.draw.arc(screen, (255, 0, 0), (x + 20, y - 30, 25, 70), 11, 13.7, 3)
        else:
            attack = pygame.draw.arc(screen, (255, 0, 0), (x - 25, y - 30, 25, 70), 1.7, 4.7, 3)

    player = pygame.draw.rect(screen, (255, 0, 0), (x, y, height, width))
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
