'''
Juego de Snake.
Participantes: Maria Sol Alcaraz
			   Franco Medina
			   Damian Palomba
'''

import pygame, sys, random

<<<<<<< HEAD
#Pantalla
#Cuadrados de 20x20, 25 de alto, 40 de ancho
ANCHO = 800 
ALTO = 500
CUADROS = 20
=======
#Dimensiones de la ventana (tupla)
SCREEN_ANCHO = 800
SCREEN_ALTO = 500
#FPS
FPS = 30
>>>>>>> d0b56c0b36d19b70e3673fb26fd5e7b3ecd3e911
#Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_CUERPO = (0, 255, 255)
COLOR_FRUTA = (255, 200, 0)
#Direcciones
IZQUIERDA = (-1, 0)
DERECHA = (1, 0)
ARRIBA =(0, -1)
ABAJO = (0, 1)
#Preferencias
POS_INICIAL = [((ANCHO // 2), (ALTO // 2))]
LARGO_MAX = 10
FPS = 60
comenzar = "Yy"

#Preferencias del snake
class Snake(pygame.sprite.Sprite):
	def __init__(self):
		#Caracteristicas visuales del snake
		self.imagen_izq = pygame.image.load("cabeza_izquierda.png").convert()
		self.imagen_izq.set_colorkey(BLANCO)
		self.imagen_der = pygame.image.load("cabeza_derecha.png").convert()
		self.imagen_der.set_colorkey(BLANCO)
		self.imagen_up = pygame.image.load("cabeza_arriba.png").convert()
		self.imagen_up.set_colorkey(BLANCO)
		self.imagen_down = pygame.image.load("cabeza_abajo.png").convert()
		self.imagen_down.set_colorkey(BLANCO)

		self.rect_izq = self.imagen_izq.get_rect()
		self.rect_der = self.imagen_der.get_rect()
		self.rect_up = self.imagen_up.get_rect()
		self.rect_down = self.imagen_down.get_rect()
		
		self.largo = 1
		self.posicion = [POS_INICIAL]
		self.direccion = DERECHA
		self.vel_x = 0
		self.vel_y = 0

	def posicion_inicial(self):
		'''Devuelve la posicion de la cabeza'''
		return tuple(self.posicion[0])

	def es_perdedor(self):
		'''Devuelve True si la cabeza de la serpiente está por fuera de los confines del campo.'''
		posicion_cabeza = self.posicion_inicial()
		return (
        	(posicion_cabeza[0] >= ALTO or posicion_cabeza[0] < 0) or
        	(posicion_cabeza[1] >= ANCHO or posicion_cabeza[1] < 0) or
        	(self.posicion.count(posicion_cabeza) > 1)
    	)


	def es_ganador(self):
		'''Devuelve True si la longitud de la serpiente alcanza el largo máximo permitido.'''
		return self.largo == LARGO_MAX

	def reset(self):
		self.largo = 1
		self.posicion = [POS_INICIAL]
		self.direccion = DERECHA
		self.vel_x = 0
		self.vel_y = 0

	def dibujo(self, pantalla):
		if self.direccion == IZQUIERDA:
			pantalla.blit(self.imagen_izq, self.posicion_inicial())
		elif self.direccion == DERECHA:
			pantalla.blit(self.imagen_der, self.posicion_inicial())
		elif self.direccion == ARRIBA:
			pantalla.blit(self.imagen_up, self.posicion_inicial())
		elif self.direccion == ABAJO:
			pantalla.blit(self.imagen_down, self.posicion_inicial())

	def update(self):
		# Lógica de actualización aquí (por ejemplo, manejo de eventos de teclado)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.vel_y = -1
			self.vel_x = 0
		if keys[pygame.K_DOWN]:
			self.vel_y = 1
			self.vel_x = 0
		if keys[pygame.K_LEFT]:
			self.vel_x = -1
			self.vel_y = 0
		if keys[pygame.K_RIGHT]:
			self.vel_x = 1
			self.vel_y = 0
    

'''Comienzo del juego.
Inicializacion de pygame, configuracion general y bucle principal.
'''
def main():
	pygame.init()
	screen = pygame.display.set_mode((ANCHO, ALTO))
	pygame.display.set_caption('Juego Snake')
	clock = pygame.time.Clock()
	fondo = pygame.image.load("fondo.png").convert()
	termina = False


	snake = Snake()
	#fruta = Fruta()

	while not termina:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				termina = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					snake.direccion = ARRIBA
				elif event.key == pygame.K_DOWN:
					snake.direccion = ABAJO
				elif event.key == pygame.K_LEFT:
					snake.direccion = IZQUIERDA
				elif event.key == pygame.K_RIGHT:
					snake.direccion = DERECHA

		snake.update()
		screen.blit(fondo, [0, 0])
		snake.dibujo(screen)
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
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
>>>>>>> d0b56c0b36d19b70e3673fb26fd5e7b3ecd3e911
