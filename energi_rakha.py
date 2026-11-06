# pemrograman python menghitung energi potensial

MERAH = '\033[91m'
HIJAU = '\033[92m'
BIRU = '\033[94m'
KUNING = '\033[93m'
RESET = '\033[0m' 

print("================================")
print("======== " + BIRU + "ENERGI POTENSIAL" + RESET + "========")
print("================================")
print("")
benda = str(input("Benda            : "))
massa = int(input("Massa            : "))
gravitasi = 9.8  # m/s^2
ketinggian = int(input("ketinggian       : "))
energi_potensial = float(massa * gravitasi * ketinggian)
print("")
print("<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>")
print("")
print("Benda            :", str(benda))
print("Massa            :", str(massa) + " kg")
print("Gravitasi        :", str(gravitasi) + " m/s^2")
print("Ketinggian       :", str(ketinggian) + " m")
print("Energi Potensial :", str(energi_potensial) + " J")
print("")
print("================================")
print("=============SELESAI============")
print("================================")
print("")
print("--------------------------------")

# pemrograman python menghitung energi kinetik

print("")
print("================================")
print("=========" + BIRU + "ENERGI KINETIK" + RESET + "=========")
print("================================")
print("")
benda = str(input("Benda            : "))
massa = int(input("Massa            : "))
kecepatan = int(input("Kecepatan        : "))
energi_kinetik  = float(0.5 * massa * kecepatan ** 2)
print("")
print("<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>")
print("")
print("Benda            :", str(benda))
print("Massa            :", str(massa) + " kg")
print("Kecepatan        :", str(kecepatan) + " m/s")
print("Energi Kinetik   :", str(energi_kinetik) + " J")
print("")
print("================================")
print("=============SELESAI============")
print("================================")