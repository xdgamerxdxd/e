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

       # get rect woooooooo //// Gives player a hitbok
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


class Meele_attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Meele_attack, self).__init__()
        
        self.image = pygame.image.load('nowepon.png')
        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()


    def update(self):

        self.atk = False
        self.image = pygame.image.load('nowepon.png')

        if keys[pygame.K_o]:
            if player.facing == 'right':
                self.image = pygame.image.load('swor.png')
                self.image = pygame.transform.scale(self.image, (150, 100))
                self.rect = self.image.get_rect()
                self.rect.x = player.rect.x + 40
                self.rect.y = player.rect.y - 50
                self.atk = True
            else:
                self.image = pygame.image.load('swol.png')
                self.image = pygame.transform.scale(self.image, (150, 100))
                self.rect = self.image.get_rect()
                self.rect.x = player.rect.x - 200
                self.rect.y = player.rect.y - 50
                self.atk = True
            
        
        


# make attak
class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super(Attack, self).__init__()

        self.image = pygame.image.load('nowepon.png')

        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()

        self.on = False
        self.count = False
        self.counter = 10
        self.facing = ''

    def update(self):

        # what attack looks like without pushing button
        self.image = pygame.image.load('nowepon.png')

        # which way is attack facing
        if player.facing == 'right' and self.count == False:
            self.rect.x = player.rect.x + 50
        if player.facing == 'left' and self.count == False:
            self.rect.x = player.rect.x - 55

        if keys[pygame.K_i] and self.count == False:
            self.count = True
            self.on = True
            self.counter = 10
            self.rect.y = player.rect.y - 40
            if player.facing == 'right':
                self.facing = 'right'
            else:
                self.facing = 'left'

        if self.count == True:
            self.image = pygame.image.load('san_attack.png')
            self.counter -= 1
            if self.facing == 'right':
                self.rect.x += 20
            if self.facing == 'left':
                self.rect.x -= 20

        if self.counter == -10:
            self.count = False
            self.on = False


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
        self.live = True

    # mofe emeneh
    def update(self):

        vel = 20
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= vel
            self.facing = 'left'

        if keys[pygame.K_d] and self.rect.x < 1920 - self.rect.width:
            self.rect.x += vel
            self.facing = 'right'

        # Make thing go up (Jump up)
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= vel

        if keys[pygame.K_s] and self.rect.y < 1080 - self.rect.height:
            self.rect.y += vel
        
        if self.facing == 'right':
            self.image = pygame.image.load('filenamel.png')
            
        if self.facing == 'left':
            self.image = pygame.image.load('filename.png')
            

# random thing list
custom_list = pygame.sprite.Group()

# list where random and also maybe player
all_sprites_list = pygame.sprite.Group()

attack_list = pygame.sprite.Group()

# mak pleher
player = Player((255, 0, 0), 20, 20)
# mek enemeh
enemy = Player1()

attack = Attack()

matk = Meele_attack()

attack_list.add(attack)

attack_list.add(matk)
 
# add enemeh to list
custom_list.add(enemy)

# add enemeh to this list also
all_sprites_list.add(enemy)

# edd pleher to thes list
all_sprites_list.add(player)

all_sprites_list.add(attack)

all_sprites_list.add(matk)

# gib pleher and enemeh coords
e = player.rect.x = 500
r = player.rect.y = 590

enemy.rect.x = 1200
enemy.rect.y = 400

clock = pygame.time.Clock()

keys = pygame.key.get_pressed()

running = True
while running:

    # if pleher make collide in enemeh it make die!
    # enemy_hit_list = pygame.sprite.spritecollide(player, custom_list, False)

    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            player.live = True
            enemy.live = True


    # make things spawn in screen
    all_sprites_list.draw(screen)

    # update the thangs
    if player.live == True:
        player.update()
        attack.update()
        matk.update()
    enemy.update()

    if player.live == False:
        matk.image = pygame.image.load('nowepon.png')
        matk.atk = False
    # if player collide enemy then mak plaher ded lol ezpz also if attak is on then pleher is not die lulullu
    if pygame.sprite.spritecollideany(player, custom_list) and player.atk == False:
        player.kill()
        player.live = False

    if pygame.sprite.spritecollideany(attack, custom_list) and attack.on == True or pygame.sprite.spritecollideany(matk, custom_list) and matk.atk == True:
        enemy.kill()
        enemy.live = False

    clock.tick(30)
    pygame.display.flip()
pygame.quit()
