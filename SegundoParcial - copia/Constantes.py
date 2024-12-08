import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_AMARILLO = (239,255,0)
COLOR_VERDE_OSCURO = "#0B9827"
ANCHO = 800
ALTO = 800
VENTANA = (ANCHO,ALTO)
FPS = 60


TAMAÑO_PREGUNTA = (425,150)
TAMAÑO_RESPUESTA = (300,100)
TAMAÑO_BOTON = (320,80)
CUADRO_TEXTO = (325,60)
TAMAÑO_BOTON_VOLUMEN = (100,100)
TAMAÑO_BOTON_VOLVER = (90,90)
TAMAÑO_COMODIN = (100,100)
TAMAÑO_DATOS = (250,80)


FUENTE_22 = pygame.font.SysFont("Arial",22)
FUENTE_25 = pygame.font.SysFont("Arial",25)
FUENTE_27 = pygame.font.SysFont("Arial",27)
FUENTE_30 = pygame.font.SysFont("Arial",30)
FUENTE_32 = pygame.font.SysFont("Arial",32)
FUENTE_40 = pygame.font.SysFont("Arial",40)
FUENTE_50 = pygame.font.SysFont("Arial",50)

FUENTE_TIMES_40 = pygame.font.SysFont("timesnewroman",40)
FUENTE_TIMES_25 = pygame.font.SysFont("timesnewroman",25)
FUENTE_TIMES_30 = pygame.font.SysFont("timesnewroman",30)
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

RESPUESTAS_CORRECTAS_CONSECUTIVAS = 0

BOTON_JUGAR = 0
BOTON_AJUSTES = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3