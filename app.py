import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

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
        
        # QPixmap
        pixmap = QPixmap('Roger_Federer.jpg')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel(f'Width: {str(pixmap.width())}, Height: {str(pixmap.height())}')
        lbl_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        widget.setLayout(vbox)
        
        # Main
        self.show()


    def center(self):
        qr = self.frameGeometry()   # 스크린의 위치와 크기 정보를 가져옴
        cp = QGuiApplication.primaryScreen().availableGeometry().center() # 스크린의 가운데 위치 파악
        qr.moveCenter(cp)   # 창의 직사각형 위치를 화면의 중심의 위치로 이동
        self.move(qr.topLeft()) # 현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킴.

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())