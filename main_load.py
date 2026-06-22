import sys
from PyQt5.QtWidgets import QApplication
from load.load_menu import LoadMenu

def main():
    app = QApplication(sys.argv)
    window = LoadMenu()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    