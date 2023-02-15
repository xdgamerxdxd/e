import pygame
from player import Player

pygame.init()

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.entitymove()

    def entitymove(self):
        self.player = Player((255,255,255), 20, 20)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)

    def run(self):
        keys = pygame.key.get_pressed()
        self.all_sprite_list.draw(self.screen)
        self.player.update()
        if keys[pygame.K_ESCAPE]:
            self.running = False

def main():

    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    game = Game(screen)
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.run()

        pygame.display.update()
        clock.tick(60)
        screen.fill((14, 14, 17))

    pygame.quit()
main()