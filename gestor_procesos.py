def leer_bash():
    with open("bash.txt", 'r') as archivo:
        return archivo.readlines()

def ajustar_formato(proceso):
    temporal = proceso[:-1].split()
    temporal[1] = int(temporal[1])
    temporal[2] = int(temporal[2])
    return temporal

def ordenar_procesos(procesos):
    procesos.sort(key=lambda x: x[2], reverse=True)
    procesos.sort(key=lambda x: x[1])
    return procesos

def bash_procesos():
    bash = leer_bash()

    for i in range(len(bash)):
        bash[i] = ajustar_formato(bash[i])
    
    bash = ordenar_procesos(bash)
    return bash


print(bash_procesos())