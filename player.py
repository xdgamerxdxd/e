import pygame

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
        self.rect.x = 500
        self.rect.y = 540

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
