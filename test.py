import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))


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
        # which way is player facing
        self.facing = ''
        # Is player alive????
        self.live = True

        self.atk = False

    # moof the pleher
    def update(self):

        vel = 20
        self.atk = False

        if self.live == True:

            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= vel
                self.facing = 'left'

            if keys[pygame.K_RIGHT] and self.rect.x < 1920 - self.rect.width:
                self.rect.x += vel
                self.facing = 'right'
            # Make thing go up (Jump up)
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= vel

            if keys[pygame.K_DOWN] and self.rect.y < 1080 - self.rect.height:
                self.rect.y += vel

# is enemeh or sth
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()

        # How player looking is? with pictur
        self.image = pygame.image.load('filename.png').convert()

        self.image.set_colorkey((255, 255, 255))
                        # haha get rekt
        self.rect = self.image.get_rect()
        self.facing = ''

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

# edd pleher to thes list
all_sprites_list.add(player)

# gib pleher and enemeh coords
player.rect.x = 500
player.rect.y = 590

enemy.rect.x = 1200
enemy.rect.y = 400


clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

running = True
while running:

    # if pleher make collide in enemeh it make die!
    # enemy_hit_list = pygame.sprite.spritecollide(player, custom_list, False)


    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 2
            text = str(counter).rjust(3) if counter > 0 else 'attack'
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False
    if keys[pygame.K_o] and counter < 0:
            counter = 10
    # make things spawn in screen
    all_sprites_list.draw(screen)
    # update the thangs
    player.update()
    enemy.update()

    # if player collide enemy then mak plaher ded lol ezpz also if attak is on then pleher is not die lulullu
    if pygame.sprite.spritecollideany(player, custom_list) and player.atk == False:
        player.kill()
        player.live = False
    if pygame.sprite.spritecollideany(player, custom_list) and player.atk == True:
        enemy.kill()
    screen.blit(font.render(text, True, (255, 230, 10)), (32, 48))
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
