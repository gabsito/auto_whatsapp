
# Funcion que cuenta los contactos en el archivo.
def contarContactos(file):
    cont = 0
    for line in file:
        if line.find("BEGIN") >= 0:
            cont += 1
    return cont

#Funcion que crea un diccionario siendo las claves los nombres de contacto y el contenido es el numero
def crearDict(file):
    dic = {}
    name = ""
    num = ""
    for line in file:
        if "FN:" in line:
            name = line[line.find(":") + 1:].replace("# ", "").replace("\n", "")
        if "CELL:" in line:
            num = line[line.find(":") + 1:].replace("\n", "")
            if "+" not in num:
                num = "+593" + num[1:].replace("-", "")
        dic[name] = num
    return dic
