
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):                                 # constructor 
        super().__init__()                              # call super constructor
        self.setWindowTitle("Hello")                    # set window title
        self.UI()                                       # call UI function

    def UI(self):
        mainLayout = QVBoxLayout()                      # create main layout
        self.tabs = QTabWidget()                        # create tab widget
        self.tab1 = QWidget()                           # create tab 1
        self.tabs.addTab(self.tab1, "Hello World!")     # add tab 1
        self.setText("Hello World!")
        mainLayout.addWidget(self.tabs)                 # add tab widget to main layout
        self.setLayout(mainLayout)                      # set main layout to window
        self.show()                                     # show window

def main():
    App = QApplication(sys.argv)                        # create application
    window = Window()                                   # create window
    sys.exit(App.exec_())                               # execute application


if __name__ == "__main__":                              # if main
    main()
