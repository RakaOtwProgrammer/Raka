# Input Hasil raport siswa

# Ini hanya warna jangan di ubah

HIJAU = "\033[1;32m"
BIRU = "\033[1;40m"
RESET = "\033[0m"

def input_hijau(prompt):
    try:
        return input(HIJAU + prompt)
    finally:
        print(RESET, end="", flush=True)

print("============================================")
print("------------ " + BIRU + "HASIL RAPORT SISWA" + RESET + " ------------")
print("============================================")
print("")

Nama = input_hijau("Nama                  : ") 

Nilai_harian = int(input_hijau("Nilai harian          : "))

Nilai_mid_harian = int(input_hijau("Nilai mid harian      : "))

Nilai_akhir_semester = int(input_hijau("Nilai akhirsemester   : "))

Nama_lengkap_siswa = input_hijau("Nama lengkap siswa    : ")

Nilai_akhir = float(Nilai_harian + Nilai_mid_harian + Nilai_akhir_semester) / 3

print("")
print("================ " + BIRU + "HASIL NILAI" + RESET + " ===============")
print("")
print("Nilai harian          : " + HIJAU + str(Nilai_harian) + RESET)
print("Nilai mid harian      : " + HIJAU + str(Nilai_mid_harian) + RESET)
print("Nilai akhir semester  : " + HIJAU + str(Nilai_akhir_semester) + RESET)
print("Nilai akhir           : " + HIJAU + str(Nilai_akhir) + RESET)

print("")
print("============================================")
print("------------------ " + BIRU + "SELESAI" + RESET + " -----------------")
print("============================================")