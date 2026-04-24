# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'A10.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 1021)
        self.actionGrayScale = QAction(MainWindow)
        self.actionGrayScale.setObjectName(u"actionGrayScale")
        self.actionLoad_Image = QAction(MainWindow)
        self.actionLoad_Image.setObjectName(u"actionLoad_Image")
        self.actionSave_Image = QAction(MainWindow)
        self.actionSave_Image.setObjectName(u"actionSave_Image")
        self.actionBrightness = QAction(MainWindow)
        self.actionBrightness.setObjectName(u"actionBrightness")
        self.actionSimple_Contrast = QAction(MainWindow)
        self.actionSimple_Contrast.setObjectName(u"actionSimple_Contrast")
        self.actionContrast_Stretching = QAction(MainWindow)
        self.actionContrast_Stretching.setObjectName(u"actionContrast_Stretching")
        self.actionNegative_Image = QAction(MainWindow)
        self.actionNegative_Image.setObjectName(u"actionNegative_Image")
        self.actionBiner_Image = QAction(MainWindow)
        self.actionBiner_Image.setObjectName(u"actionBiner_Image")
        self.actionGray_Histogram = QAction(MainWindow)
        self.actionGray_Histogram.setObjectName(u"actionGray_Histogram")
        self.actionRGB_Histogram = QAction(MainWindow)
        self.actionRGB_Histogram.setObjectName(u"actionRGB_Histogram")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(240, 480, 75, 23))
        self.imgLabel = QLabel(self.centralwidget)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(60, 50, 450, 420))
        self.imgLabel.setFrameShape(QFrame.Box)
        self.hasilLabel = QLabel(self.centralwidget)
        self.hasilLabel.setObjectName(u"hasilLabel")
        self.hasilLabel.setGeometry(QRect(610, 50, 450, 420))
        self.hasilLabel.setFrameShape(QFrame.Box)
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(800, 480, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOperasi_Titik = QMenu(self.menubar)
        self.menuOperasi_Titik.setObjectName(u"menuOperasi_Titik")
        self.menuHistogram = QMenu(self.menubar)
        self.menuHistogram.setObjectName(u"menuHistogram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOperasi_Titik.menuAction())
        self.menubar.addAction(self.menuHistogram.menuAction())
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuOperasi_Titik.addAction(self.actionGrayScale)
        self.menuOperasi_Titik.addAction(self.actionBrightness)
        self.menuOperasi_Titik.addAction(self.actionSimple_Contrast)
        self.menuOperasi_Titik.addAction(self.actionContrast_Stretching)
        self.menuOperasi_Titik.addAction(self.actionNegative_Image)
        self.menuOperasi_Titik.addAction(self.actionBiner_Image)
        self.menuHistogram.addAction(self.actionGray_Histogram)
        self.menuHistogram.addAction(self.actionRGB_Histogram)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGrayScale.setText(QCoreApplication.translate("MainWindow", u"GrayScale", None))
        self.actionLoad_Image.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.actionSave_Image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.actionBrightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.actionSimple_Contrast.setText(QCoreApplication.translate("MainWindow", u"Simple Contrast", None))
        self.actionContrast_Stretching.setText(QCoreApplication.translate("MainWindow", u"Contrast Stretching", None))
        self.actionNegative_Image.setText(QCoreApplication.translate("MainWindow", u"Negative Image", None))
        self.actionBiner_Image.setText(QCoreApplication.translate("MainWindow", u"Biner Image", None))
        self.actionGray_Histogram.setText(QCoreApplication.translate("MainWindow", u"Histogram Grayscale", None))
        self.actionRGB_Histogram.setText(QCoreApplication.translate("MainWindow", u"Histogram RGB", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.imgLabel.setText("")
        self.hasilLabel.setText("")
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOperasi_Titik.setTitle(QCoreApplication.translate("MainWindow", u"Operasi Titik", None))
        self.menuHistogram.setTitle(QCoreApplication.translate("MainWindow", u"Histogram", None))
    # retranslateUi

