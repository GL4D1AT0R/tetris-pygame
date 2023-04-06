import pygame

#initialize pygame
pygame.init()

screen = pygame.display.set_mode((800,600)) #screen

#title and loop
pygame.display.set_caption("Space Invaders Made By Gyandev")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

def player(x,y):
    screen.blit(playerImg,(x, y))

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change=0;
#game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #KEY STROKES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    screen.fill((0, 0, 0)) #rgb 
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX>= 736:
        playerX = 736
    player(playerX, playerY )
    pygame.display.update()