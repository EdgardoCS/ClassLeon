entry0 = [{'album': 'Sound Awake'}, {'artist': 'Karnivool'}, {'year': 2009}]
entry1 = [{'album': 'Blackbird'}, {'artist': 'Alter Bridge'}, {'year': 2007}]
entry2 = [{'album': 'Deadwing'}, {'artist': 'Porcupine Tree'}, {'year': 2005}]
entry3 = [{'album': 'AM'}, {'artist': 'Artic Monkeys'}, {'year': 2013}]
entry4 = [{'album': 'Themata'}, {'artist': 'Karnivool'}, {'year': 2005}]
entry4 = [{'album': 'Eidolon'}, {'artist': 'Rishloo'}, {'year': 2007}]
entry5 = [{'album': 'One Day Remains'}, {'artist': 'Alter Bridge'}, {'year': 2004}]
entry6 = [{'album': 'Feathergun'}, {'artist': 'Rishloo'}, {'year': 2010}]
entry7 = [{'album': 'In Absentia'}, {'artist': 'Porcupine Tree'}, {'year': 2002}]
entry8 = [{'album': 'Asymmetry'}, {'artist': 'Karnivool'}, {'year': 2013}]

myLibrary = [entry0, entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8]

"""
HINTS 

Para acceder a cada dato: 
print(entry1)
print(entry1[0])
print(entry1[0]['album'])
print(entry1[1]['artist'])

condiciones: 
if (entry1[2]['year'] <= 2005):
    print(entry1[2]['year'])
    
Para acceder a dato dentro de myLibrary: 
myLibrary[posicion del dato] 
EJ: quiero acceder al dato entry 2, que se ubica en la posición 2 de myLibrary
print(myLibrary[2])

Ciclo For: 
print(len(myLibrary)
for x in range (0, 9):  =====> largo de myLibray
    print(myLibrary[x])
"""

"""
Ejercicio: 
1. Quiero organizar mi libreria de discos y necesito identificar cuales son de Karnivool, 
para ello, con un ciclo for recorrer variable myLIbrary e imprimir en pantalla cualquier disco
que tenga por artista a Karnivool. 

2. Quiero conocer los discos que fueron lanzados entre 2005 y 2010. 
"""
