print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")

import time
import math

print('Nama : "Ismail Baihaqi"')
print('Nim : "065002200025"')

x1 = eval(input('Masukan titik kordinat x1: '))
x2 = eval(input('Masukan titik kordinat x2: '))
y1 = eval(input('Masukan titik kordinat y1: '))
y2 = eval(input('Masukan titik kordinat y2: '))

print('Hasil dari jarak antara titik A[{0} , {1}] dan B[{2} , {3}] adalah'.format(x1,x2,y2,y1), math.sqrt((x2-x1)**2+(y2-y1)**2))
time.sleep(50)





