#La idea principal es generar un randomdizador practico para completarlo en tirada de dos dados
import random 
random.randint (1,6)
#dados_deseados = 2
#Explicar la regla de puntos y funcionalidades por separadas con un orden estetico.
print("\n---Reglas de juego---")
print("\n<El dado solo reglas y funciones>")
print("Tendras una oportunidad las cuales debes superar el numero 9 para poder ganar")
print("\n<El dado duo reglas y funciones>")
print("Tendras una oportunidad las cuales debes superar el numero 12 para poder ganar")
dados_deseados = int(input("\n¿cuantos dados deseas tirar en este juego?:"))
if dados_deseados == 1 :
 print("Haz elegido usar un dado, muy buena suerte recuerda que tan solo tienes una oportunidad para cada lanzada")
 #Condicion evaluada.
 suma_dados1 = random.randint(1,6)
 #Percibe el primer numero para identificarlo.
 print("Tu primer resultado es: ", suma_dados1)
 #Percibe el segundo numero para identificarlo.
 suma_dados2 = random.randint(1,6)
 print("Tu segundo resultado es de: ", suma_dados2)
 resultado_final = suma_dados1 + suma_dados2
 print(f"El numero final de tu tirada es de : {resultado_final}")
 #Define numero ganador o perdedor con un mensaje final.
 if resultado_final >= 9:
  print("Vaya suerte haz podido ganar ¡FELICITACIONES!")
 else:
  print("¡Que pena! No lograste el numero deseado vuelve a intentarlo")
elif dados_deseados == 2 :
    print("<Ha elegido jugar con dos dados, muy buena suerte solo tienes una oportunidad para cada lanzada")
    #Condicion evaluada.
    suma_dados1 = random.randint(1,6)
    #Percibe el primer numero para identificarlo.
    print("Tu primer resultado es: ", suma_dados1)
    #Percibe el segundo numero para identificarlo.
    suma_dados2 = random.randint(1,6)
    print("Tu segundo resultado es de: ", suma_dados2)
    #Condicion evaluada.
    suma_dados3 = random.randint(1,6)
    #Percibe el primer numero para identificarlo.
    print("Tu tercer resultado es: ", suma_dados3)
    #Percibe el segundo numero para identificarlo.
    suma_dados4 = random.randint(1,6)
    print("Tu cuarto resultado es de: ", suma_dados4)
    resultado_final = suma_dados1 + suma_dados2 + suma_dados3 + suma_dados4
    print(f"El numero final de tu tirada es de : {resultado_final}")
    #Define numero ganador o perdedor con un mensaje final.
    if resultado_final >= 12:
     print("Vaya suerte haz podido ganar ¡FELICITACIONES!")
    else:
     print("¡Que pena! No lograste el numero deseado vuelve a intentarlo")