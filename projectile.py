import pygame

#définir la classe qui va gérer les projectiles du joueur
class Projectile(pygame.sprite.Sprite):
    
    #définir le constructeur de la classe
    def __init__(self, player):
            super().__init__()
            self.velocity = 1
            self.player = player
            self.image = pygame.image.load('jeu/projectiles/blue_shots/blue_shot_1.png')
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect()
            self.rect.x = player.rect.x + 5
            self.rect.y = player.rect.y - 20
            
                  
            
    def remove(self):
        self.player.all_projectiles.remove(self)
        
        
    def move(self):
        self.rect.y -= self.velocity
        if self.rect.y > 600:
                self.image = pygame.image.load('jeu/projectiles/blue_shots/blue_shot_1.png')
        elif self.rect.y > 400:
            self.image = pygame.image.load('jeu/projectiles/blue_shots/blue_shot_2.png')
        elif self.rect.y > 200:
            self.image = pygame.image.load('jeu/projectiles/blue_shots/blue_shot_3.png')
        elif self.rect.y > 50:
            self.image = pygame.image.load('jeu/projectiles/blue_shots/blue_shot_4.png')
            
        #vérifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)
        
        #vérifier si le projectile n'est plus sur l'écran
        if self.rect.y < 0:
            #supprimer le projectile
            self.remove()

