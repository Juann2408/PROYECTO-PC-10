import random
#BIENVENIDOS

Casillas= ["[]"]*68
Individual1= ["[]"]*7
Individual2= ["[]"]*7
fichas={
"Ficha 1R":{"posicion":0, "estado": "activa"},
"Ficha 2AZ":{"posicion":0, "estado": "activa"},
}  
def TURNOS (ficha_nombre):
    dado=random.randint(1,6)
    print(f"{ficha_nombre} sacó {dado}")
    input("ENTER para continuar")
    SacarFicha()

def INICIO ():
    while True:
        if fichas["Ficha 1R"]["posicion"]==68:
            break
        else:
            TURNOS("Ficha 1R")

        if fichas["Ficha 2AZ"]["posicion"]==68:
            break
        else:
            TURNOS("Ficha 2AZ" )
        
          


def actuTab():
    global Casillas
    Casillas= ["[]"]*68
    for ficha_nombre, datos in fichas.items():
        poss = datos["posicion"]
        if 0 <= poss < 68:
            Casillas[poss]= f"[{ficha_nombre}]"

    print(" ".join(Casillas)) 

def DadosGen():
    DadoUno = random.randint(1,6)
    DadoDos= random.randint(1,6)
    SumaAmbos= DadoUno + DadoDos
    print(f"Sacó en 1: {DadoUno}, y en 2: {DadoDos} eso suma un total de...: {SumaAmbos}")
    input("ENTER para acepatar")
def moverfichas(ficha_nombre, cant):
    ficha = fichas[ficha_nombre]
    ficha["posicion"]+=cant
    




def dadoA():

    Dado1 = random.randint(1, 6)
    print("JUGADOR 1, Sacó",Dado1)
    input("Presione enter para seguir")
    SacarFicha(Dado1)

def dadoB():

    Dado1 = random.randint(1, 6)
    print("JUGADOR 2, Sacó",Dado1)
    input("Presione enter para seguir")
    SacarFicha2(Dado1)


def SacarFicha(ficha_nombre, dado):
    ficha = fichas["ficha_nombre"]
    if ficha["posicion"]==0:
        ficha = fichas["Ficha 1R"]  
        if dado == 5 and ficha["posicion"]==0:
            ficha["posicion"]=1
            print("Ficha 1R ha entrado al juego")
            actuTab()
        else:
            print("Eso no parece ser un 5... TURNO DE:  ")
            dadoB()
    else: 
        print("Esta ficha ya está afuera")
        DadosGen()
dadoA()
            









