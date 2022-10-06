print("    ██╗███████╗███╗   ███╗ █████╗ ██╗██╗         ")
print("    ██║██╔════╝████╗ ████║██╔══██╗██║██║         ")
print("    ██║███████╗██╔████╔██║███████║██║██║         ")
print("    ██║╚════██║██║╚██╔╝██║██╔══██║██║██║         ")
print("    ██║███████║██║ ╚═╝ ██║██║  ██║██║███████╗    ")
print("    ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ")
print("                                                 ")

print("Klasifikasi Gempa")
print()
Skala = float(input("Masukkan nilai skala yang akan diukur tingkat Gempanya: "))

if (Skala < 2 ):
    print("Level = Micro")
elif (Skala >= 2) and (Skala < 3):
    print("Level = Very Minor")
elif (Skala >= 3) and (Skala < 4):
    print("Level = Minor")
elif (Skala >= 4) and (Skala < 5):
    print("Level = Light")
elif (Skala >= 5) and (Skala < 6):
    print("Level = Moderate")
elif (Skala >= 6) and (Skala < 7):
    print("Level = Strong")
elif (Skala >= 7) and (Skala < 8):
    print("Level = Major")
elif (Skala >= 8) and (Skala < 10):
    print("Level = Great")
else:
    print("Level = Meteoric")