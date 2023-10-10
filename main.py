import random
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def elegirPalabra():
    """
    Esta función selecciona aleatoriamente
    una palabra de las que tiene disponibles
    """
    listarPalabra = ["CASA"]
    return listarPalabra[random.randint(0,len(listarPalabra))-1] # el indice de "listarPalabra"
                                                                 # es igual al numero generado aleatoreamente
                                                                 # por el "random.randint" entre 0 y el numero de elementos "listarPalabra" -1 para no pasarse del indice.

def dibujarIntento(intento):
    """
    dibuja en pantalla el numero de intentos permitidos.
    no mas de 6
    """
    if intento == 0:
       return print("""
    +---------+
    |         
    |        
    |         
""")
    elif intento == 1:
       return print("""
    +---------+
    |         O
    |        
    |         
""")
    elif intento == 2:
       return print("""
    +---------+
    |         O
    |         |
    |         
""")
    elif intento == 3:
       return print("""
    +---------+
    |         O
    |        /|
    |         
""")
    elif intento == 4:
       return print("""
    +---------+
    |         O
    |        /|\\
    |        
""")
    elif intento == 5:
       return print("""
    +---------+
    |         O
    |        /|\\
    |        / 
""")
    elif intento == 6:
       return print("""
    +---------+
    |         O
    |        /|\\
    |        / \\
""")

def Verificar(letra,var):
    """
    revisa si la variable "letra" coinside con algunos de los elementos 
    de "fn" de ser asi sobreescribe "correcto" de los contrario
    sobreescribe incorrecto
    """
    if letra in var:

        if letra in correcto:
            try:
                correcto[var.index(letra,-1)] = letra # buscar "letra" en "var" desde el ultimo elemento de "var" 
                                                      # y sobreescribe "correcto" con el valor "letra" con el mismo indice en el que se encontro "letra".
                                                      # NOTA: de ser posible buscar la forma de buscar "letra" desde la primera aparicion de esa misma "letra".

            except ValueError:
                incorrecto.append(letra)
               
        
        correcto[var.index(letra,0)] = letra # buscar "letra" en "var" desde el primer elemento de "var" 
                                             # y sobreescribe "correcto" con el valor "letra" con el mismo indice en el que se encontro "letra".

    else:
       incorrecto.append(letra)

palabra = elegirPalabra()

correcto = [0]*len(palabra) # genera una lista de elementos iguales con la misma cantidad de elementos que la variable
                            # "palabra".
                            # posteriormente un elemento es reemplazado si el caracter es correcto.

incorrecto = [] # una lista con los caracteres incorrectos.

intentos = 0 # numero de intentos realizados no se permite mas de 6

palabraFinal = ""

os.system("cls")
dibujarIntento(intentos)


while True:

    print("incorrecto: ",incorrecto)
    print("correcto: ",correcto)
    jugador = input(">")

    Verificar(jugador,palabra)
    intentos += 1
    clear()

    dibujarIntento(intentos)


    palabraFinal = "".join(map(str,correcto)) # la función "map" aplica la función "str" a todos los elementos de la
                                              # lista "correcto" y devuelve un objeto "map" iterable. 
    if not jugador:
       break
    elif intentos == 6:
       clear()
       print("F I N  D E L  J U E G O")
       dibujarIntento(intentos)
       print("palabra: ",palabra)
       print("incorrecto: ",incorrecto)
       print("correcto: ",correcto)
       Verificar(jugador,palabra)
       break
    elif palabraFinal == palabra:
       clear()
       print("F E L I Z I D A D E S  G A N A S T E")
       dibujarIntento(intentos)
       print("incorrecto: ",incorrecto)
       print("correcto: ",correcto)
       Verificar(jugador,palabra)
       break