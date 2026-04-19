import sys
import cv2
import os
import numpy as np # Library wajib untuk array di A3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        # Load Path Auto
        # Ini akan otomatis mencari A3.ui di folder yang sama dengan A3.py
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'A3.ui')
        loadUi(ui_path, self) 
        
        self.image = None
        
        # --- KONEKSI TOMBOL GEDE DI LAYAR ---
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        
        # --- KONEKSIKAN MENU BAR KE FUNGSI ---
        # Asumsinya objectName di Qt Designer adalah actionLoad_Image & actionGrayScale
        self.actionLoad_Image.triggered.connect(self.loadClicked)
        self.actionGrayScale.triggered.connect(self.grayClicked)

    def loadClicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if fileName:
            self.image = cv2.imread(fileName)
            self.displayImage(1) # Tampilkan ke Label 1 (imgLabel)

    def saveClicked(self):
        # Cek dulu apakah ada gambar yang lagi dibuka/diproses
        if self.image is not None:
            options = QFileDialog.Options()
            # Buka jendela dialog untuk save file
            fileName, _ = QFileDialog.getSaveFileName(self, "Simpan Gambar Hasil", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
            
            if fileName:
                # Simpan array numpy self.image menjadi file gambar beneran
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
        
        # Pengaturan untuk Label 1 (Gambar Asli)
        if windows == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.imgLabel.setScaledContents(True)
            
        # Pengaturan untuk Label 2 (Gambar Hasil/Grayscale)
        elif windows == 2:
            self.hasilLabel.setPixmap(QPixmap.fromImage(img))
            self.hasilLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.hasilLabel.setScaledContents(True)

    def grayClicked(self):
        # Mengecek apakah gambar sudah di-load
        if self.image is not None:
            H, W = self.image.shape[:2]
            gray = np.zeros((H, W), np.uint8)
            
            # Looping manual untuk konversi ke Grayscale sesuai modul A3
            for i in range(H):
                for j in range(W):
                    # Rumus Grayscale: 0.299*R + 0.587*G + 0.114*B
                    # OpenCV pakai BGR (B=0, G=1, R=2)
                    gray[i, j] = np.clip(0.299 * self.image[i, j, 2] + 
                                         0.587 * self.image[i, j, 1] + 
                                         0.114 * self.image[i, j, 0], 0, 255)
            
            self.image = gray
            self.displayImage(2) # Tampilkan hasilnya di Label 2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())