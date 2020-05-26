from ClientPannel import *
from TextFieldConfiguration import *

if __name__ == "__main__":
    application = QApplication([])
    window1 = SQLClientWindow()
    window2 = ConfigurationDialog()
    window1.show()
    window2.show()
    application.exec_()




