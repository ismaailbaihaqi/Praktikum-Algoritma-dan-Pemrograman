print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print(                                                   )


while True:
    isi=input("Masukan list angka (Integer) : ")
    print("----------------")
    split = isi.split()
    for x in split[0:]:
        x = int(x)
        if x % 2 == 1:
            print(x, "adalah angka ganjil")
        elif x % 2 == 0:
            print(x, "adalah angka genap")
    if x % 2 == 0:
        print("List angka memiliki angka genap")
    else:
        print("List angka tidak memiliki angka genap")
    print("----------------")
    q = input("Exit? [Yes/No] ")
    if (q == "yes" or q == "Yes" or q == "YES"):
        break
    print()