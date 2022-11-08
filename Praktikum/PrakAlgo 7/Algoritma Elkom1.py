print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print(                                                   )

"""
Program kalkulator GLBB
Dikodekan oleh: Ismail Baihaqi

"""

print("============================")
print("MENGHITUNG JARAK TEMPUH GLBB")
print("============================")



def GLBB():
    #Input data
    v0 = int(input("Masukan v0: "))
    t  = int(input("Masukan t: "))
    a  = int(input("Masukan a: "))

    #Structure
    s = v0 * t + (1/2) * a * t**2
    
    #Cetak
    print("Diketahui:")
    print("Jarak tempuh jika kecepatan awal = ", v0)
    print("Waktu = ", t)
    print("Percepatan = ", a)
    print("Hasil perhitungan kalkulator GLBB = ", s)
GLBB()