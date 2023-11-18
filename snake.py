'''
Juego de Snake.
Participantes: Maria Sol Alcaraz
			  Franco Medina
			  Damian Palomba
'''

import pygame, sys, random

#Pantalla
#Cuadrados de 20x20, 25 de alto, 40 de ancho
ANCHO = 800 
ALTO = 500
CUADROS = 20
#Dimensiones de la ventana (tupla)
SCREEN_ANCHO = 800
SCREEN_ALTO = 500
#FPS
FPS = 30
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
LARGO_MAX = 10
FPS = 60

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
		self.posicion = [(ANCHO // 2, ALTO // 2)]
		self.direccion = DERECHA
		self.velocidad = 2

	def posicion_inicial(self):
		'''Devuelve la posicion de la cabeza'''
		return self.posicion[0]

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
		self.velocidad = 1

	def dibujo(self, pantalla):
		cabeza = self.posicion_inicial()
		if self.direccion == IZQUIERDA:
			pantalla.blit(self.imagen_izq, cabeza)
		elif self.direccion == DERECHA:
			pantalla.blit(self.imagen_der, cabeza)
		elif self.direccion == ARRIBA:
			pantalla.blit(self.imagen_up, cabeza)
		elif self.direccion == ABAJO:
			pantalla.blit(self.imagen_down, cabeza)

		for segmento in self.posicion[1:]:
			pygame.draw.rect(pantalla, COLOR_CUERPO, (segmento[0], segmento[1], CUADROS, CUADROS))

	def update(self):
		#Actualiza la posicion en funcion de la direccion
		x, y = self.posicion[0]
		new_x = x + self.direccion[0] * self.velocidad
		new_y = y + self.direccion[1] * self.velocidad
		self.posicion.insert(0, (new_x, new_y))

	def cambiar_direccion(self, nueva_direccion):
		#Cambia la direccion del snake
		if (self.direccion[0] + nueva_direccion[0]!= 0 or self.direccion[1] + nueva_direccion[1] != 0):
			self.direccion = nueva_direccion

	def comio_fruta(self, fruta):
		cabeza_x, cabeza_y = self.posicion_inicial()
		fruta_x, fruta_y = fruta.posicion
		cabeza_rect = pygame.Rect(cabeza_x, cabeza_y, CUADROS, CUADROS)
		fruta_rect = pygame.Rect(fruta_x, fruta_y, CUADROS, CUADROS)
		return cabeza_rect.colliderect(fruta_rect)

#Preferencias de la fruta
class Fruta(pygame.sprite.Sprite):
	def __init__(self,):
		self.imagen_fruta = pygame.image.load("manzana.png").convert()
		self.imagen_fruta.set_colorkey(BLANCO)
		self.rect_fruta = self.imagen_fruta.get_rect()
		self.posicion = (0, 0)
		self.random_posicion()

	def random_posicion(self):
		self.posicion = (random.randint(0, ALTO - 1), random.randint(0, ANCHO - 1))

	def actualizar_fruta(self, snake):
		if snake.posicion_inicial() == self.posicion:
			self.random_posicion()

	def dibujo_fruta(self, pantalla):
		pantalla.blit(self.imagen_fruta, self.posicion)

'''Comienzo del juego.
Inicializacion de pygame, configuracion general y bucle principal.
'''
def main():
	pygame.init()
	screen = pygame.display.set_mode((ANCHO, ALTO))
	pygame.display.set_caption('Juego Snake')
	clock = pygame.time.Clock()
	fondo = pygame.image.load("fondo.png").convert()
	iniciado = False

	snake = Snake()
	fruta = Fruta()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if not iniciado:
					iniciado = True
				if event.key == pygame.K_UP:
					snake.cambiar_direccion(ARRIBA)
				elif event.key == pygame.K_DOWN:
					snake.cambiar_direccion(ABAJO)
				elif event.key == pygame.K_LEFT:
					snake.cambiar_direccion(IZQUIERDA)
				elif event.key == pygame.K_RIGHT:
					snake.cambiar_direccion(DERECHA)

		if iniciado:
			snake.update()
			fruta.actualizar_fruta(snake)
			if snake.comio_fruta(fruta):
				snake.largo += 1
				fruta.random_posicion()

		if snake.es_perdedor() or snake.es_ganador():
			snake.reset()
			fruta.random_posicion()

		screen.blit(fondo, [0, 0])

		fruta.dibujo_fruta(screen)
		snake.dibujo(screen)

		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()

if __name__ == "__main__":
    main()