from pathlib import Path

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget


class LoadGraphPySide6(QWidget):
    def __init__(self):
        super().__init__()
        base_dir = Path(__file__).resolve().parents[1]
        ui_path = base_dir / 'ui' / 'Graph.ui'

        ui_file = QFile(str(ui_path))
        if not ui_file.open(QIODevice.ReadOnly):
            raise FileNotFoundError(f'No se pudo abrir la interfaz: {ui_path}')

        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
