import sys
import cv2
import os
import numpy as np
import math 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        # Ubah target pencarian file menjadi A5.ui
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'A5.ui')
        loadUi(ui_path, self) 
        
        self.image = None
        
        # --- KONEKSI TOMBOL GEDE DI LAYAR ---
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        
        # --- KONEKSIKAN MENU BAR KE FUNGSI ---
        self.actionLoad_Image.triggered.connect(self.loadClicked)
        self.actionGrayScale.triggered.connect(self.grayClicked)
        
        # Kabel Brightness sudah DIBUANG. 
        # Cukup koneksikan menu Simple Contrast saja
        self.actionSimple_Contrast.triggered.connect(self.contrast)

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

    def grayClicked(self):
        if self.image is not None:
            H, W = self.image.shape[:2]
            gray = np.zeros((H, W), np.uint8)
            for i in range(H):
                for j in range(W):
                    gray[i, j] = np.clip(0.299 * self.image[i, j, 2] + 
                                         0.587 * self.image[i, j, 1] + 
                                         0.114 * self.image[i, j, 0], 0, 255)
            self.image = gray
            self.displayImage(2)

    # --- PRAKTEK A5: SIMPLE CONTRAST ---
    def contrast(self):
        if self.image is not None:
            # Konversi citra RGB ke grayscale sesuai instruksi
            img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            
            # Tentukan konstanta nilai kontras
            contrast_val = 1.6 
            h, w = img.shape[:2]
            
            # Looping untuk masing-masing array piksel
            for i in range(h):
                for j in range(w):
                    # Ambil nilai piksel (dijadikan int agar aman saat dikali)
                    a = int(img[i, j]) 
                    
                    # Rumus Kontras: f(x,y)' = f(x,y) * c
                    # Menggunakan math.ceil untuk membulatkan ke atas
                    b = math.ceil(a * contrast_val) 
                    
                    # Terapkan proses clipping
                    if b > 255: 
                        b = 255
                    elif b < 0: 
                        b = 0
                        
                    # Kembalikan nilai piksel yang baru
                    img[i, j] = b 
                    
            self.image = img
            self.displayImage(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())