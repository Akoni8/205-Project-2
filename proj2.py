import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Start(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.UI()
        
    def UI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("1.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        
        #sets height weight and placement of window
        #self.setGeometry(50, 50, 600, 350)
        #sets window title
        self.setWindowTitle('Testing')
        #shows window
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Start()
    sys.exit(app.exec_())


