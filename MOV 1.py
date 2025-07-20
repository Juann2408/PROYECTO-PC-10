import random

#CÓDIGO DEL PARQUÉS


Casillas= ["[]"]*68
Individual1= ["[]"]*7
Individual2= ["[]"]*7
fichas = {
    "Jugador ROJO":{
        "Ficha 1R":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 2R":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 3R":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 4R":{"posicion":0, "estado": "presa en el extranjero"}
    },
    "Jugador AZUL" :{
        "Ficha 1AZ":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 2AZ":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 3AZ":{"posicion":0, "estado": "presa en el extranjero"},
        "Ficha 4AZ":{"posicion":0, "estado": "presa en el extranjero"} 
    }
}
def extraerFichas (ficha_nombre):
    for playerA, ficha_individual in fichas.items():
            for ficha, datos in ficha_individual.items():
                if ficha == ficha_nombre:   
                    return datos
                
                
    else: 
        return None


def actuTab():
    global Casillas
    Casillas= ["[]"]*68
    for fichass in fichas.values():
        for ficha_nombre, datos in fichass.items():
            poss = datos["posicion"]
            if 0 <= poss <= len(Casillas):
             Casillas[poss]= f"[{ficha_nombre}]"

    print(" ".join(Casillas)) 
    input("TABLERO ACTUALIZADO. Presione ENTER para continuar")


def moverfichas(ficha_nombre, Cant):
    ficha = extraerFichas(ficha_nombre)
    ficha["posicion"]= (ficha["posicion"] + Cant) % len(Casillas)
    actuTab()

def DadosGen(playerA, sumaAmbos):

    fichass = fichas[playerA]
    fichas_activas = [pieza for pieza, datos in fichass.items() if datos["estado"] == "activa"]

    if not fichas_activas:
        print("No hay fichas activas para mover.")
        actuTab()
        return

    print(f"Fichas activas disponibles: {', '.join(fichas_activas)}")
    ficha_elegida = input("Escriba el nombre exacto de la ficha que desea mover: ")
    moverfichas(ficha_elegida, sumaAmbos)


def SacarFicha(playerA, dado):
    fichass = fichas[playerA]

    if dado == 5:
        for pieza, datos in fichass.items():
            if datos["estado"] != "activa":
                datos["estado"] = "activa"
                datos["posicion"] = 5 if playerA == "Jugador ROJO" else 1
                print(f"{pieza} ha entrado al juego")
                actuTab()
                return
        print("Todas las fichas ya están activas!!! :)")
        actuTab()
        return
    else: 
        DadosGen(playerA)
def TURNOS (playerA):
    Dado1=  random.randint(1,6)
    Dado2= random.randint(1,6)
    print(f"{playerA} sacó {Dado1} y {Dado2}")
    input("ENTER para continuar")
    if Dado1 == 5 or Dado2 == 5:
     SacarFicha(playerA,5)
    else:
        sumaAmbos = Dado1 + Dado2
        print(f"{playerA} sacó en  Dado 1: {Dado1} y Dado 2: {Dado2}, eso suma un total de...{sumaAmbos}")
        DadosGen(playerA,sumaAmbos)

def INICIO ():
    
    while True:
        TURNOS("Jugador ROJO")
        if fichas ["Jugador ROJO"]["Ficha 1R"]["posicion"]>= 63:
            print("Jugador ROJO ha ganado")


            exit()

        TURNOS("Jugador AZUL")

        if fichas["Jugador AZUL"]["Ficha 1AZ"]["posicion"]>=68:
            print("Jugador AZUL ha ganado")
            exit()
#BIENVENIDOS
def WELCOME ():
    print("Bienvenidos al parqués en python de Juan Manuel Ayala")
    input("Presione ENTER para continuar")
    RULE= input("Si conoce las reglas, presione A, de lo contraio B para conocerlas: ")
    if RULE.upper() == "A":
        print("Perfecto, comencemos a jugar")
        input("Presione ENTER para continuar")
        INICIO()
    elif RULE.upper() == "B":
        mensaje = """
        - Cada equipo tiene hasta 4 fichas.
        - El tablero tiene 68 casillas externas compartidas + 8 casillas de llegada por equipo.
        - Se usan dos dados estándar (1 al 6).
        - Cada equipo tiene hasta 4 fichas.
        - El tablero tiene 68 casillas externas compartidas + 8 casillas de llegada por equipo.
        - Se usan dos dados estándar (1 al 6).
        - Se lanzan 2 dados por turno.
        - Las fichas solo pueden salir si hay un 5 en el dado.
        - Máximo 2 fichas por casilla



        """
        print(mensaje)

        input("Presione ENTER para continuar")
        INICIO()
    else:
        print("No entendí su respuesta, intentelo de nuevo")
        exit()
WELCOME()

        
          

    












