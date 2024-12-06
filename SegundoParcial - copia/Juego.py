import pygame 
import random
from Funciones import *
# from Preguntas import *
pygame.init()
fondo = pygame.image.load("fondo.jpg")

fondo = pygame.transform.scale(fondo,VENTANA) #Carga imagen y la escala a la ventana

lista_respuestas = []

lista_comodines = []

lista_preguntas = leer_csv("Archivo_CSV_Juego.csv")

imagenes_comodines = [
    "bombita.jpg",
    "pordos.jpg",
    "flecha.jpg",
    "segundachance.jpg"
]

imagen_pregunta_respuesta = "preguntasyrespuestas.jpg"

cuadro_datos = crear_boton("preguntasyrespuestas.jpg",TAMAÑO_DATOS)

cuadro_pregunta = crear_boton("preguntasyrespuestas.jpg",TAMAÑO_PREGUNTA)

for i in range(4):
    cuadro_respuesta = crear_boton("preguntasyrespuestas.jpg",TAMAÑO_RESPUESTA)
    lista_respuestas.append(cuadro_respuesta)

    cuadro_comodines = crear_boton((imagenes_comodines[i]),TAMAÑO_COMODIN)
    lista_comodines.append(cuadro_comodines)

indice = 0
contador_incorrecto = 0
contador_doble_chance_incorrecto = 0
bandera_respuesta = False
comodin_por_dos_activado = False
comodin_doble_chance_activado = False
random.shuffle(lista_preguntas)
nombre = ""

