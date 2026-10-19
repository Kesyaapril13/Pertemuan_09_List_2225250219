
# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Kesya Nur Aprilliani  
**NIM:** 2225250219  
**Kelas:** 3E  
**Program Studi:** Pendidikan Matematika  
**Mata Kuliah:** Algoritma dan Pemrograman

## 1. Tujuan

Mengolah kumpulan data numerik menggunakan list Python, melakukan akses dan manipulasi elemen, serta menghitung jumlah, banyak data, nilai minimum, maksimum, dan rata-rata.

## 2. Struktur Program

| No. | Nama File | Keterangan |
|---|---|---|
| 1 | `01_buat_list.py` | Membuat list dan menyimpan data |
| 2 | `02_indeks_slicing.py` | Mengakses elemen dengan indeks dan slicing |
| 3 | `03_manipulasi_list.py` | Menambah, mengubah, menyisipkan, dan menghapus elemen |
| 4 | `04_agregasi_nilai.py` | Menghitung jumlah, minimum, maksimum, dan rata-rata |
| 5 | `05_filter_kelulusan.py` | Memisahkan nilai berdasarkan batas kelulusan |
| 6 | `06_fungsi_statistik.py` | Mengolah data menggunakan fungsi |
| 7 | `analisis_nilai_mahasiswa.py` | Praktik analisis nilai mahasiswa |

## 3. Cara Menjalankan

Program dijalankan menggunakan Python melalui terminal VS Code.

1. Buka folder proyek di VS Code.
2. Buka terminal melalui menu **Terminal → New Terminal**.
3. Jalankan program dengan perintah:

```bash
python analisis_nilai_mahasiswa.py
```

Sesuaikan perintah dengan lokasi dan nama file yang digunakan.

## 4. Hasil Pengujian

| No. | Input | Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Berhasil |
| 2 | `[60, 70, 80]` | Minimum dan maksimum | 60 dan 80 | 60 dan 80 | Berhasil |
| 3 | `[60, 70, 80]` | Jumlah nilai lulus | 3 | 3 | Berhasil |
| 4 | `[59, 60, 61]` | Batas kelulusan 60 | 2 nilai lulus | 2 nilai lulus | Berhasil |
| 5 | `[]` | List kosong pada fungsi rata-rata | Tidak terjadi error | Perlu diuji | Belum diuji |

## 5. Refleksi

Melalui latihan ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel. Indeks membantu mengakses elemen tertentu, sedangkan perulangan memudahkan pengolahan seluruh data. Saya juga memahami cara menghitung statistik sederhana dan menggunakan fungsi agar kode lebih terstruktur.

## 6. Kesimpulan

List Python memudahkan penyimpanan dan pengolahan kumpulan data numerik. Dengan menggunakan indeks, manipulasi list, perulangan, seleksi, dan fungsi, data dapat diolah secara sistematis.

## 7. Dokumentasi

Hasil pengujian dicatat berdasarkan output program yang dijalankan melalui VS Code.
