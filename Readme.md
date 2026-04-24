# IFB-208 — Pengolahan Citra Digital

> Kumpulan praktikum mata kuliah **Pengolahan Citra Digital** (IFB-208) Semester 4.
> Dibangun menggunakan Python, OpenCV, dan PyQt5 — dari loading gambar sederhana sampai GUI interaktif buat ngatur brightness & contrast!

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat-square&logo=opencv)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-orange?style=flat-square&logo=qt)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Semester](https://img.shields.io/badge/Semester-4-purple?style=flat-square)

---

## Tentang Project Ini

Repository ini berisi semua assignment dari praktikum **Pengolahan Citra Digital**.
Setiap assignment dibangun secara progresif — mulai dari konsep paling dasar sampai implementasi GUI yang interaktif.

## 📝 Daftar Assignment

### A1 — Basic Image Loading & Display

> **Konsep:** Membaca dan menampilkan gambar menggunakan OpenCV

Titik awal dari semuanya. Di sini kita belajar cara OpenCV membaca file gambar, memahami struktur array BGR, dan menampilkan hasilnya ke layar.

**Yang dipelajari:**

- `cv2.imread()` dan `cv2.imshow()`
- Perbedaan format BGR (OpenCV) vs RGB (normal)
- Struktur data gambar sebagai NumPy array

---

### A2 — PyQt5 GUI Image Viewer

> **Konsep:** Membangun antarmuka grafis pertama untuk menampilkan gambar

Dari terminal ke GUI! Assignment ini memperkenalkan PyQt5 sebagai framework untuk bikin aplikasi desktop dengan tampilan yang lebih manusiawi.

**Yang dipelajari:**

- Setup window PyQt5 dari file `.ui` (Qt Designer)
- Konversi format gambar OpenCV → PyQt5 (QPixmap)
- Event handling dasar (tombol buka file, dll.)

---

### A3 — Manual Grayscale Conversion

> **Konsep:** Point Operations — konversi grayscale secara manual

Nggak pakai `cv2.cvtColor()` bawaan! Kita hitung sendiri nilai grayscale per piksel pakai rumus luminance standar. Ini inti dari *point operations* — transformasi yang hanya bergantung pada nilai satu piksel.

**Rumus yang digunakan:**

```
Gray = 0.299×R + 0.587×G + 0.114×B
```

**Yang dipelajari:**

- Konsep point operations
- Iterasi manual per piksel vs. operasi vektor NumPy
- Menampilkan hasil di GUI PyQt5

---

### A4 — Brightness Adjustment dengan GUI

> **Konsep:** Point Operations — manipulasi kecerahan gambar secara interaktif

Nambahin atau ngurangin kecerahan gambar pakai slider. Setiap gerakan slider langsung update tampilan gambar secara *real-time*. Belajar pentingnya *clipping* supaya nilai piksel nggak overflow.

**Rumus yang digunakan:**

```
Piksel_baru = clip(Piksel_lama + nilai_brightness, 0, 255)
```

**Yang dipelajari:**

- Slider widget di PyQt5
- Operasi aritmatika pada array gambar dengan NumPy
- Clipping nilai piksel dengan `np.clip()`

---

### A5 — Contrast Adjustment dengan GUI

> **Konsep:** Point Operations — manipulasi kontras gambar secara interaktif

Kalau brightness itu penjumlahan, contrast itu perkalian. Kita pakai faktor pengali untuk meregangkan atau mempersempit rentang intensitas piksel.

**Rumus yang digunakan:**

```
Piksel_baru = clip(Piksel_lama × faktor_contrast, 0, 255)
```

**Yang dipelajari:**

- Perkalian skalar pada array NumPy
- Perbedaan efek visual brightness vs. contrast
- Kombinasi slider untuk kontrol interaktif

---

## ⚙️ Cara Menjalankan

### 1. Prasyarat

Pastikan Python sudah terinstall (versi **3.8 - 3.11** disarankan).

```bash
python --version
```

### 2. Install Dependensi

```bash
pip install opencv-python PyQt5 numpy scipy scikit-image Pillow
```

Atau kalau ada file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Jalankan Assignment

Masuk ke folder assignment yang diinginkan, lalu jalankan file Python-nya:

```bash
# Contoh menjalankan Assignment 4
cd p1/A4
python a4_brightness.py
```

---

## 🛠️ Tech Stack

| Library                | Kegunaan                            |
| ---------------------- | ----------------------------------- |
| **Python 3.8+**  | Bahasa pemrograman utama            |
| **OpenCV**       | Baca, tulis, dan proses gambar      |
| **PyQt5**        | Framework GUI desktop               |
| **NumPy**        | Operasi array/matriks pada piksel   |
| **SciPy**        | Operasi matematis lanjutan          |
| **scikit-image** | Algoritma pengolahan citra tambahan |
| **Pillow (PIL)** | Alternatif baca/tulis format gambar |

---

## 📁 Format File Gambar yang Didukung

```
✅ JPG / JPEG
✅ PNG
✅ BMP
✅ TIFF
```

---

## 👤 Informasi

|                       |                                  |
| --------------------- | -------------------------------- |
| **Mata Kuliah** | IFB-208 Pengolahan Citra Digital |
| **Semester**    | 4                                |
| **Tipe**        | Praktikum / Lab Course           |

---

## 📄 Lisensi

Repository ini dibuat untuk keperluan **akademik** mata kuliah IFB-208.
Silakan dijadikan referensi belajar, tapi jangan lupa pahami konsepnya ya — bukan sekadar copy-paste! 😄

---

<div align="center">
  <sub>Dibuat dengan ☕ dan sedikit debugging session tengah malam</sub>
</div>
