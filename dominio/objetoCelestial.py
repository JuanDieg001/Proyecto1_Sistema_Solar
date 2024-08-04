import pygame
import math
from abc import ABC, abstractmethod

class ObjetoCelestial(ABC):

    def __init__(self, image_path, mass, distance=0, orbit_speed=None):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self.mass = mass
        self._orbit_speed = 0  # Inicializa el atributo privado
        
        # Usa el setter para validar el valor inicial de orbit_speed
        if orbit_speed is not None:
            self.orbit_speed = orbit_speed

    @property
    def orbit_speed(self):
        return self._orbit_speed

    @orbit_speed.setter
    def orbit_speed(self, value):
        if 1 <= value <= 10:
            self._orbit_speed = value
        else:
            raise ValueError("Orbit value error")

    def update(self):
        self.angle += self.orbit_speed
        
    def draw(self, screen):
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        print(f"objeto:  {self.image_path}, Coor x: {x}, Coor y: {y}")
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)


    @abstractmethod
    def generate_magnetic_field(self, screen):
        pass

class Planeta(ObjetoCelestial):
    
    def __init__(self, image_path, distance, orbit_speed, mass, nucleo_status):
        
        super().__init__(image_path=image_path, mass=mass, distance=distance, orbit_speed=orbit_speed)
        self.nucleo_status = nucleo_status

        if self.mass > 200:
            self.blue_field = pygame.image.load("recursos/imagenes/campo_azul.png")
            self.blue_field = pygame.transform.scale(self.blue_field, (self.rect.width + 40, self.rect.height + 40))
            self.blue_field_rect = self.blue_field.get_rect()



    def generate_magnetic_field(self, screen):
        if self.nucleo_status == "Activate" and self.mass > 200:
            self.blue_field_rect.centerx = self.rect.centerx
            self.blue_field_rect.centery = self.rect.centery
            screen.blit(self.blue_field, self.blue_field_rect)

class Estrella(ObjetoCelestial):

    def __init__(self, image_path, mass, nucleo_status):

        super().__init__(image_path=image_path, mass=mass)
        self.nucleo_status = nucleo_status


        if self.mass > 1000:
            self.red_field = pygame.image.load("recursos/imagenes/campo_rojo.png").convert_alpha()
            width = self.rect.width + 90
            height = self.rect.height + 100
            self.red_field = pygame.transform.scale(self.red_field, (width, height))
            self.red_field_rect = self.red_field.get_rect()


    def generate_magnetic_field(self, screen):
        if self.nucleo_status == "Activate" and self.mass > 1000:
            self.red_field_rect.center = self.rect.center
            screen.blit(self.red_field, self.red_field_rect)

class Asteroide(ObjetoCelestial):
    
    def __init__(self, image_path, distance, orbit_speed, mass):
        
        super().__init__(image_path=image_path, distance=distance, orbit_speed=orbit_speed, mass=mass)
        
    def generate_magnetic_field(self, screen):
        pass