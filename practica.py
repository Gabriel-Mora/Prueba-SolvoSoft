
import random


cant_jugadores = int(input("Ingrese la cantidad de Jugadores: "))
baraja=["2C","2D","2T","2P","3C","3D2",
        "3T","3P","4C","4D","4T","4P", "5C","5D","4T","4P","5C","5D","5T","5P"
        ,"6C","6D","6T","6P","7C","7D","7T","7P","8C","8D","8T","8P","9C","9D",
        "9T","9P","JC","JD","JT","JP","QC","QD","QT","QP"
        "KC","KD","KT", "KP","AC","AD","AT","AP"]




def ObtenerCartaJugador(baraja):
    i=0
    barajaJugador=[]
    for i in range(2):
        carta= random.choice(baraja)
        barajaJugador.append(carta)
    return barajaJugador

def Menu(cant_jugadores):
    for i in range(cantJugadores):

    
print(ObtenerCartaJugador(baraja))
        
        

    
        
    
    
    
    
