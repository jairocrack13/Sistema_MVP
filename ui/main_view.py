from PySide6.QtCore import Qt, Signal as pyqtSignal
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self._label = QLabel("BIENVENIDO - PANEL DE ADMINISTRADOR", alignment=Qt.AlignCenter)
        self._label.setStyleSheet("font-size: 20px; color: blue;")
        layout.addWidget(self._label)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, {user}.\nSesión de Administrador.")
