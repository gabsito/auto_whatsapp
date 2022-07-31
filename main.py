import functions as fn

# number = "+593984317433"
# gr_id = "KhJdc47BNFsJszySOqUvpF"
# ms = ""
# pywhatkit.sendwhatmsg_instantly(number, ms, 10, tab_close=True, close_time=4)

# Global constants
FILENAME = "contacts.vcf"
MSG = """*MAÑANA*
MEGA COMBO
2 Tortillas de verde + Bistec + Huevo
*Está más rico que nunca* 
🤤😋🤤😋🍳🫓🥩🍳
También tendremos :
✓ *Humitas* 🫔🫔🫔🫔
*Entregas 7:00 ~ 11:00 am*
Pedidos: wa.me/593978671193"""

msg_testimonio = '''Si aun está dudanndo de hacer su pedido no esperes más!!!😋😋
100% recomendado, nuestros clientes satisfechos!'''


CarlosAlberto = "+593978671193"
belen = "+593962557948"
gaby = "+593991408734"
img_path = "img.jpeg"
img_testimonio = "testimonio.jpeg"
SECTORS = ["Maestro", "Orquideas"]


file = open(FILENAME, "r")
dic = fn.createDict(file)
bigDic = fn.order_by_sectors(dic)
fn.toCSV(bigDic, "test")
# fn.sendSoloWsp(belen, img_path, MSG)
fn.sendWsp(bigDic, SECTORS, img_path, MSG)


file.close()


