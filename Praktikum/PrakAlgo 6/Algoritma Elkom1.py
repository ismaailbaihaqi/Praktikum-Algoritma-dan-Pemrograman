print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print(                                                   )

#Interface
print("===PROGRAM KONVERSI BILANGAN===")
print("1 => Desimal to Binary")
print("2 => Binary to Desimal")
print("3 => Keluar           ")
print("===============================")


#struktur
def struktur():
    while True:
        print()
        data = int(input("Silahkan pilih menu: "))
        if data == 1:
            desimal = int(input("Masukan bilangan: "))
            if desimal==0:
                print(0)
            else:
                print("HasilBagi Sisa Biner")
                bitString=""
                while desimal>0:
                    sisa = desimal % 2
                    desimal = desimal // 2
                    bitString = str(sisa)+bitString
                    print("%5d%8d%12s" % (desimal, sisa, bitString))
                print("Representasi binernya:", bitString)
        elif data == 2:
            bitString=input("Masukan string bit: ")
            desimal=0
            eksponen = len(bitString)-1
            for digit in bitString:
                desimal=desimal+int(digit)*2**eksponen
                eksponen=eksponen-1
            print("Nilai desimal adalah",desimal)
        elif data == 3:
            print("---End---")
            break
struktur()
