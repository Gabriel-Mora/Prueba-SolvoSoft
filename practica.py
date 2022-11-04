
import random


cant_jugadores = int(input("Ingrese la cantidad de Jugadores: "))
baraja=["2C","2D","2T","2P","3C","3D2",
        "3T","3P","4C","4D","4T","4P", "5C","5D","4T","4P","5C","5D","5T","5P"
        ,"6C","6D","6T","6P","7C","7D","7T","7P","8C","8D","8T","8P","9C","9D",
        "9T","9P","JC","JD","JT","JP","QC","QD","QT","QP"
        "KC","KD","KT", "KP","AC","AD","AT","AP"]

def obtenerUnaCarta(baraja):
    carta= random.choice(baraja)
    return carta
    
def ObtenerCartaJugador(baraja):
    
    i=0
    barajaJugador=[]
    for i in range(2):
        carta= random.choice(baraja)
        barajaJugador.append(carta)
        baraja.pop(carta)
    return barajaJugador

def ObtenerCartaJugadores(cant_jugadores, baraja):
    lista_barajas=[]
    for i in range(cant_jugadores):
        
        lista_barajas.append(ObtenerCartaJugador(baraja))
    return lista_barajas

def Menu(cant_jugadores, baraja ):
    
    for i in range (cant_jugadores):
        respuesta= int(input("Desea otra Carta? 1. Sí o 2.No: "))

        if respuesta== 1:
            

        else if respuesta ==2:
            
        
        

    
print(ObtenerCartaJugador(baraja))
print(Menu(cant_jugadores, baraja))

        
        

    
        
    
    
    
    
