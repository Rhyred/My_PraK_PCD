import sys
import cv2
import numpy as np
import math
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('A8.ui', self)
        self.Image = None
        self.temp_gray = None
        
        # Koneksi MenuBar
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionGrayscale.triggered.connect(self.grayClicked)
        self.actionOperasi_Kecerahan.triggered.connect(self.brightness)
        self.actionSimple_Contrast.triggered.connect(self.contrast)
        self.actionContrast_Stretching.triggered.connect(self.contrastStretching)   
        
        # Slider
        self.sliderBrightness.valueChanged.connect(self.update_brightness)
        
        # Negative
        self.actionNegative.triggered.connect(self.negativeImage)
        
        # Biner
        self.actionBiner.triggered.connect(self.binerImage)
        
        # Koneksi Button (Agar tombol lama tetap berfungsi)
        self.pushButton.clicked.connect(self.fungsi)
        self.prosesCitra.clicked.connect(self.grayClicked)
        
    def fungsi(self):  
        self.Image = cv2.imread('Foto.jpg')
        self.displayImage()
        
    def open_file(self):
        # Bisa buka via tombol atau menu File -> Open
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', "Image Files (*.jpg *.png)")
        if fname:
            self.Image = cv2.imread(fname)
            self.displayImage(1)

    def save_file(self):
        if self.Image is not None:
            fname, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "JPG (*.jpg);;PNG (*.png)")
            if fname:
                cv2.imwrite(fname, self.Image)
        else:
            QMessageBox.warning(self, "Peringatan", "Tidak ada gambar untuk disimpan.")

    def grayClicked(self):
        if self.Image is None:
            return

        if len(self.Image.shape) < 3:
            return

        H, W = self.Image.shape[:2]
        gray = np.zeros((H, W), np.uint8)   
        for i in range(H):
            for j in range(W):
                b = self.Image[i, j, 0]
                g = self.Image[i, j, 1]
                r = self.Image[i, j, 2]
                gray[i,j] = np.clip(0.299 * r + 0.587 * g + 0.114 * b, 0, 255)
        
        self.Image = gray
        
        # --- Tambahkan perintah print di sini ---
        print("\nMatriks Piksel Citra Keabuan:")
        print(self.Image)
        # ----------------------------------------
        
        self.displayImage(2)
        
    def brightness(self):
        try:
            self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
        except:
            pass
        
        H, W = self.Image.shape[:2]
        cerah = 80 
        for i in range(H):
            for j in range(W):
                a = self.Image.item(i, j)
                b = np.clip(a + cerah, 0, 255)
                
                self.Image[i, j] = b
        
        print(self.Image)         
        self.displayImage(1)
        
    def contrast(self):
        try:
            self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
        except:
            pass
        
        H, W = self.Image.shape[:2]
        kontras = 1.6
        for i in range(H):
            for j in range(W):
                a = self.Image.item(i, j)
                b = math.ceil(a * kontras)
                
                self.Image[i, j] = np.clip(b, 0, 255)
        
        print(self.Image)         
        self.displayImage(1)
        
    def contrastStretching(self):
        try:
            self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
        except:
            pass
        
        H, W = self.Image.shape[:2]
        minV = np.min (self.Image)
        maxV = np.max (self.Image)
        for i in range(H):
            for j in range(W):
                a = self.Image.item(i, j)
                b = float(a - minV ) / (maxV - minV) * 255
                
                self.Image[i, j] = np.clip(b, 0, 255)
        
        print(self.Image)         
        self.displayImage(1)
        
        
    # Perbaikan logika: Gunakan temp_gray agar tidak akumulasi
    def update_brightness(self):
        if self.temp_gray is None:
            if self.Image is not None:
                # Jika user belum klik grayscale, paksa buat temp dari gambar saat ini
                if len(self.Image.shape) == 3:
                    self.temp_gray = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
                else:
                    self.temp_gray = self.Image.copy()
            else:
                return

        nilai_slider = self.sliderBrightness.value()
        
        # Hitung dari temp_gray (gambar dasar), simpan hasilnya ke self.Image
        # Clip harus 255 untuk standar warna putih
        self.Image = np.clip(self.temp_gray.astype(np.int16) + nilai_slider, 0, 255).astype(np.uint8)
        
        self.displayImage(2)
        print(f"Nilai Kecerahan: {nilai_slider}")
        
    def negativeImage(self):
        if self.Image is None:
            return

        # Pastikan gambar dikonversi ke grayscale terlebih dahulu
        if len(self.Image.shape) == 3:
            self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
        
        H, W = self.Image.shape[:2]
        max_intensity = 255
        
        for i in range(H):
            for j in range(W):
                # Ambil nilai piksel input f(x, y)
                a = self.Image.item(i, j)
                
                # Terapkan Persamaan (7): f(x, y)' = 255 - f(x, y)
                b = max_intensity - a
                
                # Update nilai piksel
                self.Image[i, j] = np.clip(b, 0, 255)
        
        # Cetak matriks ke terminal
        print("\nMatriks Piksel Citra Negatif:")
        print(self.Image)
        
        # Tampilkan di label hasil (label_2)
        self.displayImage(2)
        
    def binerImage(self):
        if self.Image is None:
            return

        # Pastikan gambar dikonversi ke grayscale terlebih dahulu
        if len(self.Image.shape) == 3:
            self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)
        
        H, W = self.Image.shape[:2]
        
        # 1. Tentukan nilai ambang (Threshold)
        # Jika piksel > threshold jadi putih (255), jika kurang jadi hitam (0)
        threshold = 256
        
        for i in range(H):
            for j in range(W):
                # 2. Baca nilai array piksel f(x, y)
                a = self.Image.item(i, j)
                
                # 3. Terapkan Logika Biner
                if a >= threshold:
                    b = 255
                else:
                    b = 0
                
                # Masukkan kembali ke matriks
                self.Image[i, j] = b
        
        # 4. Display Image
        print("\nMatriks Piksel Citra Biner:")
        print(self.Image)
        self.displayImage(2)
    
        

    def displayImage(self, windows=1):
        if self.Image is None: return
        
        if len(self.Image.shape) == 3:
            h, w, ch = self.Image.shape
            bytes_per_line = ch * w
            qformat = QImage.Format_RGB888
            img_show = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB)
        else:
            h, w = self.Image.shape
            bytes_per_line = w
            qformat = QImage.Format_Indexed8
            img_show = self.Image

        img = QImage(img_show.data, w, h, bytes_per_line, qformat)
        pixmap = QPixmap.fromImage(img)
        
        if windows == 1:
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
        if windows == 2:
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
                    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())