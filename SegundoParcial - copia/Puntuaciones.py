import pygame
from Constantes import *
from Funciones import *
import json
pygame.init()

fondo_menu = pygame.image.load("fondoconfiguraciones.jpg")
fondo_menu = pygame.transform.scale(fondo_menu,VENTANA)

boton_volver = crear_boton("volver.png",TAMAÑO_BOTON_VOLVER)


def mostar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "puntuaciones"

    try:
        with open("partidas.json", "r") as archivo:
            partidas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        partidas = []

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"

    pantalla.blit(fondo_menu, (0, 0))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    for i, partida in enumerate(partidas, 1):
        texto_ranking = f"{i}. {partida['nombre']} - {partida['puntaje']} pts ({partida['fecha']})"
        mostrar_texto(pantalla, texto_ranking, (10, 150 + (i * 60)), FUENTE_30, COLOR_ROJO)
    return retorno