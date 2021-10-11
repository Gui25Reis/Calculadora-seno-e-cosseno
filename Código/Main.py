# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:

from PyQt5.QtWidgets import QApplication
from Client.Client import Client                # Arquivo local
import sys


def main() -> None:
    app = QApplication(sys.argv)
    win = Client()

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()