from PySide2.QtWidgets import *

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()

        bouton1 = QPushButton("Configure")
        bouton2 = QPushButton("Connect")
        bouton3 = QPushButton("Disconnect")

        layout.addWidget(bouton1)
        layout.addWidget(bouton2)
        layout.addWidget(bouton3)

        self.setLayout(layout)

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600, 400)
        layout = QVBoxLayout()

        boutonpanel = ButtonsPanel()
        notification = QTextEdit()

        results = QTableWidget(5, 3)
        results.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(boutonpanel)
        layout.addWidget(notification)
        layout.addWidget(results)

        self.setLayout(layout)

