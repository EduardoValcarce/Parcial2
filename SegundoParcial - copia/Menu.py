import pygame
from Constantes import *
from Funciones import *
pygame.init()

fondo_menu = pygame.image.load("fondomenu.jpg")
fondo_menu = pygame.transform.scale(fondo_menu,VENTANA)

lista_botones = []

for i in range(4):
    boton = crear_boton("cuadro.jpg",TAMAÑO_BOTON)
    lista_botones.append(boton)

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "menu"
    pygame.display.set_caption("MENU")
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if lista_botones[BOTON_JUGAR]["rectangulo"].collidepoint(evento.pos):
                retorno = "juego"
            elif lista_botones[BOTON_AJUSTES]["rectangulo"].collidepoint(evento.pos):
                retorno = "configuracion"
            elif lista_botones[BOTON_RANKINGS]["rectangulo"].collidepoint(evento.pos):
                retorno = "puntuaciones"
            elif lista_botones[BOTON_SALIR]["rectangulo"].collidepoint(evento.pos):
                retorno = "salir"

    pantalla.blit(fondo_menu, (0, 0))
    
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_JUGAR] ["superficie"],(220,220))
    lista_botones[BOTON_AJUSTES]["rectangulo"] = pantalla.blit(lista_botones[BOTON_AJUSTES] ["superficie"],(220,320))
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(lista_botones[BOTON_RANKINGS] ["superficie"],(220,420))
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_SALIR] ["superficie"],(220,520))

    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(125,20),FUENTE_40,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_AJUSTES]["superficie"],"AJUSTES",(110,20),FUENTE_40,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]["superficie"],"RANKINGS",(100,20),FUENTE_40,COLOR_NEGRO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(125,20),FUENTE_40,COLOR_NEGRO)

    return retorno













