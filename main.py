import random
import os

def elegirPalabra():
    """
    Esta función selecciona aleatoriamente
    una palabra de las que tiene disponibles
    """
    listarPalabra = [
        'GATO', 'PERRO', 'CASA', 
        'ROJO', 'AZUL', 'SOL', 
        'LUNA', 'AGUA', 'FLOR', 
        'MESA'
        ]


    # el indice de "listarPalabra" es igual al numero generado aleatoreamente
    # por el "random.randint" entre 0 y el numero de elementos 
    # "listarPalabra" -1 para no pasarse del indice.
    return listarPalabra[random.randint(0,len(listarPalabra))-1]

palabra = elegirPalabra()

#para ganar esta variable tiene que ser identica a "palabra"
palabraFinal = ""

# numero de intentos realizados no se permite mas de 6
intentos = 0 

# genera una lista de elementos iguales con la misma cantidad de elementos 
# que la variable "palabra"
# posteriormente un elemento es reemplazado si el caracter es correcto
correcto = [0]*len(palabra) 

# una lista con los caracteres incorrectos
incorrecto = [] 

def clear():
    """
    limpia la pantalla
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
 
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

clear()

while True:
    # la función "map" aplica la función "str" a todos los elementos de la
    # lista "correcto" y devuelve un objeto "map" iterable.
    palabraFinal = "".join(map(str,correcto))
    
    if intentos == 6:
       clear()
       print("F I N  D E L  J U E G O")
       dibujarIntento(intentos)
       print("palabra: ",palabra)
       print("incorrecto: ",incorrecto)
       print("correcto: ",correcto)
       break
    elif palabraFinal == palabra:
       clear()
       print("F E L I Z I D A D E S  G A N A S T E")
       dibujarIntento(intentos)
       print("palabra: ",palabra)
       print("incorrecto: ",incorrecto)
       print("correcto: ",correcto)
       break

    dibujarIntento(intentos)

    print("incorrecto: ",incorrecto)
    print("correcto: ",correcto)
    jugador = input("> ")
    
    clear()

    if jugador in palabra:
        if jugador in correcto:
            try:
                # buscar "jugador" en "palabra" desde el ultimo elemento encontrado en "palabra" 
                # y sobreescribe "correcto" con el valor "jugador" con el mismo indice en el que se encontro "jugador"
                correcto[palabra.index(jugador,palabra.index(jugador,0)+1)] = jugador

            except ValueError:
                incorrecto.append(jugador)
                intentos += 1
        
        # buscar "jugador" en "palabrar" desde el primer elemento de "palabra" 
        # y sobreescribe "correcto" con el valor "jugador" con el mismo indice en el que se encontro "jugador".
        correcto[palabra.index(jugador,0)] = jugador       
    elif not jugador in palabra:
        incorrecto.append(jugador)
        intentos += 1