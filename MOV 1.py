import random
#BIENVENIDOS
print("Bienvenidos al parqués de Python")
input("Presione ENTER para continuar")
RULE= input("Si conoce las reglas, presione A, de lo contraio B para conocerlas")
if RULE.upper() == "A":
    print("Perfecto, comencemos a jugar")
elif RULE.upper() == "B":
    mensaje = """
    - Cada jugador tiene  4  fichas, las cuales deben llegar a la meta
    - Se inicia por defecto en la cárcel, y se debe sacar un 5 para sacar una ficha
    - Si alguna ficha obtiene un 5, puede empezar a jugar
    - Si no tiene fichas afuera, no podrá mover ninguna ficha
    -MAS TEXTO...

    """
    print(mensaje)



    print("Para sacar una ficha, debe sacar un 5 en el dado")
    print("Si saca un número diferente a 5, pero no tiene fichas afuera, no podrá mover ninguna ficha")
    print("Acá va más texto...")
    input("Presione ENTER para continuar")
else:
    print("No entendí su respuesta, por favor reinicie el programa")
    exit()


Casillas= ["[]"]*68
Individual1= ["[]"]*7
Individual2= ["[]"]*7
fichas={
"Ficha 1R":{"posicion":0, "estado": "activa"},
"Ficha 2AZ":{"posicion":0, "estado": "activa"},
}  

def actuTab():
    global Casillas
    Casillas= ["[]"]*68
    for ficha_nombre, datos in fichas.items():
        poss = datos["posicion"]
        if 0 <= poss < 68:
            Casillas[poss]= f"[{ficha_nombre}]"

    print(" ".join(Casillas)) 


def moverfichas(ficha_nombre, Cant):
    ficha = fichas[ficha_nombre]
    ficha["posicion"]+= Cant
    actuTab()

def DadosGen(ficha_nombre):
    DadoUno = random.randint(1,6)
    DadoDos= random.randint(1,6)
    SumaAmbos= DadoUno + DadoDos
    print(f"Sacó en 1: {DadoUno}, y en 2: {DadoDos} eso suma un total de...: {SumaAmbos}")
    input("ENTER para acepatar")

    moverfichas(ficha_nombre, SumaAmbos)


def SacarFicha(ficha_nombre,dado):
    ficha = fichas[ficha_nombre]
    if ficha["posicion"]==0:
        if dado == 5:
            ficha["posicion"]= 1
            print("Ficha 1R ha entrado al juego")
            actuTab()
        else:
            print("Eso no parece ser un 5... TURNO DE: FICHA 2AZ  ")
            
    else: 
        print("Esta ficha ya está afuera")
        DadosGen(ficha_nombre)
            
def TURNOS (ficha_nombre):
    dado = random.randint(1,6)
    print(f"{ficha_nombre} sacó {dado}")
    input("ENTER para continuar")
    SacarFicha(ficha_nombre,dado)

def INICIO ():
    banana = True
    while banana == True:
        TURNOS("Ficha 1R")
        if fichas["Ficha 1R"]["posicion"]>=68:
            banana=False

            exit()

        TURNOS("Ficha 2AZ" )

        if fichas["Ficha 2AZ"]["posicion"]>=68:
            banana=False

            exit()

INICIO()
        
          

    












