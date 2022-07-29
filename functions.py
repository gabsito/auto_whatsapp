# Author: Gabriel Castro
# github: gabsito
# Last commit: 29/7/2022

from os.path import exists


# Funcion que cuenta los contactos en el archivo.
def countContacts(file):
    cont = 0
    for line in file:
        if line.find("BEGIN") >= 0:
            cont += 1
    return cont


# Funcion que crea un diccionario siendo las claves los nombres de contacto y el valor es el numero
def createDict(file):
    dic = {}
    name = ""
    num = ""
    for line in file:
        if "FN:" in line:
            name = line[line.find(":") + 1:].replace("# ", "").replace("\n", "").replace(" ", "")
        elif "CELL:" in line:
            num = line[line.find(":") + 1:].replace("\n", "")
            if "+" not in num:
                num = "+593" + num[1:].replace("-", "")
        dic[name] = num
    return dic


# Funcion que crea un diccionario ordenado por sectores.
def order_by_sectors(dic):
    bigDic = {"Huancavilca": {}, "Maestro": {}, "Vergeles": {}, "Aurora": {}, "Bastion": {}, "Orquideas": {},
              "Sin Sector": {}, "CDA": {}}
    for contact in dic.keys():
        if "(h)" in contact.lower() or "huancavilca" in contact.lower():
            bigDic["Huancavilca"][contact] = dic[contact]
        elif "(v)" in contact.lower() or "vergeles" in contact.lower():
            bigDic["Vergeles"][contact] = dic[contact]
        elif "(m)" in contact.lower() or "maestro" in contact.lower():
            bigDic["Maestro"][contact] = dic[contact]
        elif "(au)" in contact.lower() or "aurora" in contact.lower():
            bigDic["Aurora"][contact] = dic[contact]
        elif "(bast)" in contact.lower() or "bastion" in contact.lower():
            bigDic["Bastion"][contact] = dic[contact]
        elif "(or)" in contact.lower() or "orquideas" in contact.lower() or "(o)" in contact.lower():
            bigDic["Orquideas"][contact] = dic[contact]
        elif "cda" in contact.lower() or "avt" in contact.lower():
            bigDic["CDA"][contact] = dic[contact]
        else:
            bigDic["Sin Sector"][contact] = dic[contact]
    return bigDic


# Funcion que crea un csv con los datos del diccionario
def toCSV(dic, filename):
    if not exists(filename + ".csv"):
        file = open(filename + ".csv", "w")
        file.write("ID,Sector,nombre,telefono\n")
        id = 1
        for sector in dic.keys():
            for contact in dic[sector].keys():
                file.write(str(id) + "," + sector + "," + contact + "," + dic[sector][contact] + "\n")
                id+=1
        file.close()
        print(filename + ".csv created!")
    else:
        print("file already exist!")
