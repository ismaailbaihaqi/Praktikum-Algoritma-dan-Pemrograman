print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


"""
Program pembalikan input angka dari user
Dikodekan oleh Ismail Baihaqi
"""

def Diputar(s): 
    str = "" 
    for i in s: 
        str = i + str 
    return str 

s = input("Masukan sebuah bilangan int positif: ")

print ("Hasil pembalikan angka: ",end="") 
print (Diputar(s))

