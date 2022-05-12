import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt6.QtGui import QIcon, QAction, QFont, QGuiApplication
from PyQt6.QtCore import QCoreApplication

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
        btn.move(300, 300)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 상태바
        self.statusBar().showMessage('Ready')
        
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
        
        # Main
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('web.png'))    # 타이틀바의 아이콘
        self.resize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())