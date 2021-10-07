# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


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
    ## Construtor: Cria a janela principal com o menu e o local onde vai ser colocado as páginas
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
        lblAng = self.lbl("Ângulo: ", 12, 20, 20, 60, 20, self.root)
        self.angInput = self.lineEdit(10, 95, 20, 120, 20, self.root)

        self.senOpt = QRadioButton("Seno", self.root)                           # Cria a opção de Idioma
        self.senOpt.setGeometry(QtCore.QRect(20, 60, 75, 18))                   # Define a posição
        self.senOpt.setFont(QFont('Arial', 12, 50))
        self.senOpt.setChecked(True)                                            # Deixa marcado como padrão
        
        self.cosOpt = QRadioButton("Cosseno", self.root)                        # Cria a opção de Idioma
        self.cosOpt.setGeometry(QtCore.QRect(125, 60, 90, 18))                  # Define a posição
        self.cosOpt.setFont(QFont('Arial', 12, 50))
        
        self.txtLog = self.txtView(20, 90, 200, 120, self.root)                # Cria a área de vizualização de texto
        self.txtLog.setText('Ative o server clicando no botão "ativar".')               # Define o texto inicial

        self.btAtiv:QPushButton = self.bts("Calcular", 80, 225, 75, 23, self.root)            # Cria o botão (Ler PLanílha | Ativar | Atualizar)
        self.btAtiv.clicked.connect(self.btAction)

        txt = "v1.0 (09/21)\nCOPYRIGHT © 2021 KINGS"
        copyright = self.lbl(txt, 8, 20, 260, 190, 30, self.root)
        copyright.setFont(QFont('Arial', 8, 75))
        
    
    ## Método especial: define o texto
    def setTxt(self, t_:str) -> None: 
        text = t_ + "\n" + self.txtLog.toPlainText()
        self.txtLog.setText(text)
    

    ## Método: ação do botão
    def btAction(self) -> None:
        try:
            if self.erro:
                self.txtLog.setText("")
                self.erro = False
            
            entrada = int(self.angInput.text())
            ang_type:str = self.opcChecked()
            data = get(URL, params={"ang":entrada, "ang_type":ang_type})

            tipo = "Seno" if ang_type == "sen" else "Cosseno"
            self.setTxt(f"{tipo} de {entrada}: {data.text[:7]}\n")
            
        except:
            self.txtLog.setText("Houve um erro. Tente colocar um número inteiro na entrada, caso o erro pesrsita há um problema com a conexão com os servers.")
            self.erro = True
            self.angInput.setText("")


    ## Método: Verifica a opção selecionada da linguegem
    def opcChecked(self) -> str:
        if self.senOpt.isChecked():                                               # Verifica se "Português-Brazil" está marcado
            return "sen"                                                                # 1 -> Português-Brazil
        return "cos"                                                                    # 0 -> English
