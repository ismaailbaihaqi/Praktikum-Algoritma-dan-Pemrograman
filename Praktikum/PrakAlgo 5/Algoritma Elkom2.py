print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


#input
total     = int(input("Masukan total harga belanjaan anda: Rp "))
uang_anda = int(input("Masukan jumlah uang anda: Rp "))
print()
#struktur
data      = uang_anda - total

print("Kembalian anda sejumlah Rp ",data,"dengan Rincian kembalian")

RP = [100000, 50000, 20000, 10000, 5000, 1000, 500, 200, 100, 50, 25]
for x in range (0, 10):
    i=0
    while data >= RP[x]:
        data = data - RP[x]
        i = i+1
        if (i>0):
            print ("| Uang kertas Rp. %d sebanyak %d lembar" %(RP[x], i))
        else:
            print("Selesai")

#Footer
print("---Bye---")
        