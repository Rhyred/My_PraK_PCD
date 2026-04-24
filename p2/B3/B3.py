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

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'B3.ui')
        loadUi(ui_path, self) 
        
        self.image = None
        
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

    # FUNGSI B3
    def resizeImage(self):
        if self.image is not None:
            # Mengubah ukuran gambar jadi 50% dari aslinya
            # fx = skala sumbu x, fy = skala sumbu y
            resized_img = cv2.resize(self.image, (0, 0), fx=0.5, fy=0.5)
            self.image = resized_img.copy()
            self.displayImage(2)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())