import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt6.QtWidgets import QLabel, QGridLayout, QLabel, QHBoxLayout, QFrame, QSplitter

from PyQt6.QtGui import QIcon, QAction, QFont, QGuiApplication
from PyQt6.QtCore import QCoreApplication, QDateTime, Qt, QBasicTimer

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('web.png'))    # 타이틀바의 아이콘
        self.resize(800, 600)
        self.center() # 창이 화면의 가운데에 위치하게 함
        self.initUI()

    def initUI(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)
        
        # 툴팁
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is <b>QWidget</b> widget')
        
        # 버튼
        # btn = QPushButton('Quit', self) # (버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯)
        # btn.move(300, 300)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 상태바
        self.statusBar().showMessage(QDateTime.currentDateTime().toString())
        
        # 메뉴바 - 어플리케이션에서 사용되는 모든 명령의 모음
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        editAction = QAction(QIcon('edit.png'), 'Edit', self)
        printAction = QAction(QIcon('print.png'), 'Print', self)
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.quit)
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu.addAction(saveAction)
        editmenu = menubar.addMenu('&Edit')
        editmenu.addAction(editAction)
        editmenu.addAction(printAction)

        # 툴바 - 자주 사용하는 명령들을 툴바에 표기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(exitAction)
        
        # QProgressBar
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Shape.Box)
        
        midleft = QFrame()
        midleft.setFrameShape(QFrame.Shape.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Shape.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.Shape.WinPanel)
        bottom.setFrameShadow(QFrame.Shadow.Sunken)

        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        widget.setLayout(hbox)
        
        
        # Main
        self.show()

    def center(self):
        qr = self.frameGeometry()   # 스크린의 위치와 크기 정보를 가져옴
        cp = QGuiApplication.primaryScreen().availableGeometry().center() # 스크린의 가운데 위치 파악
        qr.moveCenter(cp)   # 창의 직사각형 위치를 화면의 중심의 위치로 이동
        self.move(qr.topLeft()) # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킴.

    
    def item_selected(self):
        item = self.combo.currentText()
        self.lbl.setText(f"You have selected : {item}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())