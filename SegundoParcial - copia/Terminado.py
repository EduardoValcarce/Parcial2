import pygame
from Constantes import *
from Funciones import *
pygame.init()

fondo_terminado = pygame.image.load("fondoterminado.jpg")
fondo_terminado = pygame.transform.scale(fondo_terminado,VENTANA)

cuadro_texto = crear_boton("cuadroterminado.jpg",((CUADRO_TEXTO)))

nombre = ""

boton = crear_boton("cuadroterminado.jpg",TAMAÑO_BOTON)

cuadro_mensaje = crear_boton("cuadroterminado.jpg",((500,100)))
def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict)-> str:
    global nombre
    retorno = "terminado"
    guardado = False

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton["rectangulo"].collidepoint(evento.pos):
                if len(nombre) > 0 and nombre.strip():
                    if not guardado:
                        datos_juego["nombre"] = nombre
                        fin_del_juego(pantalla, datos_juego["puntuacion"], nombre)
                        guardado = True

                    retorno = "menu"
                    nombre = ""
                    cuadro_texto["superficie"] = pygame.image.load("cuadroterminado.jpg")
                    cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],((CUADRO_TEXTO)))
                    
        elif evento.type == pygame.KEYDOWN:
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS

            if tecla_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1]
                cuadro_texto["superficie"] = pygame.image.load("cuadroterminado.jpg")
                cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],((CUADRO_TEXTO)))

            if tecla_presionada == "space" and len(nombre) != 10:
                    nombre += " "

            if len(tecla_presionada) == 1 and len(nombre) != 10:
                if bloc_mayus != 0:
                    nombre += tecla_presionada.upper()
                else:
                    nombre += tecla_presionada

    pantalla.blit(fondo_terminado, (0, 0))
    boton["rectangulo"] = pantalla.blit(boton["superficie"],(225,500))
    cuadro_texto["rectangulo"] = pantalla.blit(cuadro_texto["superficie"],(225,300))
    cuadro_mensaje["rectangulo"] = pantalla.blit(cuadro_mensaje["superficie"],(150,0))
    mostrar_texto(cuadro_texto["superficie"],nombre,(10,0),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(cuadro_mensaje['superficie'],f'USTED OBTUVO {datos_juego["puntuacion"]} puntos. \nPor favor ingrese su nombre:',(0,0),FUENTE_TIMES_30,COLOR_BLANCO)
    mostrar_texto(boton["superficie"],"DEVUELTA AL MENU(Nombre Guardado)",(0,0),FUENTE_TIMES_25,COLOR_BLANCO)
    return retorno