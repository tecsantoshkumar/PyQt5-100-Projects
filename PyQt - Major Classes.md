﻿
PyQt - Major Classes

**PyQt API** is a large collection of classes and methods. These classes are defined in more than 20 modules. Following are some of the frequently used modules −



|**Sr.No.**|**Modules & Description**|
| - | - |
|1|<p>**QtCore**</p><p>Core non-GUI classes used by other modules</p>|
|2|<p>**QtGui**</p><p>Graphical user interface components</p>|
|3|<p>**QtMultimedia**</p><p>Classes for low-level multimedia programming</p>|
|4|<p>**QtNetwork**</p><p>Classes for network programming</p>|
|5|<p>**QtOpenGL**</p><p>OpenGL support classes</p>|
|6|<p>**QtScript**</p><p>Classes for evaluating Qt Scripts</p>|
|7|<p>**QtSql**</p><p>Classes for database integration using SQL</p>|
|8|<p>**QtSvg**</p><p>Classes for displaying the contents of SVG files</p>|
|9|<p>**QtWebKit**</p><p>Classes for rendering and editing HTML</p>|
|10|<p>**QtXml**</p><p>Classes for handling XML</p>|
|<p>11</p><p>s://www.tutori</p>|<p>**QtAssistant**</p><p>alspoint.com/pyqt/pyqt\_major\_classes.htm</p>|

|||
| :- | :- |
|2/22, 11:33 PM|<p>PyQt - Major Classes</p><p>Support for online help</p>|
|12|<p>**QtDesigner**</p><p>Classes for extending Qt Designer</p>|
7/2

PyQt API contains more than 400 classes. The **QObject** class is at the top of class hierarchy. It is the base class of all Qt objects. Additionally, **QPaintDevice** class is the base class for all objects that can be painted.

**QApplication** class manages the main settings and control flow of a GUI application. It contains main event loop inside which events generated by window elements and other sources are processed and dispatched. It also handles system-wide and application-wide settings.

**QWidget** class, derived from QObject and QPaintDevice classes is the base class for all user interface objects. **QDialog** and **QFrame** classes are also derived from QWidget class. They have their own sub-class system.

Following diagrams depict some important classes in their hierarchy.

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.001.png)

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.002.png)

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.003.png)

https://www.tutorialspoint.com/pyqt/pyqt\_major\_classes.htm 4/9
7/22/22, 11:33 PM PyQt - Major Classes

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.004.png)

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.005.png)

Here is a select list of frequently used widgets − Given below are the commonly used Widgets.

https://www.tutorialspoint.com/pyqt/pyqt\_major\_classes.htm 5/9
7/22/22, 11:33 PM PyQt - Major Classes
|**Sr.No.**|**Widgets & Description**|
| - | - |
|1|<p>**QLabel**</p><p>Used to display text or image</p>|
|2|<p>**QLineEdit**</p><p>Allows the user to enter one line of text</p>|
|3|<p>**QTextEdit**</p><p>Allows the user to enter multi-line text</p>|
|4|<p>**QPushButton**</p><p>A command button to invoke action</p>|
|5|<p>**QRadioButton**</p><p>Enables to choose one from multiple options</p>|
|6|<p>**QCheckBox**</p><p>Enables choice of more than one options</p>|
|7|<p>**QSpinBox**</p><p>Enables to increase/decrease an integer value</p>|
|8|<p>**QScrollBar**</p><p>Enables to access contents of a widget beyond display aperture</p>|
|9|<p>**QSlider**</p><p>Enables to change the bound value linearly.</p>|
|10|<p>**QComboBox**</p><p>Provides a dropdown list of items to select from</p>|
|<p>11</p><p>s://www.tutori</p>|<p>**QMenuBar**</p><p>alspoint.com/pyqt/pyqt\_major\_classes.htm</p>|

http

7/9

|||
| :- | :- |
|2/22, 11:33 P|<p>M PyQt - Major Classes</p><p>Horizontal bar holding QMenu objects</p>|
|12|<p>**QStatusBar**</p><p>Usually at bottom of QMainWindow, provides status information.</p>|
|13|<p>**QToolBar**</p><p>Usually at top of QMainWindow or floating. Contains action buttons</p>|
|14|<p>**QListView**</p><p>Provides a selectable list of items in ListMode or IconMode</p>|
|15|<p>**QPixmap**</p><p>Off-screen image representation for display on QLabel or QPushButton object</p>|
|16|<p>**QDialog**</p><p>Modal or modeless window which can return information to parent window</p>|
7/2

A typical GUI based application’s top level window is created by **QMainWindow** widget object. Some widgets as listed above take their appointed place in this main window, while others are placed in the central widget area using various layout managers.

The following diagram shows the QMainWindow framework −

![](Aspose.Words.2edb2115-d33f-4424-9dec-7ef562ee81a0.006.png)
https://www.tutorialspoint.com/pyqt/pyqt\_major\_classes.htm 9/9