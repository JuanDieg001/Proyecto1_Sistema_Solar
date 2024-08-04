import pygame

from dominio.objetoCelestial import Estrella, Planeta, Asteroide

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

image_base_path = 'recursos/imagenes/'

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sistema solar")

sun = Estrella(image_path=image_base_path + "sol.png", mass= 2000, nucleo_status= "Activate")
mercury = Planeta(image_path=image_base_path + "mercurio.png", distance= 150, orbit_speed= 2, mass= 50, nucleo_status="Inactive")
mars = Planeta(image_path=image_base_path + "marte.png", distance= 220, orbit_speed= 1, mass= 250, nucleo_status="Activate")
asteroid = Asteroide(image_path=image_base_path + "asteroide.png", distance= 150, orbit_speed= 1, mass= 20)

background_image = pygame.image.load("recursos/imagenes/fondo.png").convert()
background_react = background_image.get_rect()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.blit(background_image, background_react)
    sun.draw(screen)
    mercury.draw(screen)
    mars.draw(screen)
    asteroid.draw(screen)

    mars.generate_magnetic_field(screen)
    sun.generate_magnetic_field(screen)

    sun.update()
    mercury.update()
    mars.update()
    asteroid.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
