import pygame
from game import Game

pygame.init()



#générer la fenetre du jeu
pygame.display.set_caption("game", "./icone.png")
screen = pygame.display.set_mode((1280, 720))


#charger l'arriere plan de notre jeu
background = pygame.image.load('./background.jpg')
background = pygame.transform.scale(background, (1280, 720))

#charger le jeu
game = Game()


running = True

#boucle tant que cette condition est vrai
while running:
            
    #applique l'arriere plan du jeu
    screen.blit(background, (0, 0))
    
    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    
    #actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)
    
    #récuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
        
    #récupere les projectiles des monstres
    for projectile in game.monster.all_monster_projectiles:
        projectile.move()
        
    #appliquer le sprojectiles des monstres
    game.monster.all_monster_projectiles.draw(screen)
    #appliquer les projectiles
    game.player.all_projectiles.draw(screen)
    
    
    #récuperer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
        
    for projectile in game.monster.all_monster_projectiles:
        projectile.update_position()
    
    #appliquer l'ensemble des image du monstre
    game.all_monsters.draw(screen)

    
    #si le joueur souhaite se déplacer
    if game.pressed.get(pygame.K_d) and game.player.rect.x <1200:
        game.player.move_right()
    if game.pressed.get(pygame.K_q) and game.player.rect.x >0:
        game.player.move_left()
    if game.pressed.get(pygame.K_z) and game.player.rect.y > 50:
        game.player.move_up()
    if game.pressed.get(pygame.K_s) and game.player.rect.y < 640:
        game.player.move_down()
        
    
    
    #mettre l'écran à jour
    pygame.display.flip()
    
    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évênement est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #détecter si le joueur la une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #détecter si le clic gauche est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                game.monster.launch_projectile()
                #game.monster.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
            
    