
#Bienvenida
import random
Dado1 = random.randint(1, 6)
Dado2=random.randint(1, 6)
Tablero= []

print(Tablero)
def movimiento1(Ficha1, Ficha2):
  while Tablero[Ficha1] != 20 :
    Dado1 = random.randint(1, 6)
    Dado2=random.randint(1, 6)
    print("El resultado es {} y {}".format(Dado1,Dado2))
    Mueve1= (Dado1 + Dado2)
    comomoverse=int(input("¿JUGADOR 1. Desea mover únicamente una ficha o dos? Una: 1, Dos: 2 "))
    if comomoverse==1:
      Ficha1+=Mueve1
      print(Ficha1)
    elif comomoverse==2:
      CUALFICHA1=int(input("¿JUGADOR 1. ¿Qué ficha desea mover {} movimientos? (1 o 2)".format(Dado1)))
      CUALFICHA2=int(input("¿JUGADOR 1. ¿Qué ficha desea mover {} movimientos? (1 o 2)".format(Dado2)))
      if CUALFICHA1==1:
        Ficha1+=Dado1
        Ficha2+=Dado2
        print(Ficha1)
        print(Ficha2)

      elif CUALFICHA2==2:
        Ficha2+=Dado2
        Ficha1+=Dado1
      print(Ficha2)
      print(Ficha1)
      if Ficha1 or Ficha2 >= len(Tablero):
        break
  return(Ficha1, Ficha2)
  

def movimiento2(Ficha2):
    while Tablero[Ficha2] != 20 :
      Dado1 = random.randint(1, 6)
      Dado2=random.randint(1, 6)
      print("El resultado es {} y {}".format(Dado1,Dado2))
      Mueve2= (Dado1 + Dado2)
      comomoverse=int(input("¿JUGADOR 2. Desea mover únicamente una ficha o dos? Una: 1, Dos: 2 "))
      if comomoverse==1:
        Ficha2+=Mueve2
        print(Ficha2)
        if Ficha2 >= len(Tablero):
          break
    return(Ficha2)
Ficha1=0
Ficha2=0

Ficha1, Ficha2 = movimiento1(Ficha1, Ficha2), movimiento2(Ficha2)
print("H")

