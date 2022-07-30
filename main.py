import functions as fn

# number = "+593984317433"
# gr_id = "KhJdc47BNFsJszySOqUvpF"
# ms = ""
# pywhatkit.sendwhatmsg_instantly(number, ms, 10, tab_close=True, close_time=4)

# Global constants
FILENAME = "contacts.vcf"
MSG = """*REGRESÓ* EL MEGA COMBO de Tortillas de verde + Bistec + Huevo
*Está más rico que nunca* 
🤤😋🤤😋🍳🫓🥩🍳

Hay pocos disponibles para *MAÑANA* Separa el tuyo con tiempo.
*Entregas 7:00 ~ 11:00 am*
Contacto: wa.me/593978671193"""
CarlosAlberto = "+593978671193"
img_path = "img.jpeg"
SECTORS = ["Huancavilca", "Maestro", "Orquideas"]

file = open(FILENAME, "r")
dic = fn.createDict(file)
bigDic = fn.order_by_sectors(dic)
fn.toCSV(bigDic, "test")
fn.sendWsp(bigDic, SECTORS, img_path, MSG)

file.close()


