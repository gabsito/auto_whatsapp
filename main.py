import functions as fn

# number = "+593984317433"
# gr_id = "KhJdc47BNFsJszySOqUvpF"
# ms = ""
# pywhatkit.sendwhatmsg_instantly(number, ms, 10, tab_close=True, close_time=4)

# Global constants
FILENAME = "contacts.vcf"

file = open(FILENAME, "r")

dic = fn.createDict(file)
bigDic = fn.order_by_sectors(dic)
fn.toCSV(bigDic, "test")
file.close()
