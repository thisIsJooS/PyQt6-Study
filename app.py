import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QFont


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 툴팁
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is <b>QWidhet</b> widget')
        
        # 버튼
        btn = QPushButton('Quit', self) # (버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 상태바
        self.statusBar().showMessage('Ready')
        
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('web.png'))    # 타이틀바의 아이콘
        self.setGeometry(300, 300, 300, 200)    # move()와 resize()를 하나로 합친 메서드
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())