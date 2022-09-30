print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")


import math
print("KALKULATOR PYTHAGORAS BY ISMAIL B.")
print("==================================")
rumus = input('sisi mana yang ingin anda hitung A,B, atau C = ')

if rumus == 'c' or rumus == 'C':
    A = int(input('masukan panjang sisi a = '))
    B = int(input('masukan panjang sisi b = '))
    
    hasil = int(math.sqrt(A**2 + B**2))

elif rumus == 'A' or rumus == 'a':
    B = int(input('masukan panjang sisi b = '))
    C = int(input('masukan panjang sisi c = '))
    if C < B:
        print("panjang sisi c tidak valid!")
        C = int(input('masukan panjang sisi c = '))

    hasil = int(math.sqrt(C**2 - B**2))

elif rumus == 'b' or rumus =='B':
    A = int(input('masukan panjang sisi a = '))
    C = int(input('masukan panjang sisi c = '))
    if C < A:
        print("panjang sisi c tidak valid!")
        C = int(input('masukan panjang sisi c = '))

    hasil = int(math.sqrt(C**2 - A**2))

else:
    print('input salah')

print("panjang sisi {0} adalah {1}".format(rumus,hasil))
#-----------------------------------------------------#