# Praktik: Analisis Nilai Mahasiswa

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []

    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)

    return lulus


# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menghitung statistik
banyak = len(nilai)
total = sum(nilai)
minimum = min(nilai)
maksimum = max(nilai)
rata = rata_rata(nilai)

# Memeriksa kelulusan
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak - jumlah_lulus

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print("Seluruh nilai       :", nilai)
print("Banyak data         :", banyak)
print("Total nilai         :", total)
print(f"Rata-rata           : {rata:.2f}")
print("Nilai minimum       :", minimum)
print("Nilai maksimum      :", maksimum)
print("Nilai yang lulus    :", lulus)
print("Jumlah mahasiswa lulus       :", jumlah_lulus)
print("Jumlah belum lulus            :", jumlah_belum_lulus)

print("\n=== PENGUJIAN FUNGSI ===")
print(f"Rata-rata [60, 70, 80] = {rata_rata([60, 70, 80]):.2f}")
print("Minimum [60, 70, 80] =", min([60, 70, 80]))
print("Maksimum [60, 70, 80] =", max([60, 70, 80]))
print("Jumlah lulus [60, 70, 80] =", len(nilai_lulus([60, 70, 80])))
print("Jumlah lulus [59, 60, 61] =", len(nilai_lulus([59, 60, 61])))
print("Rata-rata list kosong =", rata_rata([]))