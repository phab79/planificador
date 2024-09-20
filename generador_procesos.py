import random

def generar_procesos(cantidad):
    prefijo = "procesos/proceso_"
    for i in range(cantidad):
        nombre_archivo = prefijo + str(i) + ".txt"
        cant_instrucciones = random.randrange(10, 16)
        # Abre el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            for i in range(cant_instrucciones):
                flag = random.randrange(4)
                if flag:
                    archivo.write('EXEC\n')
                else:
                    archivo.write('WAIT\n')
            archivo.write('EXEC')

generar_procesos(5)
