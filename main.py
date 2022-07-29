import functions as fn

# number = "+593984317433"
# gr_id = "KhJdc47BNFsJszySOqUvpF"
# ms = ""
# pywhatkit.sendwhatmsg_instantly(number, ms, 10, tab_close=True, close_time=4)

# Global constants
FILENAME = "contacts.vcf"

file = open(FILENAME, "r")

print(fn.crearDict(file))
file.close()
