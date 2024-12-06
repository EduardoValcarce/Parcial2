from Constantes import *
import random
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def manejar_sonidos_juego(porcentaje_musica:float):
            pygame.mixer.init()
            pygame.mixer.Sound("sonido_silbato.mp3").play()
            pygame.mixer.music.load("musica.juego.mp3")
            pygame.mixer.music.set_volume(porcentaje_musica)
            pygame.mixer.music.play(-1)

def crear_boton(imagen, tamaño)-> dict:
    boton = {}
    boton["superficie"] = pygame.image.load(imagen)  # Cargar la imagen
    boton["superficie"] = pygame.transform.scale(boton["superficie"], tamaño)  # Escalar la imagen
    boton["rectangulo"] = boton["superficie"].get_rect()
    return boton

def actualizar_indice(lista_preguntas, indice):
    if indice >= len(lista_preguntas): 
        random.shuffle(lista_preguntas)  
        indice = 0  
    return indice

def crear_cabecera(diccionario: dict, separador: str) -> str:
    claves = list(diccionario.keys())
    cabecera = separador.join(claves)
    return cabecera.upper()

def crear_dato_csv(diccionario: dict, separador: str) -> str:
    lista_valores = []
    for valor in diccionario.values():
        if isinstance(valor, str) and separador in valor:
            lista_valores.append(f'"{valor}"')
        else:
            lista_valores.append(str(valor))
    
    dato = separador.join(lista_valores)
    return dato

def guardar_csv(nombre_archivo: str, lista: list) -> bool:
    if isinstance(lista, list) and len(lista) > 0 and isinstance(lista[0], dict):
        cabecera = crear_cabecera(lista[0], ",")
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(cabecera + "\n")
            for i in range(len(lista)):
                dato = crear_dato_csv(lista[i], ",")
                archivo.write(dato + "\n")
        return True
    else:
        return False

from Preguntas import *


guardar_csv("Archivo_CSV_Juego.csv", lista_preguntas)


import os  

def crear_diccionario(lista_valores: list) -> dict:
    diccionario = {}
    diccionario["pregunta"] = lista_valores[0]
    diccionario["respuesta_1"] = lista_valores[1]
    diccionario["respuesta_2"] = lista_valores[2]
    diccionario["respuesta_3"] = lista_valores[3]
    diccionario["respuesta_4"] = lista_valores[4]
    diccionario["respuesta_correcta"] = int(lista_valores[5])
    return diccionario

import os  # Asegúrate de importar el módulo os

def leer_csv(nombre_archivo: str):
    if os.path.exists(nombre_archivo):
        lista_alumnos = []
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.readline()
            for linea in archivo:
                linea = linea.replace("\n", "")
                lista_valores = linea.split(",")
                diccionario = crear_diccionario(lista_valores)
                lista_alumnos.append(diccionario)
        return lista_alumnos 
    else:
        return [] 
    
import json
from datetime import datetime

def fin_del_juego(pantalla, puntaje, nombre):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    partida = {"nombre": nombre, "puntaje": puntaje, "fecha": fecha}
    print(f"Nombre guardado: {nombre}")
    
    # Guardo punto en el JSON
    try:
        with open("partidas.json", "r") as datos_jugador:
            partidas = json.load(datos_jugador)
    except (FileNotFoundError, json.JSONDecodeError):
        partidas = []
    
    partidas.append(partida)
    
    with open("partidas.json", "w") as datos_jugador:
        json.dump(partidas, datos_jugador, indent=4)
    
    pygame.display.update()


