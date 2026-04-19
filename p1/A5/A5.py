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
        
        # Nyalakan dua-duanya di A5
        self.actionBrightness.triggered.connect(self.brightness)
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

    # ========================================================
    # KUMPULAN FUNGSI OPERASI TITIK (A3 - A5 KUMULATIF)
    # ========================================================

    def grayClicked(self):
        if self.image is not None:
            # Satpam Pengecekan Warna
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
            # Satpam Pengecekan Warna
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
            # Satpam Pengecekan Warna
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())