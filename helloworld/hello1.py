""" ------------------------------------------------------------------------------
@ author: Tec Santosh Kumar
@ date: 2020-04-01
@ description: This is the first project in python
-------------------------------------------------------------------------------"""


"""-------------------------------------------------------------------------------
   Creating a simple GUI application using PyQt involves the following steps −
   1. Create a QApplication object.
   2. Create a QWidget object.
   3. Create a QLabel object.
   4. Create a QPushButton object.
   5. Create a QVBoxLayout object.
   6. Add the QLabel and QPushButton objects to the QVBoxLayout object.
   7. Set the layout for the QWidget.
   8. Show the QWidget.
   9. Execute the application.
------------------------------------------------------------------------------"""

import sys
from PyQt5.QtWidgets import *

"""-------------------------------------------------------------------------------
@ definition: Window()
-------------------------------------------------------------------------------"""

def window():
   app = QApplication(sys.argv)       # create application
   w = QWidget()                      # create window
   b = QLabel(w)                      # create label
   b.setText("Hello World!")          # set text
   w.setGeometry(100,100,200,50)      # set geometry
   b.move(50,20)                      # move label
   w.setWindowTitle('Hello World')    # set title
   w.show()                           # show window
   sys.exit(app.exec_())              # execute application
   
if __name__ == '__main__':            # if main
   window()                           # call window function

