# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


## Bibliotecas necessárias:
# Arquivo local:
from Client.Client import Client

# Arquivo de sistema:
import sys

# Arquivo da biblioteca de interface gráfica:
from PyQt5.QtWidgets import QApplication

## Função main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Client()

    win.show()
    sys.exit(app.exec_())


# self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint )

# pyinstaller.exe --onefile --windowed --noconsole --name='MC - Análise' --icon=images/logo-icone.ico main.py --version-file _versao.txt