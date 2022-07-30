# Author: Gabriel Castro
# GitHub: gabsito
# Last commit: 29/7/2022

from os.path import exists
import pywhatkit as pw


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
def order_by_sectors(dic: dict):
    big_dic = {"Huancavilca": {}, "Maestro": {}, "Vergeles": {}, "Aurora": {}, "Bastion": {}, "Orquideas": {},
               "Sin Sector": {}, "CDA": {}}
    for contact in dic.keys():
        if "(h)" in contact.lower() or "huancavilca" in contact.lower():
            big_dic["Huancavilca"][contact] = dic[contact]
        elif "(v)" in contact.lower() or "vergeles" in contact.lower():
            big_dic["Vergeles"][contact] = dic[contact]
        elif "(m)" in contact.lower() or "maestro" in contact.lower():
            big_dic["Maestro"][contact] = dic[contact]
        elif "(au)" in contact.lower() or "aurora" in contact.lower():
            big_dic["Aurora"][contact] = dic[contact]
        elif "(bast)" in contact.lower() or "bastion" in contact.lower():
            big_dic["Bastion"][contact] = dic[contact]
        elif "(or)" in contact.lower() or "orquideas" in contact.lower() or "(o)" in contact.lower():
            big_dic["Orquideas"][contact] = dic[contact]
        elif "cda" in contact.lower() or "avt" in contact.lower():
            big_dic["CDA"][contact] = dic[contact]
        else:
            big_dic["Sin Sector"][contact] = dic[contact]
    return big_dic


# Funcion que crea un csv con los datos del diccionario
def toCSV(dic: dict, filename: str):
    if not exists(filename + ".csv"):
        file = open(filename + ".csv", "w")
        file.write("ID,Sector,nombre,telefono\n")
        count = 1
        for sector in dic.keys():
            for contact in dic[sector].keys():
                file.write(str(count) + "," + sector + "," + contact + "," + dic[sector][contact] + "\n")
                count += 1
        file.close()
        print(filename + ".csv created!")
    else:
        print("file already exist!")


# Funcion que envia mensajes a todos los numeros del diccionario
def sendWsp(dic: dict, sectors: list, img_path: str, msg: str):
    for sector in dic.keys():
        if sector in sectors:
            for number in dic[sector].values():
                pw.sendwhats_image(number, img_path, msg, 15, True, 3)


# Funcion que envia un mensaje ocn imagen a un solo numero
def sendSoloWsp(number: str, img_path: str, msg: str):
    pw.sendwhats_image(number, img_path, msg, 15, True, 3)
