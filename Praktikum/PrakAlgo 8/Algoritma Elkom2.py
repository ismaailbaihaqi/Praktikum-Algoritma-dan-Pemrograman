print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


"""
Program Perhitungan Tarif Taksi pada waktu tertentu
Dikodekan oleh Ismail Baihaqi
"""

#eksekusi
def tarif_siang():
    #tarifawal = 6000
    siang = int(KM) * 6000 + 8000
    print("Total Tarif Anda: ",siang)
def tarif_malam():
    #tarifawal = 8000
    malam = int(KM) * 8000 + 8000
    print("Total Tarif Anda: ",malam)

#Tampilan
print("===Program Perhitungan Tarif Taksi===")
print()

#looping jarak
while True:
    KM = input("Jarak Tempuh (dalam KM)? ")
    if KM == "":
        print("Tidak boleh kosong...Ulangi")
        print()
        continue
    elif not KM.isnumeric():
        print("Masukkan angka saja...Ulangi")
        print()
        continue
    else:
        print()
        break

#looping waktu perjalanan
while True:
    waktu = str(input("Waktu Perjalanan (Siang/Malam)? "))
    if waktu == 'siang' or waktu == 'Siang' or waktu == 'SIANG':
        tarif_siang()
        break
    elif waktu == 'malam' or waktu == 'Malam' or waktu == 'MALAM':
        tarif_malam()
        break
    else:
        print("Input yang anda masukkan salah...Ulangi")
        print()
print("Terima kasih telah menggunakan program layanan taksi kami.")
print("----------------------------------------------------------")

