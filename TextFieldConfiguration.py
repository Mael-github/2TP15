from PySide2.QtWidgets import *

class LabeledTextField(QWidget):
    def __init__(self, texte):
        QWidget.__init__(self)
        self.texte = texte

        layout = QHBoxLayout()

        label = QLabel(texte)
        texte1 = QTextEdit()
        texte1.setMaximumHeight(20)

        layout.addWidget(label)
        layout.addWidget(texte1)

        self.setLayout(layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")
        self.setMinimumSize(300, 100)

        layout = QVBoxLayout()

        label1 = LabeledTextField("Address IP")
        label2 = LabeledTextField("Username")
        label3 = LabeledTextField("Password")

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)

