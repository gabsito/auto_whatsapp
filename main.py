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
*Entregas 7:00 ~ 11:00 am*"""
CarlosAlberto = "+593978671193"
img_path = "img.jpeg"

file = open(FILENAME, "r")

dic = fn.createDict(file)
bigDic = fn.order_by_sectors(dic)
fn.toCSV(bigDic, "test")
fn.sendSoloWsp(CarlosAlberto,img_path, MSG)

file.close()


