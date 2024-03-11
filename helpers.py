#contendra funciones auxiliares de uso comun en todo el proyecto

import os 
#este modulo nos permitira identificar que sistema estamos usando
import platform


def limpiar_pantalla():
  
  #este es un operador ternario para idenrificar en que sistema estamos
    #utilizando el modulo os y deacuerdo a lo que identifique   
      #ejecuta un script que borra el contenido de la consola 
  os.system("cls") if platform.system() == "Windows" else os.system("clear")
  
  
#crearenos esta funcion que nos permitira capturar informacion por pantalla
  #nos ayudara en el momento de emplear las funciones con el cliente
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
  print(mensaje) if mensaje else None
  while True:
    texto = input(">")
    if len(texto) >= longitud_min and len(texto) <= longitud_max:
      return texto
  
