#sys permite cerrar la ventana, random permite obtener numeros aleatorios
import pygame, sys, random

#Dimensiones de la ventana (tupla)
SCREEN_ANCHO = 800
SCREEN_ALTO = 500
#FPS
FPS = 60
#Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
#Algunos conceptos
POS_INICIAL = ([(SCREEN_ANCHO // 2), (SCREEN_ALTO // 2)])

#Preferencias del snake
class Snake(pygame.sprite.Sprite):
	#Sprite del snake
	def __init__(self):
		super().__init__()
		#Caracteristicas visuales del snake
		self.image = pygame.image.load("head_right.png").convert()
		self.image.set_colorkey(BLANCO)
		#Obtiene el rectangulo de la imagen para manipularlo
		self.rect = self.image.get_rect()
		#Centro la posicion
		self.rect.center = POS_INICIAL
		#Velocidad inicial
		self.X_vel = 0
		self.Y_vel = 0

	def cambio_velocidad(self, x, y):
		self.X_vel += x
		self.Y_vel += y

	def update(self):
		#Actualiza esto cada vuelta del bucle
		self.rect.x += self.X_vel
		self.rect.y += self.Y_vel
		
		#if self.rect.top > alto  pos alta
			#self.rect.bottom = 0  pos baja

#class Fruta (pygame.sprite.Sprite):

#inicializo pygame
pygame.init()
#Crear ventana
screen = pygame.display.set_mode([SCREEN_ANCHO, SCREEN_ALTO])
#Definir reloj, controla los FPS 
clock = pygame.time.Clock()
#Fondo
fondo = pygame.image.load("fondo.png").convert()
#Conceptos previos
perdedor = False
puntos = 0

#Grupo de sprites, para agruparlos en la variable, inicializacion del snake y lo agregamos al sprite
snake_list = pygame.sprite.Group()
#fruta_list = pygame.sprite.Group()
todos_sprites_list = pygame.sprite.Group()

snake = Snake()
snake_list.add(snake)
todos_sprites_list.add(snake)

#Bucle principal, monitoreo de los eventos principales
while not perdedor:
	for event in pygame.event.get():
		#Cerrando y terminando el bucle
		if event.type == pygame.QUIT:
			perdedor = True

		#Eventos del teclado
		if event.type == pygame.KEYDOWN:
			#PRESIONO LA TECLA
			if event.key == pygame.K_UP:
				snake.cambio_velocidad(0, -3)
			if event.key == pygame.K_DOWN:
				snake.cambio_velocidad(0, 3)
			if event.key == pygame.K_LEFT:
				snake.cambio_velocidad(-3, 0)
			if event.key == pygame.K_RIGHT:
				snake.cambio_velocidad(3, 0)
		if event.type == pygame.KEYUP:
			#DEJO DE PRESIONAR LA TECLA
			if event.key == pygame.K_UP:
				snake.cambio_velocidad(0, -3)
			if event.key == pygame.K_DOWN:
				snake.cambio_velocidad(0, 3)
			if event.key == pygame.K_LEFT:
				snake.cambio_velocidad(-3, 0)
			if event.key == pygame.K_RIGHT:
				snake.cambio_velocidad(3, 0)

	#Actualizacion del sprites
	todos_sprites_list.update()

	#Definir el fondo		
	screen.blit(fondo, [0, 0])

	#Dibujo
	todos_sprites_list.draw(screen)

	#Actualizarr pantalla
	pygame.display.flip()
	#Configurar reloj, en FPS, su velocidad
	clock.tick(FPS)
pygame.quit()