import pygame


pygame.init()
tamanho  =  300,150
screen = pygame.display.set_mode(tamanho)


run = True
while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         screen.fill('LightSkyBlue')
         
         pygame.draw.rect(screen,'red',(125,50,50,50) ) 
         
        # LINHA 
         pygame.draw.line(screen,'red',(10,10), (150,30), 10 ) 
        # ELIPSE 
         pygame.draw.ellipse(screen, 'yellow', (170,30,150,40))
        # CIRCULO
         pygame.draw.circle(screen, 'blue', (200,70), 20)
         
         pygame.display.update()
         
pygame.quit()               
         
         
    


  



