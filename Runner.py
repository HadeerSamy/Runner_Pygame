import pygame
from sys import exit
#1- we have to init the pygame
pygame.init()

#2- set a display surface
screen = pygame.display.set_mode((800,400))

#the name of the program
pygame.display.set_caption("Game")

#we need to create a clock object to make a cieling and floor to the speed of the game (frame per second FPS)
clock = pygame.time.Clock()

#to create surface image / we convert to change the png to something pygame can work faster with
sky_surface = pygame.image.load("graphics\Sky.png").convert()
ground_surface = pygame.image.load("graphics\ground.png").convert()

snail_surface = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(800,250))

player1_surface = pygame.image.load("graphics\Player\player_walk_1.png").convert_alpha()
player1_rect = player1_surface.get_rect(bottomleft=(0,250))



#to create surface color
# test = pygame.Surface((400,200))
# test.fill("yellow")

#to create surface text: 1.create font / 2.create text / 3. put it on screen
testFont  = pygame.font.Font("font\Pixeltype.ttf",50)
#second parameter is aliasing but since we're working with pixel art then it'd be false
score_surface = testFont.render("HEllO", False,"black")
score_rect = score_surface.get_rect(center = (400,30))


gravity = 0

while True:

    #to be able to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #to finish the code and not continue, we could use break statement but exit() is more secure
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity -= 20
                

                print("jump")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player1_rect.collidepoint(event.pos):
                gravity -= 20
                print("hello")

    #to add surface on our display surface        
    #screen.blit(surface, position)
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    pygame.draw.rect(screen, "pink", score_rect)


    screen.blit(score_surface,score_rect)
    # pygame.draw.line(screen, "purple", (0,0), (800,400), 5)

    # gravity += 1
    player1_rect.y += gravity
    screen.blit(player1_surface,player1_rect)
    # player1_rect.left += 5
    # if player1_rect.left >=800:
    #     player1_rect.left = 0


    screen.blit(snail_surface,snail_rect)
    snail_rect.left -= 5 
    if snail_rect.left <=0:
        snail_rect.left = 800


    if(player1_rect.colliderect(snail_rect)):
        score_surface = testFont.render("Collide", False,"blue")
    else:
        score_surface = testFont.render("HEllO", False,"black")

    mouse_pos = pygame.mouse.get_pos()
    if(player1_rect.collidepoint(mouse_pos)):
        score_surface = testFont.render("mousy", False,"red")
    keys = pygame.key.get_pressed()

    # if keys[pygame.K_SPACE]:
    #     print("hii")
    #     score_surface = testFont.render("jump", False,"black")

    #to keep updating the frames
    pygame.display.update()

    #to insure that the loop won't run faster than 60 FPS => we set the max
    #but for the minimum then we should simplify the game
    clock.tick(60)