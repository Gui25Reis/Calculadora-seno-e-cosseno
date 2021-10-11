# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:

# Arquivo local:
from Client.AuxWidgets import AuxWidgets

# GUI:
from PyQt5.QtWidgets import QMainWindow, QWidget, QRadioButton, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

from requests import get


URL = "http://192.168.15.73:5000/"


class Client(QMainWindow, AuxWidgets):
    r"""
    Classe para criação da interface gráfica.

    Overview
    --------
    Nessa classe é criado os componentes da interface gráfica e também
    a execução da lógica onde pega os dados que vão ser recebidos da api
    SeriesServer.

    Métodos
    -------
    ``gui_Ui() -> None`` - Cria os componentes da interface.

    ``setTxt(t_:str) -> None`` - Define o texto mostrado na text view.
    
    ``btAction() -> None`` - Ação do botão calcular.
    """  
    def __init__(self) -> None:
        super(Client, self).__init__()

        self.setWindowTitle("Prova P1 - Parte 01")                                                                      # Define o título da janela
        self.setStyleSheet("QMainWindow{background: rgb(235, 230, 215);}")                                              # Define a cor de fundo
        
        self.setFixedSize(235, 315)

        self.root = QWidget()
        self.setCentralWidget(self.root)                                                                                     # Define como área central

        ## Objetos instaciados da GUI    
        self.gui_Ui()

        self.erro = True

        
    def gui_Ui(self) -> None:
        r"""Cria os componentes da interface."""
        self.lbl("Ângulo: ", 12, 20, 20, 60, 20, self.root)
        self.angInput = self.lineEdit(10, 95, 20, 120, 20, self.root)

        self.senOpt = QRadioButton("Seno", self.root)
        self.senOpt.setGeometry(QtCore.QRect(20, 60, 75, 18))
        self.senOpt.setFont(QFont('Arial', 12, 50))
        self.senOpt.setChecked(True)
        
        self.cosOpt = QRadioButton("Cosseno", self.root)
        self.cosOpt.setGeometry(QtCore.QRect(125, 60, 90, 18))
        self.cosOpt.setFont(QFont('Arial', 12, 50))
        
        self.txtLog = self.txtView(20, 90, 200, 120, self.root)
        self.txtLog.setText('Ative o server clicando no botão "ativar".')

        self.btAtiv:QPushButton = self.bts("Calcular", 80, 225, 75, 23, self.root)
        self.btAtiv.clicked.connect(self.btAction)

        txt = "v1.0 (10/21)\nCOPYRIGHT © 2020 KINGS"
        copyright = self.lbl(txt, 8, 20, 260, 190, 30, self.root)
        copyright.setFont(QFont('Arial', 8, 75))
        
    
    def setTxt(self, t_:str) -> None:
        r"""Define o texto mostrado na text view.

        ### Parameters
            ``t_``: str -- texto que vai ser adidionado.
        """
        text = t_ + "\n" + self.txtLog.toPlainText()
        self.txtLog.setText(text)
    

    def btAction(self) -> None:
        r"""Ação do botão calcular: faz a chamda da api e adiciona na text view o resultado."""
        try:
            if self.erro:
                self.txtLog.setText("")
                self.erro = False
            
            entrada = int(self.angInput.text())
            ang_type:str = self.opcChecked()
            data = get(URL, params={"ang":entrada, "ang_type":ang_type})

            tipo:str = "Seno" if ang_type == "sen" else "Cosseno"
            self.setTxt(f"{tipo} de {entrada}: {data.text[:7]}\n")
            
        except:
            erro_txt:str = "Houve um erro. Tente colocar um número inteiro na entrada, caso o erro pesrsita há um problema com a conexão com os servers."
            self.txtLog.setText(erro_txt)
            self.erro = True
            self.angInput.setText("")


    def opcChecked(self) -> str:
        r"""Verifica qual opção foi selecionada.

        ### Return
            ``str`` -- string que relaciona com a opção selecionada.
        """
        return "sen" if self.senOpt.isChecked() else "cos"