import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo_menu = pygame.image.load("fondoconfiguraciones.jpg")
fondo_menu = pygame.transform.scale(fondo_menu,VENTANA)

boton_suma = crear_boton("suma.JPG",TAMAÑO_BOTON_VOLUMEN)

boton_resta = crear_boton("resta.JPG",TAMAÑO_BOTON_VOLUMEN)

boton_volver = crear_boton("volver.png",TAMAÑO_BOTON_VOLVER)

boton_mute = crear_boton("mute.jpg",TAMAÑO_BOTON_VOLUMEN)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict):
    retorno = "configuracion"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                print('suma volumen')
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                else:
                    pygame.mixer.Sound("error.mp3").play()

            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                print('baja volumen')
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                else:
                    pygame.mixer.Sound("error.mp3").play()

            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
            
            elif boton_mute["rectangulo"].collidepoint(evento.pos):
                datos_juego["volumen_musica"] = 0

    pantalla.blit(fondo_menu, (0, 0))

    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(120,300))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(520,300))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"],(320,100))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    
    pygame.draw.rect(pantalla,COLOR_AZUL,boton_suma["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,boton_mute["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_ROJO,boton_resta["rectangulo"],2)

    mostrar_texto(pantalla,f'{datos_juego["volumen_musica"]} %',(320,320),FUENTE_50,COLOR_NEGRO)

    return retorno