def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event],datos_juego:dict):
    retorno = "juego"
    global indice
    global bandera_respuesta
    global contador_incorrecto
    global comodin_por_dos_activado
    global comodin_doble_chance_activado
    global contador_doble_chance_incorrecto
    global RESPUESTAS_CORRECTAS_CONSECUTIVAS
    global nombre

    if bandera_respuesta:
            pygame.time.delay(250)
            cuadro_pregunta["superficie"] = pygame.image.load(imagen_pregunta_respuesta)
            cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"], TAMAÑO_PREGUNTA)

            for i in range(len(lista_respuestas)):
                lista_respuestas[i]["superficie"] = pygame.image.load(imagen_pregunta_respuesta)
                lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"],TAMAÑO_RESPUESTA)
            bandera_respuesta = False

    pregunta_actual = lista_preguntas[indice]

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            if lista_comodines[0]["rectangulo"].collidepoint(evento.pos) and datos_juego["bandera_bomba"] == True: 
            #Me fijo si le dio al rectangulo de bomba y si la opcion esta disponible     
                for i in range(len(lista_respuestas)):
                    if  i != pregunta_actual["respuesta_correcta"] - 1 and contador_incorrecto < 2: #Comparo la pregunta actual con el indice de las respuestas
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        contador_incorrecto += 1 #Lleno de rojo hasta 2 respuestas incorrectas
                datos_juego["bandera_bomba"] = False
            
            elif lista_comodines[1]["rectangulo"].collidepoint(evento.pos) and datos_juego["bandera_por_dos"] == True:
                comodin_por_dos_activado = True
                datos_juego["bandera_por_dos"] = False  # Solo puede usarse una vez
            
            elif lista_comodines[2]["rectangulo"].collidepoint(evento.pos) and datos_juego["bandera_flecha"] == True:
                datos_juego["bandera_flecha"] = False
                indice += 1 #Actualizo la pregunta actual
                indice = actualizar_indice(lista_preguntas, indice)
                bandera_respuesta = True
                comodin_por_dos_activado = False
            
            elif lista_comodines[3]["rectangulo"].collidepoint(evento.pos) and datos_juego["bandera_doble_chance"] == True:
                datos_juego["bandera_doble_chance"] = False
                comodin_doble_chance_activado = True

            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        comodin_doble_chance_activado = False
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        if comodin_por_dos_activado:
                            datos_juego["puntuacion"] += PUNTUACION_ACIERTO * 2
                            comodin_por_dos_activado = False
                            RESPUESTAS_CORRECTAS_CONSECUTIVAS += 1
                        else:
                            datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                            RESPUESTAS_CORRECTAS_CONSECUTIVAS += 1
                        if RESPUESTAS_CORRECTAS_CONSECUTIVAS == 5:
                            datos_juego["cantidad_vidas"] += 1
                            RESPUESTAS_CORRECTAS_CONSECUTIVAS = 0 
                      
                    else:
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        contador_doble_chance_incorrecto += 1

                        if (datos_juego["puntuacion"] > 0 and comodin_doble_chance_activado == False) or (datos_juego["puntuacion"] > 0 and contador_doble_chance_incorrecto > 1):
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR

                        if comodin_doble_chance_activado == False or contador_doble_chance_incorrecto > 1:    
                            datos_juego["cantidad_vidas"] -= 1

                    if datos_juego["cantidad_vidas"] == 0:
                        retorno = "terminado" 
                        datos_juego["bandera_bomba"] = True
                        datos_juego["bandera_por_dos"] = True
                        datos_juego["bandera_flecha"] = True
                        datos_juego["bandera_doble_chance"] = True
                        comodin_por_dos_activado = False
                        comodin_doble_chance_activado = False
                        indice = 0
                        contador_incorrecto = 0
                        contador_doble_chance_incorrecto = 0

                    if comodin_doble_chance_activado == False or contador_doble_chance_incorrecto > 1:
                        indice += 1
                        indice = actualizar_indice(lista_preguntas, indice)
                        bandera_respuesta = True
                        comodin_doble_chance_activado = False

    pantalla.blit(fondo,(0,0))
    
     # Actualizar el contenido del cuadro de datos
    cuadro_datos["superficie"] = pygame.image.load("preguntasyrespuestas.jpg")  # Cargar la imagen
    cuadro_datos["superficie"] = pygame.transform.scale(cuadro_datos["superficie"],(TAMAÑO_DATOS))

    mostrar_texto(cuadro_datos["superficie"], f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), FUENTE_22, COLOR_NEGRO)
    mostrar_texto(cuadro_datos["superficie"], f"VIDAS: {datos_juego['cantidad_vidas']}", (10, 35), FUENTE_22, COLOR_NEGRO)
    mostrar_texto(cuadro_pregunta["superficie"],f'{pregunta_actual["pregunta"]}',(20,20),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"],f'{pregunta_actual["respuesta_1"]}',(20,20),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[1]["superficie"],f'{pregunta_actual["respuesta_2"]}',(20,20),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[2]["superficie"],f'{pregunta_actual["respuesta_3"]}',(20,20),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[3]["superficie"],f'{pregunta_actual["respuesta_4"]}',(20,20),FUENTE_22,COLOR_NEGRO)

    # Dibujar elementos en pantalla
    cuadro_datos["rectangulo"] = pantalla.blit(cuadro_datos["superficie"],(540,0))

    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(150,100))

    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(150,275))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(150,400))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(150,525))#r3
    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(150,650))#r4
    
    lista_comodines[0]["rectangulo"] = pantalla.blit(lista_comodines[0]["superficie"],(475,275))
    lista_comodines[1]["rectangulo"] = pantalla.blit(lista_comodines[1]["superficie"],(475,400))
    lista_comodines[2]["rectangulo"] = pantalla.blit(lista_comodines[2]["superficie"],(475,525))
    lista_comodines[3]["rectangulo"] = pantalla.blit(lista_comodines[3]["superficie"],(475,650))

  
    pygame.draw.rect(pantalla,COLOR_BLANCO,cuadro_pregunta["rectangulo"],2) # Rectangulo pregunta

    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2) # Rectangulo Respuestas
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[3]["rectangulo"],2)

    pygame.draw.rect(pantalla,COLOR_NEGRO,lista_comodines[0]["rectangulo"],2) # Rectangulo Comodines
    pygame.draw.rect(pantalla,COLOR_NEGRO,lista_comodines[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_NEGRO,lista_comodines[2]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_NEGRO,lista_comodines[3]["rectangulo"],2)
    return retorno