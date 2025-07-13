import random
#BIENVENIDOS

Casillas= ["[]"]*68
Individual1= ["[]"]*7
Individual2= ["[]"]*7
fichas={
"Ficha 1R":{"posicion":0, "estado": "activa"},
"Ficha 2AZ":{"posicion":0, "estado": "activa"},
}
def actuTab():
    Casillas= ["[]"]*68
    for ficha_nombre, datos in fichas.items():
        poss = datos["posicion"]
        if 0 <= poss < 68:
            Casillas[poss]= f"[{ficha_nombre}]"
    print(" ".join(Casillas))            

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
def SacarFicha2(dado):
    ficha2=fichas["Ficha 2AZ"]
    if ficha2["posicion"]==0:
         ficha = fichas["Ficha 2AZ"]  
         if dado == 5 and ficha["posicion"]==0:
            ficha["posicion"]=1
            print("Ficha 2AZ ha entrado al juego")
            actuTab()
         else:
            print("Eso no parece ser un 5... TURNO DE:  ")
            dadoA()

def SacarFicha(dado):
    ficha=fichas["Ficha 1R"]
    if ficha["posicion"]==0:
        ficha = fichas["Ficha 1R"]  
        if dado == 5 and ficha["posicion"]==0:
            ficha["posicion"]=1
            print("Ficha 1R ha entrado al juego")
            actuTab()
        else:
            print("Eso no parece ser un 5... TURNO DE:  ")
            dadoB()
dadoA()
            









