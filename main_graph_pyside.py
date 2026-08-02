import sys
from PySide6.QtWidgets import QApplication
from load.load_graph_pyside import LoadGraphPySide6


def main():
    app = QApplication(sys.argv)
    window = LoadGraphPySide6()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
