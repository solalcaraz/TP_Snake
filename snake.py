import pygame
from random import randint
from time import sleep

#Pantalla
ANCHO = 800
ALTURA = 600 
#CADA BLOQUE ES DE 20x20

#FPS
FPS = 30
#Paleta de colores
NEGRO = (0, 0, 0, 100)
BLANCO = (255, 255, 255)
COLOR_CUERPO = (0, 255, 255)
COLOR_FRUTA = (255, 200, 0)

LARGO_MAX = 10


def main():
    pygame.init()
    pygame.display.set_caption('Juego Snake')
    ventana = pygame.display.set_mode((ANCHO, ALTURA))
    fps = pygame.time.Clock()
    
    menu = pygame.image.load("menu.png").convert()    
    fondo = pygame.image.load("fondo.png").convert()
    
    cabeza_imagen = pygame.image.load("cabeza.png").convert()
    cabeza_imagen.set_colorkey(NEGRO)
    cuerpo_imag = pygame.image.load("cuerpo.png").convert()
    cuerpo_imag.set_colorkey(NEGRO)

    fruta_imag = pygame.image.load("manzana.png").convert()
    fruta_imag.set_colorkey(NEGRO)

    roca_imag = pygame.image.load("roca.png").convert()
    roca_imag.set_colorkey(BLANCO)
    
    while(True):
        snake = [[400,300],[380,300],[360,300],[340,300]]
        pos_snake = [340,300] #Posicion de la cabeza del snake en todo momento.
        roca = [[400,400],[420,420],[420,400],[400,420],[160,160],[180,180],[200,200]]

        for i in range(4):
            nueva_roca = posicion_aleatoria(ANCHO, ALTURA, snake, roca)
            roca.append(nueva_roca.copy())

        fruta = posicion_aleatoria(ANCHO,ALTURA,snake,roca);
        puntaje = 0
        iniciado = False
        direccion = 'LEFT'
        dir_siguiente = direccion
        VELOCIDAD = 10

        menu_inicial(ventana, menu)

        while(True):
            direccion, dir_siguiente = mover_snake(direccion, dir_siguiente, cabeza_imagen, pos_snake)
            snake.append(pos_snake.copy())
            if pos_snake == fruta:
                fruta = posicion_aleatoria(ANCHO,ALTURA,snake,roca);
                puntaje += 1
                VELOCIDAD *= 1.05
                print(VELOCIDAD)
            else:
                snake = snake[1:]

            ventana.blit(fondo, [0, 0])

            imprimir_campo(snake, roca, fruta, ventana, direccion, cabeza_imagen, cuerpo_imag, fruta_imag, roca_imag, pos_snake)
            if es_perdedor(snake, roca, pos_snake):
                game_over(ventana, puntaje)
                break
            print_puntaje(ventana, puntaje)
            pygame.display.update()
            if not iniciado:
                pygame.event.wait()
                iniciado = True
            fps.tick(VELOCIDAD)

def mover_snake(direccion, dir_siguiente, cabeza_imagen, pos_snake):
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
    if direccion == 'DOWN':
        pos_snake[1] += 20
    if direccion == 'LEFT':
        pos_snake[0] -= 20
    if direccion == 'RIGHT':
        pos_snake[0] += 20
        
    return [direccion, dir_siguiente]
    
def posicion_aleatoria(ancho, altura, snake, roca):
    '''Recibe las dimensiones de un campo de ALTURAxANCHO, y la lista de posiciones del snake y los obstaculos.
       Devuelve una posición [x,y] vacía aleatoria dentro de esas dimensiones.
       En este caso, "vacía" significa que la posición no se encuentra ocupada por el snake.'''
    [x, y] = [randint(1, (ANCHO-20)//20)*20, randint(1, (ALTURA-20)//20)*20]
    while [x, y] in snake or [x, y] in roca:
        [x, y] = [randint(1, (ANCHO-20)//20)*20, randint(1, (ALTURA-20)//20)*20]
    return [x, y]
    
def imprimir_campo(snake, roca, fruta, ventana, direccion, cabeza_imagen, cuerpo_imag, fruta_imag, roca_imag, pos_snake):
    for posicion in snake[:-1]:
        ventana.blit(cuerpo_imag, (posicion[0], posicion[1]))
    if direccion == 'UP':
        cabeza_rot = pygame.transform.rotate(cabeza_imagen,90)
    if direccion == 'DOWN':
        cabeza_rot = pygame.transform.rotate(cabeza_imagen,270)
    if direccion == 'LEFT':
        cabeza_rot = pygame.transform.rotate(cabeza_imagen,180)
    if direccion == 'RIGHT':
        cabeza_rot = cabeza_imagen
        
        
    ventana.blit(cabeza_rot, pos_snake)
    ventana.blit(fruta_imag, (fruta[0], fruta[1]))
    
    for roca_pos in roca:
        ventana.blit(roca_imag, (roca_pos[0], roca_pos[1]))
    
def es_perdedor(snake, roca, pos_snake):
    #Busco si la proxima posicion esta dentro del snake, si lo está la cabeza tocó el cuerpo.
    for pos_cuerpo in snake[:-1]:
        if pos_snake[0] == pos_cuerpo[0] and pos_snake[1] == pos_cuerpo[1]:
            return True
    #Chequeo que la proxima posicion no se salga del campo.
    if (pos_snake[0] < 0 or pos_snake[0] > ANCHO - 20 or pos_snake[1] < 0 or pos_snake[1] > ALTURA - 20):
        return True

    for roca_pos in roca:
        if pos_snake[0] == roca_pos[0] and pos_snake[1] == roca_pos[1]:
            return True

    return False

def menu_inicial(ventana, menu):
    ventana.blit(menu, [0, 0])
    pygame.display.update()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_a:
                    pygame.event.clear()
                    return
    pygame.time.delay(50)

def game_over(ventana, puntaje):
    print_gameover(ventana, puntaje)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    pygame.event.clear()
                    return
    
def print_gameover(ventana, puntaje):
    rect_negro = pygame.Rect(0,0,800,600)
    sup_negra = pygame.Surface(rect_negro.size,pygame.SRCALPHA)
    pygame.draw.rect(sup_negra, NEGRO, sup_negra.get_rect())
    ventana.blit(sup_negra,rect_negro)
    fuente1 = pygame.font.SysFont('Times new roman',55)
    fuente2 = pygame.font.SysFont('Times new roman',30)
    over_impresion = fuente1.render('Has Muerto. Puntaje: ' + str(puntaje), True, NEGRO)
    over_rect = over_impresion.get_rect()
    over_rect.midtop = (ANCHO/2, ALTURA/2-50)
    menu1_impresion = fuente2.render('Presione [q] para salir.', True, NEGRO)
    menu2_impresion = fuente2.render('Presione [r] para volver a jugar.', True, NEGRO)
    menu1_rect = menu1_impresion.get_rect()
    menu1_rect.midtop = (ANCHO/2-100, ALTURA/2+10)
    menu2_rect = menu1_impresion.get_rect()
    menu2_rect.midtop = (ANCHO/2-100, ALTURA/2+50)
    
    ventana.blit(over_impresion, over_rect)
    ventana.blit(menu1_impresion, menu1_rect)
    ventana.blit(menu2_impresion, menu2_rect)
    pygame.display.flip()

def print_puntaje(ventana, puntaje):
    fuente = pygame.font.SysFont('Arial',30)
    area_impresion = fuente.render('Puntaje: ' + str(puntaje), True, NEGRO)
    area_rect = area_impresion.get_rect()
    ventana.blit(area_impresion, area_rect)
    pygame.display.flip()
    
    
    
main()