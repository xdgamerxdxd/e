import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

x = 1920 / 2
y = 1060


# Is player
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Player, self).__init__()

        # How make player is look like !!!
        # IMPORTANT!!!! mek self.image, or code not workl
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
                             # get rect woooooooo
        self.rect = self.image.get_rect()

    # moof the pleher
    def update(self):

        vel = 20

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= vel

        if keys[pygame.K_RIGHT] and self.rect.x < 1920 - self.rect.width:
            self.rect.x += vel

        # Make thing go up (Jump up)
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= vel

        if keys[pygame.K_DOWN] and self.rect.y < 1080 - self.rect.height:
            self.rect.y += vel


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()

        # How player looking is? with pictur
        self.image = pygame.image.load('filename.png').convert()

        self.image.set_colorkey((255, 255, 255))
                        # haha get rekt
        self.rect = self.image.get_rect()

    # mofe emeneh
    def update(self):

        vel = 20

        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= vel

        if keys[pygame.K_d] and self.rect.x < 1920 - self.rect.width:
            self.rect.x += vel

        # Make thing go up (Jump up)
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= vel

        if keys[pygame.K_s] and self.rect.y < 1080 - self.rect.height:
            self.rect.y += vel


# random thing list
custom_list = pygame.sprite.Group()

# list where random and also maybe player
all_sprites_list = pygame.sprite.Group()

# mak pleher
player = Player((255, 0, 0), 20, 20)
# mek enemeh
enemy = Player1()

# add enemeh to list
custom_list.add(enemy)

# add enemeh to this list also
all_sprites_list.add(enemy)

# edd pleher to thes lest
all_sprites_list.add(player)

# gib pleher and enemeh coords
player.rect.x = x
player.rect.y = y

enemy.rect.x = 1000
enemy.rect.y = 1060


clock = pygame.time.Clock()
running = True
while running:

    # if pleher make collide in enemeh it make die!
    enemy_hit_list = pygame.sprite.spritecollide(player, custom_list, False)

    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif keys[pygame.K_ESCAPE]:
            running = False

    # make things spawn in screen
    all_sprites_list.draw(screen)
    # update the thangs
    player.update()
    enemy.update()

    # if player collide enemy then mak plaher ded lol ezpz
    if pygame.sprite.spritecollideany(player, custom_list):
        player.kill()
    # player = pygame.draw.rect(screen, (255, 0, 0), (x, y, height, width))
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
