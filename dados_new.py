""""
RANDOM DADOS 

Proyecto base para recrear los dados anteriores pero usando
la logica de las funciones y poder crear un programa que no
se rompa y divertido estableciendo como meta, replicarlo en java
con clases y mensajes mucho mas experimentatativos
"""

#Metas del proyecto :

"""
*La primera meta es crear las reglas en el primer print pero
buscando en bellecer el codigo mas para labusqueda de la paciencia 
y la determinacion que el juego sea legible desde el inicio.

*Arreglar errores de validacion y usar try, bucles para que el juego no
acabe en la primera partida

*Usar un recordatorio de cuantas veces uno ha ganado y aprender a aumentar
la probabuilidad gradualmente.

*Crear modos de juegos
"""

#Comenzamos importando el random de una funcion para colocar las metricas
import time
global contador 

def random_dados():#El rango del random
    import random
    numero =  random.randint(1,6)
    return numero

#Luego colocamos cuantosdados queremos tirar en el juego esta vez usando un ciclo for i in para mostrar mejor y mas limpio

def validacion_cantidad_dados(cantidad_ingresada : int) : #Cuantosndados dados se quiere jugar
    while(True):
        try :
            cantidad_limpia = int(input(cantidad_ingresada))
        except ValueError :
            print("ERROR = No puedes usar letras, simbolos o algo que no seanlos numeros indicados | Solucion = Debes usaar los numeros positivos y permitidos de usar")
            continue
        if cantidad_limpia <= 0 :
            print("ERROR = No se puede colocar numeros negativos ni el 0 dentro del programa. | Solucion = Debe utilizar numeros positivos e indicados por el juego.")
        elif cantidad_limpia > 2 :
            print("ERROR = No puedes usar numeros mayores al 2 | Solucion = Porfavor elija de 1 a 2 dados para poder jugar.")
        else :
            return cantidad_limpia

def validacion_tiradas_dados(tirada_dados : int) : #Las veces que se reepetira el tirar dados
     while(True):
            try :
                tirada_limpia = int(input(tirada_dados))
            except ValueError :
                print("ERROR = No puedes usar letras, simbolos o algo que no seanlos numeros indicados | Solucion = Debes usaar los numeros positivos y permitidos de usar")
                continue
            if tirada_limpia <= 0 :
                print("ERROR = No se puede colocar numeros negativos ni el 0 dentro del programa. | Solucion = Debe utilizar numeros positivos e indicados por el juego.")

            elif tirada_limpia > 2 :
                print("ERROR = No puedes usar numeros mayores al 2 | Solucion = Porfavor elija de 1 a 2 para poder elegir correctamente las tiradas.")

            else :
                return tirada_limpia

def funcion_repetir_mostrar(tirada_dados : int, cantidad_ingresada : int): #Genera un recorrido de las veces que le piden repetir
    
    contador = 0
    for i in range(tirada_dados):
        print("")
        print(f"\nTirada {i + 1} de {tirada_dados}")
        print("")

        for j in range(cantidad_ingresada) :
            
            acumulable = random_dados()
            contador += acumulable   
            print("")
            print(f"LLeva {j+1} dado/s")
            print("")

            print(f"La cara del dado que salio fue : {acumulable}")
            print(f"Las caras en total en esta tirada es de : {contador}")
    return contador
        

def tipo_puntuacion(dados_ingresado : int , tiradas_ingresadas : int):#Metricas de puntos
    
    if dados_ingresado == 1 and tiradas_ingresadas == 1 :
        print("Los puntos que debe ganar son de 4")
        return "a"
    
    elif dados_ingresado == 2 and tiradas_ingresadas == 2 :
        print("Los puntos que debe ganar son de 17")
        return "A"
    
    elif dados_ingresado == 1 and tiradas_ingresadas == 2 :
        print("Los puntos que debe ganar son de 8")
        return "b"
    
    elif dados_ingresado == 2 and tiradas_ingresadas == 1 :
        print("Los puntos que debe ganar son de 8")
        return "B"

