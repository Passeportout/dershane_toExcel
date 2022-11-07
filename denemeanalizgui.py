import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QFont
import pandas as pd
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Deneme Analiz") 
        self.label = QLabel(self)
        self.label.setText("ÖğrenciNo dan Sıralamaya Kadar")
        self.label.setFont(QFont('Arial', 10))
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Veri')
        self.line = QLineEdit(self)
        self.label.move(0,110)
        self.label.resize(200,20)
        self.line.move(80, 40)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 40)

        pybutton = QPushButton('Çalıştır', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 80)        

    def clickMethod(self):
        string = self.line.text() 
        header = """Öğrenci_No
        Kit_Tur Ad Soyad SINIF
        """
        header = header.split()
        dersler = "Türkçe Tarih Coğrafya Felsefe Din K. Matematik Geometri Fizik Kimya Biyoloji Toplam"

        for ders in dersler.split():
            if ders == "K.":
                pass
            else:
                for i in ["D" ,"Y","N"]:
                    header.append(ders + i)
        header.append("TYT_PUAN")
        header.append("Sıralama")

        data = {}
        for i,j in zip(string.split(), header):
            data[j] = i
        df = pd.DataFrame(data=data, index=(range(len(data))))
        df1 = df.iloc[[0]]
        df1.to_excel("deneme_analiz.xlsx", index=False)
        print(df1)
        #df.set_axis(header, axis=1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )