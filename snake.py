import pygame
from random import randint

#Pantalla
ANCHO = 800
ALTURA = 600 
#CADA BLOQUE ES DE 20x20

#FPS
FPS = 30
#Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_CUERPO = (0, 255, 255)
COLOR_FRUTA = (255, 200, 0)

LARGO_MAX = 10
VELOCIDAD = 15


def main():
    pygame.init()
    pygame.display.set_caption('Juego Snake')
    ventana = pygame.display.set_mode((ANCHO, ALTURA))
    fps = pygame.time.Clock()
    fondo = pygame.image.load("fondo.png").convert()
    
    snake = [[400,300],[380,300],[360,300],[340,300]]
    pos_snake = [340,300] #Posicion de la cabeza del snake en todo momento.
    fruta = posicion_aleatoria(ANCHO,ALTURA,snake);
    
    cabeza_izq = pygame.image.load("cabeza_izquierda.png").convert()
    cabeza_izq.set_colorkey(NEGRO)
    cabeza_der = pygame.image.load("cabeza_derecha.png").convert()
    cabeza_der.set_colorkey(NEGRO)
    cabeza_up = pygame.image.load("cabeza_arriba.png").convert()
    cabeza_up.set_colorkey(NEGRO)
    cabeza_abj = pygame.image.load("cabeza_abajo.png").convert()
    cabeza_abj.set_colorkey(NEGRO)

    cuerpo_imag = pygame.image.load("cuerpo.png").convert()
    cuerpo_imag.set_colorkey(NEGRO)

    fruta_imag = pygame.image.load("manzana.png").convert()
    fruta_imag.set_colorkey(NEGRO)

    direccion = 'RIGHT'
    cabeza_imagen = cabeza_der
    dir_siguiente = direccion

    while(True):
        direccion, dir_siguiente, cabeza_imagen = mover_snake(direccion, dir_siguiente, cabeza_imagen, cabeza_der, cabeza_abj, cabeza_up, cabeza_izq, pos_snake)
        snake.append(pos_snake.copy())
        if pos_snake == fruta:
            fruta = posicion_aleatoria(ANCHO,ALTURA,snake);
        else:
            snake = snake[1:]

        ventana.blit(fondo, [0, 0])

        imprimir_campo(snake, fruta, ventana, cabeza_imagen, cuerpo_imag, fruta_imag, pos_snake)
        if es_perdedor(snake, pos_snake): 
            game_over(ventana)
        pygame.display.update()
        fps.tick(VELOCIDAD)
    return

def mover_snake(direccion, dir_siguiente, cabeza_imagen, cabeza_der, cabeza_abj, cabeza_up, cabeza_izq, pos_snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir_siguiente = 'UP'
            if event.key == pygame.K_DOWN:
                dir_siguiente = 'DOWN'
            if event.key == pygame.K_LEFT:
                dir_siguiente = 'LEFT'
            if event.key == pygame.K_RIGHT:
                dir_siguiente = 'RIGHT'
 
    # Ocupa el caso en el que se presionen dos teclas opuestas a la vez.
    if dir_siguiente == 'UP' and direccion != 'DOWN':
        direccion = 'UP'
    if dir_siguiente == 'DOWN' and direccion != 'UP':
        direccion = 'DOWN'
    if dir_siguiente == 'LEFT' and direccion != 'RIGHT':
        direccion = 'LEFT'
    if dir_siguiente == 'RIGHT' and direccion != 'LEFT':
        direccion = 'RIGHT'
 
    # Mueve el snake un bloque
    if direccion == 'UP':
        pos_snake[1] -= 20
        cabeza_imagen = cabeza_up
    if direccion == 'DOWN':
        pos_snake[1] += 20
        cabeza_imagen = cabeza_abj
    if direccion == 'LEFT':
        pos_snake[0] -= 20
        cabeza_imagen = cabeza_izq
    if direccion == 'RIGHT':
        pos_snake[0] += 20
        cabeza_imagen = cabeza_der
        
    return [direccion, dir_siguiente, cabeza_imagen]
    
def posicion_aleatoria(ancho, altura, snake):
    '''Recibe las dimensiones de un campo de ALTURAxANCHO, y la lista de posiciones del snake.
       Devuelve una posición [x,y] vacía aleatoria dentro de esas dimensiones.
       En este caso, "vacía" significa que la posición no se encuentra ocupada por el snake.'''
    [x, y] = [randint(1, (ANCHO-20)//20)*20, randint(1, (ALTURA-20)//20)*20]
    while [x, y] in snake:
        [x, y] = [randint(1, (ANCHO-20)//20)*20, randint(1, (ALTURA-20)//20)*20]
    return [x, y]
    
def imprimir_campo(snake, fruta, ventana, cabeza_imagen, cuerpo_imag, fruta_imag, pos_snake):
    #ventana.blit(cabeza_imagen, pos_snake)
    for i, posicion in enumerate(snake[1:]):
        #if i == 0: #Cabeza del snake
        #    ventana.blit(cabeza_imagen, pos_snake)
        #else: #Cuerpo general
        ventana.blit(cuerpo_imag, (posicion[0], posicion[1]))
        #pygame.draw.rect(ventana, COLOR_CUERPO, pygame.Rect(posicion[0],posicion[1],20,20))
    ventana.blit(cabeza_imagen, pos_snake)
    ventana.blit(fruta_imag, (fruta[0], fruta[1]))
    
def es_perdedor(snake, pos_snake):
    #Busco si la proxima posicion esta dentro del snake, si lo está la cabeza tocó el cuerpo.
    if any(pos_snake == pos_cuerpo for pos_cuerpo in snake[:-1]):
        return True
    #Chequeo que la proxima posicion no se salga del campo.
    if (pos_snake[0] < 0 or pos_snake[0] > ANCHO - 20 or pos_snake[1] < 0 or pos_snake[1] > ALTURA - 20):
        return True
        
def game_over(ventana):
    pygame.draw.rect(ventana, BLANCO, pygame.Rect(400,300,20,20))
    
main()