import random
import os

def generar_bash(cantidad):
    procesos = os.listdir("procesos")
    with open("bash.txt", 'w') as archivo:
        for i in range(cantidad):
            indice = random.randrange(len(procesos))
            archivo.write(procesos[indice] + " ")
            archivo.write(str(random.randrange(1,i+2)) + " ")
            archivo.write(str(random.randrange(1,4)) + "\n")

generar_bash(10)