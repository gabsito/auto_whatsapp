import functions as fn

# number = "+593984317433"
# gr_id = "KhJdc47BNFsJszySOqUvpF"
# ms = ""
# pywhatkit.sendwhatmsg_instantly(number, ms, 10, tab_close=True, close_time=4)

# Global constants
FILENAME = "contacts.vcf"
msg_2 = """MEGA COMBO  Tortillas de verde+Queso manaba + Bistec + Huevo
*Está más rico que nunca*
🤤😋🤤😋🍳🫓🥩🍳

Hay pocos disponibles Servicio a Domicilio 
Pedidos: wa.me/593978671193"""

msg_1 = '''Disfruta Hoy de   Nuestros Desayunos
 Mami Nida 
 Ya solo 5 Combos  Disponible 😱
6 Humitas 😋
Cuantos le llevo ?'''


CarlosAlberto = "+593978671193"
belen = "+593962557948"
gaby = "+593991408734"
img_path = "img.jpeg"
img_testimonio = "testimonio.jpeg"
SECTORS1 = ["Maestro", "Orquideas"]
SECTORS2 = ["Huancavilca", "Maestro", "Vergeles", "Geranios", "Aurora", "Bastion"]

file = open(FILENAME, "r")
dic = fn.createDict(file)
bigDic = fn.order_by_sectors(dic)
fn.toCSV(bigDic, "test")
# fn.sendSoloWsp(belen, img_path, MSG)
fn.sendWsp(bigDic, SECTORS1, img_path, msg_1)
fn.sendWsp(bigDic, SECTORS2, img_path, msg_2)

file.close()