def punto_ganar(formato_puntos : str, punto_adquirido : int): #Para colocar quien gana
    
    if formato_puntos is "a" and  4 <= punto_adquirido <= 5 :
         print("¡Lograste ganar!")
    
    elif formato_puntos is "a" and punto_adquirido == 6 :
          print("¡Excelente fue perfecto!")

    elif formato_puntos is "A" and  17 <= punto_adquirido <= 23 :
       return  print("¡Lograste ganar!")
    
     
    elif formato_puntos is "A" and punto_adquirido == 24 :
       return  print("¡Excelente fue perfecto!")
    
    elif formato_puntos is "b" and punto_adquirido == 12 :
       return  print("¡Excelente fue perfecto!")
    
    elif formato_puntos is "B" and punto_adquirido == 12 :
           return  print("¡Excelente fue perfecto!")
   
    elif formato_puntos is "b"  and  7 <= punto_adquirido <= 11  :
           return  print("¡Lograste ganar!")
        
    elif formato_puntos is "B" and  7 <= punto_adquirido <= 11 :
        return  print("¡Lograste ganar!")
    
    #Seccion de cuando pierdes
    elif    formato_puntos is "a" and punto_adquirido < 4 :
        return print("Perdiste, pero recuerda que puedes volver a intentar")
    
    elif formato_puntos is "A" and punto_adquirido < 17 :
        return  print("Perdiste, pero recuerda que puedes volver a intentar")
    
    elif    formato_puntos is "b" and punto_adquirido < 7 :
        return print("Perdiste, pero recuerda que puedes volver a intentar")
        
    elif formato_puntos is "B" and punto_adquirido < 7 :
        return  print("Perdiste, pero recuerda que puedes volver a intentar")



def reglas_juego():#Explicacion de las reglas del juego
    print("\n---¡BIENVENIDO AL JUEGO DE DADOS!---")
    print("")
    print("Bienvenido a un juego sencillo de al azar que permite jugar con la probabilidad de python, ")
    print("es para testear y mostrar el cambio de la antigua version con intension de echarse unas jugadas.")
    print("")
    print("---FUNCIONAMIENTO DEL JUEGO---")
    print("*Uno puede elegir cuantos dados va a tirar y cuantas veces lo va a tirar")
    print("*Uno puede ganar desde que de el punto que muestra la pantalla y si hay suerte poder tener una tirada perfecta.")
    print("*Poder repetir las veces que quiere que se repita el juego")
    print("*Tener la posibilidad de intercalar entre los dados y las tiradas")
    print("")
    print("Espero que disfruten del mini juego o del codigo ;)")


def validar_num(numero : int):#Valida la s o n para er si quiere repetir el juego
    while(True) :
        try :
            numero_limpio = input(numero).strip()
        except ValueError :
            print("ERROR = No puedes ingresar nada que no sea el numero 1 o 2 | Solucion = Debes solo usar el numero 1 o 1 si deaseas continuar o no.")
            continue
        if len(numero_limpio) > 1 :
            print("ERROR = No puedes colocar mas de un numero dentro del programa| Solucion = Porfavor coloque 1 si desea continuar o 2 si desea que se termine el programa.")
        
        elif len(numero_limpio) == 0 :
            print("ERROR = Solo puedes colocar los numeros 1 o 2 no puedes dejarlo vacio | Solucion = Porfavor coloque 1 si desea continuar o 2 si desea que se termine el programa. ")
        elif numero_limpio== "1" or numero_limpio == "2":
            return int(numero_limpio)
        
        


reglas_juego()

def menu_juego():
    while(True):
        print("\n¡EMPEZEMOS EL JUEGO!")
        contador = 0
        print("")
        print("---CANTIDAD DE DADOS---")
        cantidad_datos = validacion_cantidad_dados("¿Cuantos dados deseas jugar? : ")
        time.sleep(3)
        print("")
        print("---CANTIDAD DETIRADAS---")
        cantidad_tiradas = validacion_tiradas_dados("¿Cuantas tiradas deseas jugar? : ")
        time.sleep(3)
        print("")
        puntuacion_formato = tipo_puntuacion(cantidad_datos,cantidad_tiradas)
        time.sleep(3)
        print("")
        cantidad_final = funcion_repetir_mostrar(cantidad_datos,cantidad_tiradas)
        time.sleep(3)
        print("")
       
        punto_ganar(puntuacion_formato,cantidad_final)
        
        print("\n---¿Deseas seguir jugando?")
        print("")
        print("Coloque 1 si desea volver a jugar y 2 si desea terminar el juego")
        print("")
        numero_adquirido = validar_num("Ingrese el numero aqui : ")
        
        if numero_adquirido == 1:
            print("REINICIANDO EL JUEGO..")
            time.sleep(2)
        elif numero_adquirido == 2:
            print("!Gracias por jugar!")
            break

menu_juego()
        
        
        
        