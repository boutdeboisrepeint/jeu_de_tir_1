import pygame
from random import *
from monster_projectile import Monster_proj


#créer une classe pour gérer la notion de monstre
class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.all_monster_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('./monstres/monstre.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(300, 1000)
        self.rect.y = 100
        self.velocity = 1
        
    def damage(self, amount):
        #infliger les dégats
        self.health -= amount
        
        #vérifier si il est mort
        if self.health <= 0:
            #réapparaitre comme un nouveau monstre
            self.rect.x = randint(200, 1000)
            self.rect.y = randint(50, 300)
            self.health = 100
            
    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_monster_projectiles.add(Monster_proj(self))
        
        
    def update_health_bar(self, surface):
        
        #dessiner la barre de vie
        pygame.draw.rect(surface, (45, 45, 49), [self.rect.x-10, self.rect.y+100, self.max_health, 5])
        pygame.draw.rect(surface, (8, 253, 0), [self.rect.x-10, self.rect.y+100, self.health, 5])
        
        
    def forward(self):
        #if not self.game.check_collision(self, self.game.all_players):
        self.rect.x -= self.velocity
        if self.rect.x <= 200 or self.rect.x >= 1000:
            self.velocity = -self.velocity

        #else:
            #self.rect.x += self.velocity
        
        