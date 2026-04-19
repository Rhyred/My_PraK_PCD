import sys
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi # Ini library untuk manggil file .ui 

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__() 
        # PANGGIL FILE UI DI SINI
        loadUi('A2.ui', self) # Pastikan nama file sesuai 
        
        self.image = None 
        
        # Hubungkan tombol 'loadButton'
        self.loadButton.clicked.connect(self.loadClicked) 

    def loadClicked(self): 
        # Buka dialog untuk pilih file gambar
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        
        if fileName:
            self.image = cv2.imread(fileName) 
            self.displayImage() 

    def displayImage(self): 
        qformat = QImage.Format_Indexed8 
        
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4: 
                qformat = QImage.Format_RGBA8888 
            else:
                qformat = QImage.Format_RGB888 
                
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat) # 
        img = img.rgbSwapped() # cv membaca BGR, PyQt membaca RGB [cite: 189, 191]
        
        # Tampilkan ke imgLabel 
        self.imgLabel.setPixmap(QPixmap.fromImage(img)) # 
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # 
        self.imgLabel.setScaledContents(True) # Biar gambar fit di dalam kotak 

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = ShowImage() 
    window.show() 
    sys.exit(app.exec_()) 