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
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'A7.ui')
        loadUi(ui_path, self) 
        
        self.image = None
        
        # --- KONEKSI TOMBOL GEDE DI LAYAR ---
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        
        # --- KONEKSIKAN MENU BAR KE FUNGSI ---
        self.actionLoad_Image.triggered.connect(self.loadClicked)
        self.actionGrayScale.triggered.connect(self.grayClicked)
        self.actionBrightness.triggered.connect(self.brightness)
        self.actionSimple_Contrast.triggered.connect(self.contrast)
        self.actionContrast_Stretching.triggered.connect(self.contrastStretching)
        
        # Kabel Baru untuk A7
        self.actionNegative_Image.triggered.connect(self.negativeImage)

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

    # FUNGSI OPERASI TITIK (KUMULATIF A3 - A7)

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

    # --- NEGATIVE IMAGE ---
    def negativeImage(self):
        if self.image is not None:
            # Satpam Pengecekan Warna
            if len(self.image.shape) == 3:
                img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
            else:
                img = self.image.copy()
            
            h, w = img.shape[:2]
            
            for i in range(h):
                for j in range(w):
                    a = int(img[i, j])
                    
                    # Rumus Negative: 255 - Nilai Piksel Asli
                    b = 255 - a
                    
                    img[i, j] = b
                    
            self.image = img
            self.displayImage(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())