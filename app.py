import sys
from PySide6.QtWidgets import QApplication
from core.app_shell import AppShell

def main():
    app = QApplication(sys.argv)
    shell = AppShell()
    shell.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
