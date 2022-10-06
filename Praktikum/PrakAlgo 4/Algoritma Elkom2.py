print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


#Tampilan Prodi
print("=======================")
print("     PROGRAM STUDI     ")
print("=======================")
print("-> Teknik Informatika  ")
print("-> Sistem Informasi    ")
print("-> MultiMedia          ")
print("-----------------------")
print("Silahkan pilih Prodi yang ada di atas")
print()

#Input-an
Prodi   = input("Masukkan Program Studi       : ")
Payment = input("Pembayaran via Tunai/Cicilan : ")
print()

#Nested if
if Payment == 'Tunai' or Payment == 'tunai':
    if Prodi == 'Teknik Informatika' or Prodi == 'teknik informatika':
        print("---Anda adalah Mahasiswa Jurusan Teknik Informatika---")
        print("Pembayaran via TUNAI")
        print("Biaya kuliah/Semester --> RP.12,000,000,-")

    elif Prodi == 'Sistem Informasi' or Prodi == 'sistem informasi':
        print("---Anda adalah Mahasiswa Jurusan Sistem Informasi---")
        print("Pembayaran via TUNAI")
        print("Biaya kuliah/Semester --> RP.11,000,000,-")

    elif Prodi == 'Multimedia' or Prodi == 'multimedia':
        print("---Anda adalah Mahasiswa Jurusan MultiMedia---")
        print("Pembayaran via TUNAI")
        print("Biaya kuliah/Semester --> RP.12,000,000,-")


elif Payment == 'Cicilan' or Payment == 'cicilan':
    if Prodi == 'Teknik Informatika' or Prodi == 'teknik informatika':
        print("---Anda adalah Mahasiswa Jurusan Teknik Informatika---")
        print("Pembayaran via CICILAN")
        print("Biaya kuliah/Semester --> RP.13,500,000,-")
        Cicilan = input("Cicilan 1-5 kali: ")
        if Cicilan == '2':
            print("Cicilan (2x) --> RP.6,750,000,-")
        elif Cicilan == '3':
            print("Cicilan (3x) --> RP.4,500,000,-")   
        elif Cicilan == '4':
            print("Cicilan (4x) --> RP.3,375,000,-")
        elif Cicilan == '5':
            print("Cicilan (5x) --> RP.2,700,000,-")

    elif Prodi == 'Sistem Informasi' or Prodi == 'sistem informasi':
        print("---Anda adalah Mahasiswa Jurusan Sistem Informasi---")
        print("Pembayaran via CICILAN")
        print("Biaya kuliah/Semester --> RP.12,500,000,-")
        Cicilan = input("Cicilan 1-5 kali: ")
        if Cicilan == '2':
            print("Cicilan (2x) --> RP.6,250,000,-")
        elif Cicilan == '3':
            print("Cicilan (3x) --> RP.4,166,666,-")
        elif Cicilan == '4':
            print("Cicilan (4x) --> RP.3,125,000,-")
        elif Cicilan == '5':
            print("Cicilan (5x) --> RP.2,500,000,-")

    elif Prodi == 'MultiMedia' or Prodi == 'multimedia':
        print("---Anda adalah Mahasiswa Jurusan MultiMedia---")
        print("Pembayaran via CICILAN")
        print("Biaya kuliah/Semester --> RP.13,000,000,-")
        Cicilan = input("Cicilan 1-5 kali: ")
        if Cicilan == '2':
            print("Cicilan (2x) --> RP.6,500,000,-")
        elif Cicilan == '3':
            print("Cicilan (3x) --> RP.4,333,333,-")
        elif Cicilan == '4':
            print("Cicilan (4x) --> RP.3,250,000,-")
        elif Cicilan == '5':
            print("Cicilan (5x) --> RP.2,600,000,-")


else:
    print("Input salah")