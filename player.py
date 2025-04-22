import pygame
from projectile import Projectile

#créer la classe du joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('jeu/player/vaisseau-spatial.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 640
        
    def damage(self, amount):
        if self.healt - amount > amount:
            self.health -= amount
        
        
    def update_health_bar(self, surface):
        
        #dessiner la barre de vie
        pygame.draw.rect(surface, (45, 45, 49), [self.rect.x-20, self.rect.y-20, self.max_health, 5])
        pygame.draw.rect(surface, (8, 253, 0), [self.rect.x-20, self.rect.y-20, self.health, 5])
        
    def launch_projectile(self):
        
        #créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity
        
    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y -= self.velocity
        
    def move_down(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y += self.velocity