from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QIcon

app = QApplication([])
mw = QWidget()
mw.resize(300,300)
mw.setWindowTitle('Kalkulator')
mw.setWindowIcon(QIcon('calculator.png'))
font = QFont()
font.setPointSize(20)

layar = QLineEdit()
layar.setFixedHeight(100)
layar.setFont(font)

button  =   QPushButton('0')
button1 =   QPushButton('1')
button2 =   QPushButton('2')
button3 =   QPushButton('3')
button4 =   QPushButton('4')
button5 =   QPushButton('5')
button6 =   QPushButton('6')
button7 =   QPushButton('7')
button8 =   QPushButton('8')
button9 =   QPushButton('9')
buttonadd = QPushButton('+')
buttonmin = QPushButton('-')
buttontimes = QPushButton('x')
buttondivide = QPushButton('/')
buttonhasil = QPushButton('=')
buttonhasil.setStyleSheet('background-color:orange;color:white')
buttondel = QPushButton('c')
buttondelself = QPushButton('<--')
buttonpangkat = QPushButton('x^2')
buttonakar = QPushButton('√X')
buttonkoma = QPushButton('.')

button.setFixedSize(70,50)
button1.setFixedSize(70,50)
button2.setFixedSize(70,50)
button3.setFixedSize(70,50)
button4.setFixedSize(70,50)
button5.setFixedSize(70,50)
button6.setFixedSize(70,50)
button7.setFixedSize(70,50)
button8.setFixedSize(70,50)
button9.setFixedSize(70,50)
buttonadd.setFixedSize(70,50)
buttonmin.setFixedSize(70,50)
buttontimes.setFixedSize(70,50)
buttondivide.setFixedSize(70,50)
buttonhasil.setFixedSize(70,50)
buttondel.setFixedSize(70,30)
buttondelself.setFixedSize(70,50)
buttonkoma.setFixedSize(70,50)
buttonpangkat.setFixedSize(70,30)
buttonakar.setFixedSize(70,30)

layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutV4 = QVBoxLayout()
mainlayout = QHBoxLayout()
layoutlayar1 = QVBoxLayout()

layoutV1.addWidget(buttondel)
layoutV1.addWidget(button7)
layoutV1.addWidget(button4)
layoutV1.addWidget(button1)
layoutV1.addWidget(buttonkoma)


layoutV2.addWidget(buttonpangkat)
layoutV2.addWidget(button8)
layoutV2.addWidget(button5)
layoutV2.addWidget(button2)
layoutV2.addWidget(button)

layoutV3.addWidget(buttonakar)
layoutV3.addWidget(button9)
layoutV3.addWidget(button6)
layoutV3.addWidget(button3)
layoutV3.addWidget(buttonhasil)

layoutV4.addWidget(buttondelself)
layoutV4.addWidget(buttontimes)
layoutV4.addWidget(buttondivide)
layoutV4.addWidget(buttonadd)
layoutV4.addWidget(buttonmin)

mainlayout.addLayout(layoutV1)
mainlayout.addLayout(layoutV2)
mainlayout.addLayout(layoutV3)
mainlayout.addLayout(layoutV4)

layoutlayar1.addWidget(layar, alignment=Qt.AlignTop)
layoutlayar1.addLayout(mainlayout)
mw.setLayout(layoutlayar1)

def tombol(value):
    old = layar.text()
    layar.setText(str(old)+str(value))
def equal():
    try:
        lama = layar.text()
        if 'x' in lama:
            lama = lama.replace('x', '*')
        if ':' in lama:
            lama = lama.replace(':', '/')
        hasil = eval(lama)
        if hasil%1 == 0:
            hasil = int(hasil)
        layar.setText(str(hasil))
    except:
        layar.setText('Error')
def hapus():
    layar.clear()
def hapuself():
    total = len(layar.text())
    hasil = layar.text()
    akhir = hasil[0:total-1]
    layar.setText(akhir)
def pangkat(value):
    try:
        lama = layar.text()
        hasil = float(lama)**value
        if hasil%1 == 0:
            hasil = int(hasil)
        layar.setText(str(hasil))
    except:
        layar.setText('Error')
def operasi(value):
    old = layar.text()
    layar.setText(str(old)+ ' ' + str(value) + ' ')

button.clicked.connect(lambda:tombol(0))
button1.clicked.connect(lambda:tombol(1))
button2.clicked.connect(lambda:tombol(2))
button3.clicked.connect(lambda:tombol(3))
button4.clicked.connect(lambda:tombol(4))
button5.clicked.connect(lambda:tombol(5))
button6.clicked.connect(lambda:tombol(6))
button7.clicked.connect(lambda:tombol(7))
button8.clicked.connect(lambda:tombol(8))
button9.clicked.connect(lambda:tombol(9))
buttonadd.clicked.connect(lambda:operasi('+'))
buttonmin.clicked.connect(lambda:operasi('-'))
buttontimes.clicked.connect(lambda:operasi('x'))
buttondivide.clicked.connect(lambda:operasi(':'))
buttonhasil.clicked.connect(lambda:equal())
buttondel.clicked.connect(lambda:hapus())
buttondelself.clicked.connect(lambda:hapuself())
buttonpangkat.clicked.connect(lambda:pangkat(2))
buttonkoma.clicked.connect(lambda:tombol('.'))
buttonakar.clicked.connect(lambda:pangkat(0.5))


mw.show()
app.exec_()