import random

#CÓDIGO DEL PARQUÉS


Casillas= ["[]"]*68
Individual1= ["[]"]*7
Individual2= ["[]"]*7
Individual3= ["[]"]*7
Individual4= ["[]"]*7
fichas = {
    "Jugador ROJO":{
        "Ficha 1R":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 2R":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 3R":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 4R":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0}
    },
    "Jugador AZUL" :{
        "Ficha 1AZ":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 2AZ":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 3AZ":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0},
        "Ficha 4AZ":{"posicion":None, "estado": "presa en el extranjero", "Distancia": 0,"ContadorPares": 0}
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
            if datos["Distancia"] > 63 or datos["posicion"] is None:
                continue  
            poss = datos["posicion"]
            if 0 <= poss <= len(Casillas):
             Casillas[poss]= f"[{ficha_nombre}]"

    print(" ".join(Casillas)) 
    input("TABLERO ACTUALIZADO. Presione ENTER para continuar")


def moverfichas(ficha_nombre, Cant):
    ficha = extraerFichas(ficha_nombre)
    ficha["posicion"]= (ficha["posicion"] + Cant) % len(Casillas) 
    ficha["Distancia"] =  (ficha["Distancia"] + Cant)
    actuTab()

def DadosGen(playerA, sumaAmbos, par):

    fichass = fichas[playerA]
    fichas_activas = [pieza for pieza, datos in fichass.items() if datos["estado"] == "activa"]

    if not fichas_activas:
        print("No hay fichas activas para mover.")
        actuTab()
        return

    print(f"Fichas activas disponibles: {', '.join(fichas_activas)}")
    ficha_elegida = input("Escriba el nombre exacto de la ficha que desea mover: ")
    if ficha_elegida not in fichas_activas:
        print("Error en digitación. Pierde tuno.")
        actuTab()
        return
    moverfichas(ficha_elegida, sumaAmbos)
    datos = fichass[ficha_elegida]
    if par:
        datos["ContadorPares"] += 1
        print(f"{ficha_elegida} lleva {datos['ContadorPares']} pares consecutivos. OJITOO")
        if datos["ContadorPares"] == 3:
            datos["estado"] = "presa en el extranjero"
            datos["posicion"] = None
            datos["Distancia"] = 0
            datos["ContadorPares"] = 0
            print(f"{ficha_elegida} ha ido a la cárcel por sacar tres pares consecutivosss")
            actuTab()
            return
    else:
        datos["ContadorPares"] = 0


def SacarFicha(playerA, dado,par):
    fichass = fichas[playerA]
    if par == True:
        if dado == 5:
            for pieza, datos in fichass.items():
                if datos["estado"] != "activa":
                    datos["estado"] = "activa"
                    datos["posicion"] = 5  if playerA == "Jugador ROJO" else 21
                    datos["ContadorPares"] += 1
                    if datos["ContadorPares"] == 3:
                        datos["estado"] = "presa en el extranjero"
                        datos["posicion"] = None
                        datos["Distancia"] = 0
                        datos["ContadorPares"] = 0
                        print(f"{pieza} ha ido a la cárcel por sacar tres pares seguidos")
                        actuTab()
                        return
                    print(f"{pieza} ha entrado al juego")
                    actuTab()
                    return
            print("Todas las fichas ya están activas!!! :)")
            for pieza, datos in fichass.items():
                datos["ContadorPares"] += 1
                if datos["ContadorPares"] == 3:
                    datos["estado"] = "presa en el extranjero"
                    datos["posicion"] = None
                    datos["Distancia"] = 0
                    datos["ContadorPares"] = 0
                    print(f"{pieza} ha ido a la cárcel por sacar tres pares seguidos")
                    actuTab()
                    return
            DadosGen(playerA)
            actuTab()
            return
        else:
            for pieza, datos in fichass.items():
                datos["ContadorPares"] += 1
                if datos["ContadorPares"] == 3:
                    datos["estado"] = "presa en el extranjero"
                    datos["posicion"] = None
                    datos["Distancia"] = 0
                    datos["ContadorPares"] = 0
                    print(f"{pieza} ha ido a la cárcel por sacar tres pares seguidos")
                    actuTab()
                    return
            DadosGen(playerA)
    else:
        for pieza, datos in fichass.items():
            datos["ContadorPares"] =0
        if dado == 5:
            for pieza, datos in fichass.items():
                if datos["estado"] != "activa":
                    datos["estado"] = "activa"
                    datos["posicion"] = 5  if playerA == "Jugador ROJO" else 21
                    datos["Distancia"] = 5 if playerA == "Jugador ROJO" else 21
                    print(f"{pieza} ha entrado al juego")
                    actuTab()
                    return
            print("Todas las fichas ya están activas!!! :)")
            actuTab()
            DadosGen(playerA)
            return
        else:
            DadosGen(playerA)
    

def TURNOS (playerA):
    repetir= True
    while repetir:
        Dado1=  random.randint(1,6)
        Dado2= random.randint(1,6)
        par= Dado1==Dado2
        print(f"{playerA} sacó {Dado1} y {Dado2}")
        input("ENTER para continuar")
        if Dado1 == 5 or Dado2 == 5:
         SacarFicha(playerA,5,par)
        else:
            sumaAmbos = Dado1 + Dado2
            print(f"{playerA} sacó en  Dado 1: {Dado1} y Dado 2: {Dado2}, eso suma un total de...{sumaAmbos}")
            DadosGen(playerA,sumaAmbos, par)
        repetir = par

def INICIO ():
    
    while True:
        TURNOS("Jugador ROJO")
        if fichas ["Jugador ROJO"]["Ficha 1R"]["Distancia"]>63 and fichas ["Jugador ROJO"]["Ficha 2R"]["Distancia"]>63 and fichas["Jugador ROJO"]["Ficha 3R"]["Distancia"]>63 and fichas["Jugador ROJO"]["Ficha 4R"]["Distancia"]>63:
            print("Jugador ROJO ha ganado")


            exit()

        TURNOS("Jugador AZUL")

        if fichas["Jugador AZUL"]["Ficha 1AZ"]["Distancia"]>68 and fichas["Jugador AZUL"]["Ficha 2AZ"]["Distancia"]>68 and fichas["Jugador AZUL"]["Ficha 3AZ"]["Distancia"]>68 and fichas["Jugador AZUL"]["Ficha 4AZ"]["Distancia"]>68:
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
        num_jugadores = int(input("¿Cuántas personas van a jugar? (1/2/3/4) (SE RECOMIENDA 2P por estabilidad): "))
        if num_jugadores in [1, 2, 3, 4]:
            if num_jugadores==2:
                print("ADELANTE")
                input("Presione ENTER para continuar")
                INICIO()
            else:
                print("ADELANTE")
                input("Presione ENTER para continuar")
                INICIO()

    elif RULE.upper() == "B":
        mensaje = """
        - Cada equipo tiene hasta 4 fichas.
        - El tablero tiene 68 casillas externas compartidas + 8 casillas de llegada por equipo.
        - Se usan dos dados estándar (1 al 6).
        - Se lanzan 2 dados por turno.
        - Las fichas solo pueden salir si hay un 5 en el dado.
        - Máximo 2 fichas por casilla
        - Comer una ficha adiciona al jugador 20 movimientos
        - Cornonar una ficha otorga 10 movimientos al jugador
        - Tres pares seguidos conllevan a enviar una ficha a la cárcel
        """
        print(mensaje)

        input("Presione ENTER para continuar")
        num_jugadores = int(input("¿Cuántas personas van a jugar? (1/2/3/4) (SE RECOMIENDA 2P por estabilidad): "))
        if num_jugadores in [1, 2, 3, 4]:
            if num_jugadores==2:
                print("ADELANTE")
                input("Presione ENTER para continuar")
                INICIO()
            else:
                print("ADELANTE")
                input("Presione ENTER para continuar")
                INICIO()
    else:
        print("No entendí su respuesta, intentelo de nuevo")
        exit()
WELCOME()

        
          

    












