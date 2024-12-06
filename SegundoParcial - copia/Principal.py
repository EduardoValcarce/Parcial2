import pygame
from Funciones import *
from Constantes import *
from Menu import *
from Juego import *
from Configuraciones import *
from Puntuaciones import *
from Terminado import *

pygame.init()
pantalla = pygame.display.set_mode(VENTANA) #Crea una ventana con las dimensiones especificadas
corriendo = True
reloj = pygame.time.Clock() #Crea un reloj para controlar la velocidad del juego.
datos_juego = {"puntuacion":0,"cantidad_vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":10,
               "bandera_bomba":True,"bandera_por_dos":True,"bandera_flecha":True,"bandera_doble_chance":True}
ventana_actual = "menu"
while corriendo:
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)

    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
        datos_juego["nombre"] = ""
        datos_juego["puntuacion"] = 0
        datos_juego["cantidad_vidas"] = CANTIDAD_VIDAS
        bandera_juego = False
        pygame.mixer.music.stop()

    elif ventana_actual == "juego":
        if bandera_juego == False:
            porcentaje_musica = datos_juego["volumen_musica"] / 100
            manejar_sonidos_juego(porcentaje_musica)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "configuracion":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "puntuaciones":
        ventana_actual = mostar_rankings(pantalla,cola_eventos)

    elif ventana_actual == "terminado":
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "salir":
        corriendo = False

    pygame.display.flip()
pygame.quit()