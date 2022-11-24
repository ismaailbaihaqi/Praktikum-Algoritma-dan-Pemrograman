print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


"""
Program untuk bill pesanan makanan
Dikodekan oleh Ismail Baihaqi
18/11/2022
"""
print("===========================")
print(" Welcome to the restaurant ")
print("---------------------------")

def food():
    print("Food:")
    print("1. Nasi Goreng Gila 15K\n"
    "2. Mie Goreng Komplit 30K\n"
    "3. Ayam Geprek 30K\n"
    "4. Es Teh manis pake gula 3K\n"
    "5. Es Buah 10K"
    )

def price(x):
    if x == '1':
        print("1")
        print("Receipt")
        print("Nasi Goreng Gila")
        print("Pesanan sedang diproses")
        x = 15000
        print()
    elif x == '2':
        print("2")
        print("Receipt")
        print("Mie Goreng Komplit")
        print("Pesanan sedang diproses")
        x = 15000     
        print()
    elif x == '3':
        print("3")
        print("Receipt")
        print("Ayam Geprek")
        print("Pesanan sedang diproses")
        x = 15000
        print()
    elif x == '4':
        print("Es Teh manis pake gula")
    elif x == '5':
        print("Es Buah")

def tulis(s):
    if s == '1':
        f = open("Pesanan.txt",'a')
        f.write(
        "\n1"
        "\nReceipt"
        "\nNasi Goreng Gila")
        f.close()
    elif s == '2':
        f = open("Pesanan.txt",'a')
        f.write(
        "\n2"
        "\nReceipt"
        "\nMie Goreng Komplit")
        f.close()   
    elif s == '3':
        f = open("Pesanan.txt",'a')
        f.write(
        "\n3"
        "\nReceipt"
        "\nAyam Geprek")
        f.close()
    elif s == '4':
        f = open("Pesanan.txt",'a')
        f.write(
        "\nEs Teh manis pake gula")
        f.close()
    elif s == '5':
        f = open("Pesanan.txt",'a')
        f.write(
        "\nEs Buah"
        )
        f.close()



while True:
    food()
    pesan = input("Masukkan pesanan anda : ")
    print()
    price(pesan)
    tulis(pesan)
    cont = input("Mau Pesan lagi? (Y/G)").upper()
    if cont == "Y":
        continue
    elif cont == "G":
        print("Terima kasih telah menggunakan program ini....Enjoy your meal:)")
        print()
        break