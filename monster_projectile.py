import pygame

class Monster_proj(pygame.sprite.Sprite):
    
    def __init__(self, monster):
        super().__init__()
        self.velocity = 1
        self.monster = monster
        self.image = pygame.image.load('./projectiles/monster_shot.png')
        self.image = pygame.transform.rotozoom(self.image, 270, 1)
        self.rect = self.image.get_rect()
        self.rect.x = monster.rect.x
        self.rect.y = monster.rect.y
        
    def update_position(self):
        #met à jour la position du projectile
        self.rect.x = self.monster.rect.x
        self.rect.y = self.monster.rect.y
        
        
    def move(self):
        self.rect.y += self.velocity
        
        #for player in self.player.game.check_collision()
        #if self.player.check_collision
        
        #vérifier si le projectile n'est plus sur l'écran
        if self.rect.y > 720:
            #supprimer le projectile
            self.remove()