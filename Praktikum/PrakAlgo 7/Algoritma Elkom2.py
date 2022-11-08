print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print(                                                   )

"""
Program kalkulator GLBB
Dikodekan oleh Ismail Baihaqi

"""
print("============================")
print("MENGHITUNG JARAK TEMPUH GLBB")
print("============================")

#v0 = Kecepatan awal
#vt = Kecepatan akhir
#a = Percepatan
#s = Jarak yang ditempuh

def rumus_vt(vawa,wakt,percepata):
    vt = vawa + (percepata*wakt)
    return vt
def rumus_s(v0,t,a):
    jarak = (v0 * t) + ((a*t**2)/2)
    return jarak

def rumus_2vt(vawal1,waktu1,percepatan1):
    cepet2 = (vawal1**2) + (2*percepatan1* rumus_s())
    return cepet2


vawal = float(input("Masukkan v0: "))
waktu = float(input("Masukkan t : "))
percepatan = float(input("Masukkan a : "))

print("kecepatan akhir jika kecepatan awal = {0} waktu = {1} dan percepatan {2} adalah {3} ".format(vawal,waktu,percepatan,rumus_vt(vawal,waktu,percepatan)))

