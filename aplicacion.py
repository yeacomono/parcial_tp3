# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14  2024

@author: Damiano Fernandez
@author: Barquero Huaman

"""

import os

dni_file = 'dni.txt'
nombre_file = 'nombre.txt'
apellido_file = 'apellido.txt'

def login():
    counter = 0
    isError = False
    while(True):
        username = input('Ingrese el nombre de usuario: ')
        contraseña = input('Ingrese su contraseña: ')
        if(counter==1):
            isError = True
            break
        login = open("login.txt","rt", encoding='utf8')
        datos_login = login.read()
        print(datos_login)

        clave = open("clave.txt","rt", encoding='utf8')
        datos_clave = clave.read()
        print(datos_clave)
        
        if(username == datos_login and contraseña == datos_clave):
            print("Logeado correctamente")
            break
        else:
            print("Contraseña erronea ingrese nuevamente")
        
        counter = counter+1
    
    if(isError):
        print('Supero el numero de intentos')
        quit()






def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
    
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def listar_personas():
    if os.path.exists(dni_file) and os.path.exists(nombre_file) and os.path.exists(apellido_file):
        print("{:<15} {:<15} {:<15}".format("DNI", "Nombres", "Apellidos"))
        print("-" * 45)
        with open(dni_file, 'r') as dnis, open(nombre_file, 'r') as nombres, open(apellido_file, 'r') as apellidos:
            dni_list = dnis.readlines()
            nombre_list = nombres.readlines()
            apellido_list = apellidos.readlines()
            for i in range(len(dni_list)):
                print("{:<15} {:<15} {:<15}".format(dni_list[i].strip(), nombre_list[i].strip(), apellido_list[i].strip()))
    else:
        print("No hay personas registradas.")    
        
        
def agregar_personas():
    dni = input("Ingrese DNI: ").strip()
    nombre = input("Ingrese Nombres: ").strip()
    apellido = input("Ingrese Apellidos: ").strip()

    with open(dni_file, 'at') as dnis, open(nombre_file, 'at') as nombres, open(apellido_file, 'at') as apellidos:
        dnis.write('\n' + dni)
        nombres.write('\n' + nombre)
        apellidos.write('\n' + apellido)
    print("Persona agregada exitosamente.")

def exit():
    print('Saliendo')
    quit()
    pass










def main():
    
    login()
    
    opciones = {
    '1': ('Listar Personas', listar_personas),
    '2': ('Agregar Personas', agregar_personas),
    '3': ('Salir', exit)
    }
    
    generar_menu(opciones,'4')



main()