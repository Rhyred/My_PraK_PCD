import sys
import cv2
import os
import numpy as np
import math 
import matplotlib
matplotlib.use('Agg') # anti gelud PyQt5 vs Matplotlib
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from konvolusi import konvolusi_2d

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'E1.ui')
        loadUi(ui_path, self) 
        
        self.image = None
        self.setWindowTitle("My_Program_[152024141]_rhyred")
        # --- KONEKSI TOMBOL ---
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        
        # --- KONEKSI MENU P1 ---
        self.actionLoad_Image.triggered.connect(self.loadClicked)
        self.actionGrayScale.triggered.connect(self.grayClicked)
        self.actionBrightness.triggered.connect(self.brightness)
        self.actionSimple_Contrast.triggered.connect(self.contrast)
        self.actionContrast_Stretching.triggered.connect(self.contrastStretching)
        self.actionNegative_Image.triggered.connect(self.negativeImage)
        self.actionBiner_Image.triggered.connect(self.binerImage)
        
        # --- KONEKSI MENU P2 ---
        self.actionGray_Histogram.triggered.connect(self.grayHistogram)
        self.actionRGB_Histogram.triggered.connect(self.rgbHistogram)
        self.actionHistogram_Equalization.triggered.connect(self.histEqualization)
        self.actionTranslasi.triggered.connect(self.translasi)
        self.actionRotasi.triggered.connect(self.rotasi)
        self.actionResize.triggered.connect(self.resizeImage)
        self.actionCrop.triggered.connect(self.cropImage)

        # --- KONEKSI MENU P2 (OPERASI ARITMATIKA - C1) ---
        self.actionTambah.triggered.connect(self.aritmatikaTambah)
        self.actionKurang.triggered.connect(self.aritmatikaKurang)
        self.actionKali.triggered.connect(self.aritmatikaKali)
        self.actionBagi.triggered.connect(self.aritmatikaBagi)

        # --- KONEKSI MENU P2 (OPERASI BOOLEAN - C2) ---
        self.actionAnd.triggered.connect(self.booleanAnd)
        self.actionOr.triggered.connect(self.booleanOr)
        self.actionXor.triggered.connect(self.booleanXor)

        # --- KONEKSI MENU P3 (OPERASI SPASIAL) ---
        self.actionFilter.triggered.connect(self.filteringClicked)
        self.actionMean_Filter.triggered.connect(self.meanFilterClicked)
        self.actionGaussian_Filter.triggered.connect(self.gaussianFilterClicked)
        self.actionSharpening.triggered.connect(self.sharpeningClicked)
        self.actionMedian_Filter.triggered.connect(self.medianFilterClicked)
        self.actionMax_Filter.triggered.connect(self.maxFilterClicked)
        self.actionMin_Filter.triggered.connect(self.minFilterClicked)

        # --- KONEKSI MENU P4 (MODUL E) ---
        self.actionDFT_Smoothing.triggered.connect(self.dftSmoothingClicked)

    def loadClicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if fileName:
            self.image = cv2.imread(fileName)
            self.displayImage(1) 

    def saveClicked(self):
        if self.image is not None:
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self, "Simpan Gambar Hasil", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
            if fileName:
                cv2.imwrite(fileName, self.image)
                print(f"Mantap! Gambar berhasil di-save di: {fileName}")
        else:
            print("Belum ada gambar yang di-load, Bos!")

    def displayImage(self, windows=1):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
                
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        
        if windows == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.imgLabel.setScaledContents(True)
        elif windows == 2:
            self.hasilLabel.setPixmap(QPixmap.fromImage(img))
            self.hasilLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.hasilLabel.setScaledContents(True)

    # FUNGSI P1
    def grayClicked(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            H, W = img.shape[:2]
            gray = np.zeros((H, W), np.uint8)
            for i in range(H):
                for j in range(W):
                    gray[i, j] = img[i, j]
            self.image = gray
            self.displayImage(2)

    def brightness(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            brightness_val = 50
            h, w = img.shape[:2]
            for i in range(h):
                for j in range(w):
                    a = int(img[i, j]) 
                    b = a + brightness_val 
                    if b > 255: b = 255
                    elif b < 0: b = 0
                    img[i, j] = b
            self.image = img
            self.displayImage(2)

    def contrast(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            contrast_val = 1.6 
            h, w = img.shape[:2]
            for i in range(h):
                for j in range(w):
                    a = int(img[i, j]) 
                    b = math.ceil(a * contrast_val) 
                    if b > 255: b = 255
                    elif b < 0: b = 0
                    img[i, j] = b 
            self.image = img
            self.displayImage(2)

    def contrastStretching(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            h, w = img.shape[:2]
            rmin = np.min(img)
            rmax = np.max(img)
            for i in range(h):
                for j in range(w):
                    r = int(img[i, j])
                    if rmax != rmin:
                        s = int(((r - rmin) / (rmax - rmin)) * 255.0)
                    else:
                        s = r
                    if s > 255: s = 255
                    elif s < 0: s = 0
                    img[i, j] = s
            self.image = img
            self.displayImage(2)

    def negativeImage(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            h, w = img.shape[:2]
            for i in range(h):
                for j in range(w):
                    a = int(img[i, j])
                    b = 255 - a
                    img[i, j] = b
            self.image = img
            self.displayImage(2)

    def binerImage(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            h, w = img.shape[:2]
            threshold = 128 
            for i in range(h):
                for j in range(w):
                    a = int(img[i, j])
                    if a > threshold: img[i, j] = 255 
                    else: img[i, j] = 0 
            self.image = img
            self.displayImage(2)

    # FUNGSI P2: HISTOGRAM 
    def grayHistogram(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            
            self.image = img.copy() 
            self.displayImage(2) 
            
            plt.figure("Histogram Grayscale")
            plt.hist(img.ravel(), 256, [0, 256], color='black')
            plt.title('Histogram Citra Grayscale')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Jumlah Piksel')
            plt.xlim([0, 256])
            
            plt.savefig("temp_hist.png") 
            plt.close() 
            
            hist_img = cv2.imread("temp_hist.png")
            cv2.imshow("Histogram Grayscale", hist_img)

    def rgbHistogram(self):
        if self.image is not None:
            if len(self.image.shape) == 3:
                color = ('b', 'g', 'r')
                plt.figure("Histogram RGB")
                for i, col in enumerate(color):
                    histo = cv2.calcHist([self.image], [i], None, [256], [0, 256])
                    plt.plot(histo, color=col)
                    plt.xlim([0, 256])
                
                plt.title('Histogram Citra RGB')
                plt.xlabel('Intensitas Piksel')
                plt.ylabel('Jumlah Piksel')
                
                plt.savefig("temp_hist_rgb.png")
                plt.close()
                
                hist_img_rgb = cv2.imread("temp_hist_rgb.png")
                cv2.imshow("Histogram RGB", hist_img_rgb)
            else:
                print("Bos, ini citra Grayscale/Hitam Putih! Gak bisa dibikin grafik RGB.")

    
    def histEqualization(self):
        if self.image is not None:
            # Pastikan formatnya grayscale dulu sesuai standar modul
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            
            # --- PROSES EKUALISASI HISTOGRAM ---
            equ = cv2.equalizeHist(img)
            
            # Tampilkan gambar hasil ekualisasi ke Label kanan
            self.image = equ.copy()
            self.displayImage(2)
            
            # Bikin dan tampilkan grafik histogram hasil pemerataan (Jalan Ninja)
            plt.figure("Histogram Equalization")
            plt.hist(equ.ravel(), 256, [0, 256], color='black')
            plt.title('Histogram Citra Equalization')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Jumlah Piksel')
            plt.xlim([0, 256])
            
            plt.savefig("temp_hist_equ.png")
            plt.close()
            
            hist_img_equ = cv2.imread("temp_hist_equ.png")
            cv2.imshow("Histogram Ekualisasi", hist_img_equ)

    def translasi(self):
        if self.image is not None:
            # 1. Ambil ukuran panjang (h) & lebar (w) gambar asli
            h, w = self.image.shape[:2]
            
            # 2. Atur seberapa jauh mau digeser (tx = sumbu X/Kanan, ty = sumbu Y/Bawah)
            tx = 100 # Geser ke kanan 100 px
            ty = 50  # Geser ke bawah 50 px
            
            # 3. Bikin matriks perpindahan (Translasi)
            # Rumusnya: [ [1, 0, tx], [0, 1, ty] ]
            M = np.float32([[1, 0, tx], [0, 1, ty]])
            
            # 4. Terapin perpindahannya pake warpAffine
            shifted_img = cv2.warpAffine(self.image, M, (w, h))
            
            # 5. Tampilkan ke hasil Label di kanan
            self.image = shifted_img
            self.displayImage(2)
    
    def rotasi(self):
        if self.image is not None:
            # 1. Ambil ukuran tinggi dan lebar gambar
            h, w = self.image.shape[:2]
            
            # 2. Tentukan titik pusat rotasi (tengah-tengah gambar)
            center = (w // 2, h // 2)
            
            # 3. Bikin matriks rotasi (pusat, sudut 90 derajat, skala 1.0)
            M = cv2.getRotationMatrix2D(center, 90, 1.0)
            
            # 4. Terapkan rotasi pake warpAffine
            rotated_img = cv2.warpAffine(self.image, M, (w, h))
            
            # 5. Tampilkan hasilnya
            self.image = rotated_img
            self.displayImage(2) 

    def resizeImage(self):
        if self.image is not None:
            # Mengubah ukuran gambar jadi 50% dari aslinya
            # fx = skala sumbu x, fy = skala sumbu y
            resized_img = cv2.resize(self.image, (0, 0), fx=0.5, fy=0.5)
            self.image = resized_img.copy()
            self.displayImage(2)

    def cropImage(self):
        if self.image is not None:
            h, w = self.image.shape[:2]
            
            # Tentukan area yang mau dipotong (Slicing Array)
            # Kita potong area tengahnya aja (buang 25% margin di setiap sisi)
            start_row, end_row = int(h * 0.25), int(h * 0.75) 
            start_col, end_col = int(w * 0.25), int(w * 0.75) 
            
            # Eksekusi Crop! (Format slicing OpenCV: image[y1:y2, x1:x2])
            cropped_img = self.image[start_row:end_row, start_col:end_col]
            
            # Wajib pake .copy() biar memori gambar aslinya gak rusak
            self.image = cropped_img.copy() 
            self.displayImage(2)

    # FUNGSI P2: OPERASI ARITMATIKA (C1)
    # Fungsi pembantu untuk ngambil gambar kedua dan nyamain ukurannya
    def _getSecondImageForMath(self):
        options = QFileDialog.Options()
        # Bakal pop up nanya gambar kedua
        fileName, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar KEDUA buat Dioperasiin", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if fileName:
            img2 = cv2.imread(fileName)
            # Jalan Ninja: Samain ukuran img2 dengan img1 biar ga force close!
            h, w = self.image.shape[:2]
            img2_resized = cv2.resize(img2, (w, h))
            return img2_resized
        return None

    def aritmatikaTambah(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath() # Minta gambar 2
            if img2 is not None:
                # cv2.add mencegah nilai nembus 255 (tetep putih, ga balik item)
                added_img = cv2.add(self.image, img2)
                self.image = added_img.copy()
                self.displayImage(2)

    def aritmatikaKurang(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # cv2.subtract mencegah nilai di bawah 0 (tetep item)
                sub_img = cv2.subtract(self.image, img2)
                self.image = sub_img.copy()
                self.displayImage(2)

    def aritmatikaKali(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # Harus diconvert ke float dulu biar ngalinya ga error overflow
                img1_f = self.image.astype(np.float32)
                img2_f = img2.astype(np.float32)
                mul_img = cv2.multiply(img1_f, img2_f)
                
                # Balikin formatnya ke gambar normal (0-255)
                mul_img = np.clip(mul_img, 0, 255).astype(np.uint8)
                self.image = mul_img.copy()
                self.displayImage(2)

    def aritmatikaBagi(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # Jalan ninja pembagian: ditambah 1.0 biar ga error "dibagi dengan nol" (ZeroDivisionError)
                img1_f = self.image.astype(np.float32)
                img2_f = img2.astype(np.float32) + 1.0 
                div_img = cv2.divide(img1_f, img2_f)
                
                div_img = np.clip(div_img, 0, 255).astype(np.uint8)
                self.image = div_img.copy()
                self.displayImage(2)

    # FUNGSI FINAL P2: OPERASI BOOLEAN (C2)
    def booleanAnd(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # Operasi logika AND (Mencari irisan yang sama-sama nyala)
                and_img = cv2.bitwise_and(self.image, img2)
                self.image = and_img.copy()
                self.displayImage(2)

    def booleanOr(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # Operasi logika OR (Gabungin semua yang nyala)
                or_img = cv2.bitwise_or(self.image, img2)
                self.image = or_img.copy()
                self.displayImage(2)

    def booleanXor(self):
        if self.image is not None:
            img2 = self._getSecondImageForMath()
            if img2 is not None:
                # Operasi logika XOR (Menyala jika berbeda, mati jika sama)
                xor_img = cv2.bitwise_xor(self.image, img2)
                self.image = xor_img.copy()
                self.displayImage(2)

    # FUNGSI P3: OPERASI SPASIAL (D1-D6)
    def filteringClicked(self):
        if self.image is not None:
            # 1. Ubah citra masukan menjadi grayscale sesuai modul
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()
            
            # 2. Bikin array piksel Kernel untuk tugas D1 
            # Kita coba pakai kernel [1,1,1 ; 1,1,1 ; 1,1,1] dari modul halaman 3
            kernel = np.array([
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ], dtype=np.float32)
            
            # Catatan: Karena isi kernel 1 semua, gambar bisa jadi terlalu terang (Over-exposure).
            # Kalau nanti mau dinormalisasi (dibagi 9), ubah kodenya jadi: kernel = kernel / 9.0
            
            # 3. Panggil fungsi konvolusi yang di-import
            print("Lagi ngitung konvolusi nih, sabar yak...")
            img_out = konvolusi_2d(img_gray, kernel)
            
            # 4. Tampilkan gambar ke Label kanan
            self.image = img_out.copy()
            self.displayImage(2)
            print("Konvolusi Beres!")
            
    def meanFilterClicked(self):
        if self.image is not None:
            # 1. Konversi ke grayscale
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()
            
            # 2. Bikin Kernel Mean Filter 3x3
            # Sama kayak D1, tapi SEKARANG KITA BAGI 9 !
            kernel = np.array([
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9]
            ], dtype=np.float32)
            
            # 3. Panggil fungsi konvolusi
            print("Lagi nge-blur gambar pake Mean Filter...")
            img_out = konvolusi_2d(img_gray, kernel)
            
            # 4. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Mean Filter Beres! Coba cek hasilnya.")

    def gaussianFilterClicked(self):
        if self.image is not None:
            # 1. Konversi ke grayscale
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()

            # 2. Bikin Kernel Gaussian 3x3 secara dinamis pakai Rumus (8)
            size = 3
            sigma = 1.0 # Standar deviasi sesuai modul
            kernel = np.zeros((size, size), dtype=np.float32)
            center = size // 2
            
            sum_val = 0.0
            for i in range(size):
                for j in range(size):
                    x = j - center
                    y = i - center
                    # Implementasi rumus: G(x,y) = 1/(2*pi*sigma^2) * exp(-(x^2+y^2)/(2*sigma^2))
                    g = (1.0 / (2.0 * math.pi * sigma**2)) * math.exp(-(x**2 + y**2) / (2.0 * sigma**2))
                    kernel[i, j] = g
                    sum_val += g
                    
            # Normalisasi kernel (dibagi total bobot) biar kecerahan gambar tetep seimbang
            kernel = kernel / sum_val
            
            # 3. Panggil fungsi konvolusi dari konvolusi.py
            print("Lagi nge-blur gambar pake Gaussian Filter...")
            img_out = konvolusi_2d(img_gray, kernel)
            
            # 4. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Gaussian Filter Beres! Coba bandingin blurnya sama yang Mean Filter.")

    def sharpeningClicked(self):
        if self.image is not None:
            # 1. Konversi ke grayscale
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()

            # 2. Bikin Kernel Sharpening (High-Pass Filter)
            # Kita pakai kernel (iii) dari Gambar 23 di modul:
            kernel = np.array([
                [ 0, -1,  0],
                [-1,  5, -1],
                [ 0, -1,  0]
            ], dtype=np.float32)

            # --- TUGAS 3 MODUL: KERNEL LAPLACE 5x5 ---
            # Kalau agan mau cobain tugas nomor 3, uncomment (hapus tanda #) kode di bawah ini 
            # dan comment (kasih tanda #) kode kernel 3x3 di atas:
            #
            # kernel = (1.0 / 16.0) * np.array([
            #     [ 0,  0, -1,  0,  0],
            #     [ 0, -1, -2, -1,  0],
            #     [-1, -2, 16, -2, -1],
            #     [ 0, -1, -2, -1,  0],
            #     [ 0,  0, -1,  0,  0]
            # ], dtype=np.float32)

            # 3. Panggil fungsi konvolusi
            print("Lagi menajamkan citra (Sharpening)...")
            img_out = konvolusi_2d(img_gray, kernel)
            
            # 4. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Sharpening Beres! Cek deh, garis tepi objeknya pasti makin nonjol.")

    def medianFilterClicked(self):
        if self.image is not None:
            # 1. Konversi citra ke grayscale sesuai arahan modul
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()

            # 2. Proses Median Filter
            # Angka 3 di bawah adalah ukuran kernel (3x3). 
            # Kalau noise bintiknya gede-gede, bisa lu ganti jadi 5 atau 7.
            print("Lagi ngurutin piksel pakai Median Filter...")
            img_out = cv2.medianBlur(img_gray, 3) 
            
            # 3. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Median Filter Beres! Coba masukin gambar yang ada noise bintik-bintiknya.")

    def maxFilterClicked(self):
        if self.image is not None:
            # 1. Konversi ke grayscale
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()

            # 2. Proses Max Filter (Pakai trik Dilatasi OpenCV dengan kernel 3x3)
            # Ini secara matematis SAMA PERSIS dengan Max Filter, tapi jauh lebih cepet dari pseudo-code!
            print("Lagi nyari piksel paling terang (Max Filter)...")
            kernel = np.ones((3,3), np.uint8)
            img_out = cv2.dilate(img_gray, kernel, iterations=1)
            
            # 3. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Max Filter Beres! Liat tuh, objek yang terang makin menebal.")

    def minFilterClicked(self):
        if self.image is not None:
            # 1. Konversi ke grayscale
            if len(self.image.shape) == 3:
                img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img_gray = self.image.copy()

            # 2. Proses Min Filter (Pakai trik Erosi OpenCV dengan kernel 3x3)
            print("Lagi nyari piksel paling gelap (Min Filter)...")
            kernel = np.ones((3,3), np.uint8)
            img_out = cv2.erode(img_gray, kernel, iterations=1)
            
            # 3. Tampilkan Hasilnya
            self.image = img_out.copy()
            self.displayImage(2)
            print("Min Filter Beres! Sekarang yang gelap-gelap jadi makin dominan.")

    # FUNGSI P4: E1 DFT SMOOTHING (LOW PASS FILTER)
    def dftSmoothingClicked(self):
        if self.image is not None:
            # 1. Pastikan gambar formatnya Grayscale sesuai Modul
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                img = self.image.copy()

            # 2. Proses Discrete Fourier Transform (DFT)
            print("Lagi ngitung spektrum Fourier, bentar bro...")
            dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)
            
            # Hitung Magnitude Spectrum (buat visualisasi)
            magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1e-5)

            # 3. Bikin Masking (Low Pass Filter / LPF)
            rows, cols = img.shape
            crow, ccol = int(rows / 2), int(cols / 2)
            mask = np.zeros((rows, cols, 2), np.uint8)
            
            # r adalah radius area yang mau diloloskan (frekuensi rendah)
            r = 50 
            x, y = np.ogrid[:rows, :cols]
            center = [crow, ccol]
            mask_area = (x - center[0])**2 + (y - center[1])**2 <= r*r
            mask[mask_area] = 1

            # 4. Terapkan Mask ke Gambar & Kembalikan ke Spasial (Inverse Fourier)
            fshift = dft_shift * mask
            fshift_mask_mag = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1e-5)
            
            f_ishift = np.fft.ifftshift(fshift)
            img_back = cv2.idft(f_ishift)
            img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

            # 5. Visualisasi Hasil Analisis pakai Matplotlib
            fig = plt.figure(figsize=(10, 10))
            
            ax1 = fig.add_subplot(2, 2, 1)
            ax1.imshow(img, cmap='gray')
            ax1.title.set_text('Input Image')
            
            ax2 = fig.add_subplot(2, 2, 2)
            ax2.imshow(magnitude_spectrum, cmap='gray')
            ax2.title.set_text('FFT of Image')
            
            ax3 = fig.add_subplot(2, 2, 3)
            ax3.imshow(fshift_mask_mag, cmap='gray')
            ax3.title.set_text('FFT + Mask (LPF)')
            
            ax4 = fig.add_subplot(2, 2, 4)
            ax4.imshow(img_back, cmap='gray')
            ax4.title.set_text('Inverse Fourier (Hasil)')
            
            # Jalan ninja anti force-close: save dulu plotnya, baru buka di OpenCV
            plt.savefig("temp_dft_e1.png")
            plt.close(fig)
            cv2.imshow("Analisis DFT E1 - Smoothing", cv2.imread("temp_dft_e1.png"))

            # 6. Tampilkan Hasil Smoothing ke Label Kanan di UI
            # Normalisasi rentang warna biar gak error saat dijadiin uint8
            cv2.normalize(img_back, img_back, 0, 255, cv2.NORM_MINMAX)
            self.image = np.uint8(img_back)
            self.displayImage(2)
            
            print("Beres! Coba cek gambar hasilnya dan perhatiin efek radius (r) ke hasil blurnya.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())