# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:
from PyQt5.QtWidgets import QLabel, QPushButton, QGroupBox, QLineEdit, QTextBrowser, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class AuxWidgets:
    r"""
    Classe usada para criação de componentes da interface gráfica

    Overview
    --------
    Os objetos da interface já estão pré determinados pra ser usado no
    programa inteiro de uma forma padranizada. Essa classe existe para
    evitar repetição de código nos outros arquivos.

    Usando ela na herança, a criação dos componentes fica mais simples
    e gasta menos tempo na hora de adicionar um componente.

    Caso precise fazer uma configuração específica, pode fazer direto
    pela variável criada para armazenar o objeto.


    Métodos
    -------
    ``lbl(self, txt_:str, tam_:int, p1_:int, p2_:int, p3_:int, p4_:int,wid_:QWidget) -> QLabel`` - cria uma label personalizada

    ``bts(self, txt_:str, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QPushButton`` - cria um botão personalizada
    
    ``lineEdit(self, tam_:int, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QLineEdit`` - cria uma linha de texto personalizada
    
    ``txtView(self, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QTextBrowser`` - cria uma caixa de texto personalizada

    ``gBox(self, n_:str, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QGroupBox`` - cria um grupo personalizado
    """         
    

    def lbl(self, txt_:str, tam_:int, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QLabel:
        r"""Cria as labels personalizadas.

        ### Parameters
            ``txt_``: str -- texto da label. \
            ``tam_``: int -- tamanho da fonte. \
            ``p1_``: int -- posição X. \
            ``p2_``: int -- posição Y. \
            ``p3_``: int -- tamanho da largura. \
            ``p4_``: int -- tamanho da altura. \
            ``wid_``: QWidget -- widget em que vai ser colocado.

        ### Return
            ``QLabel`` -- Label personalizada.
        """
        lb = QLabel(txt_, wid_)
        lb.setGeometry(p1_, p2_, p3_, p4_)
        lb.setFont(QFont('Arial', tam_))
        lb.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        return lb
    
    
    
    def bts(self, txt_:str, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QPushButton:
        r"""Cria botões personalizadas.

        ### Parameters
        ``txt_`` : str -- texto da label \
        ``tam_`` : int -- tamanho da fonte \
        ``p1_`` : int -- posição X \
        ``p2_`` : int -- posição Y \
        ``p3_`` : int -- tamanho da largura \
        ``p4_`` : int -- tamanho da altura \
        ``wid_`` : QWidget -- widget em que vai ser colocado 

        ### Return
        ``QPushButton`` -- Botão perzonalizado a partir dos Parameters passados.
        """
        bt = QPushButton(txt_, wid_)
        bt.setGeometry(p1_, p2_, p3_, p4_)
        bt.setFont(QFont('Arial', 10))
        return bt
    

    def lineEdit(self, tam_:int, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QLineEdit:
        r"""Cria as linhas de texto personalizadas.

        ### Parameters
        ``tam_`` : int -- tamanho da fonte \
        ``p1_`` : int -- posição X \
        ``p2_`` : int -- posição Y \
        ``p3_`` : int -- tamanho da largura \
        ``p4_`` : int -- tamanho da altura \
        ``wid_`` : QWidget -- widget em que vai ser colocado

        ### Return
        ``QLineEdit`` -- Linha de texto perzonalizada a partir dos Parameters passados.
        """
        le = QLineEdit(wid_)
        le.setGeometry(p1_, p2_, p3_, p4_)
        le.setFont(QFont('Arial', tam_))
        le.setStyleSheet("background-color: white")
        return le

    

    def txtView(self, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QTextBrowser:
        r"""Cria as caixas de texto personalizadas.

        ### Parameters
        ``p1_`` : int -- posição X \
        ``p2_`` : int -- posição Y \
        ``p3_`` : int -- tamanho da largura \
        ``p4_`` : int -- tamanho da altura \
        ``wid_`` : QWidget -- widget em que vai ser colocado

        ### Return
        ``QTextBrowser`` -- Caixa de texto perzonalizada a partir dos Parameters passados.
        """
        tv = QTextBrowser(wid_)
        tv.setGeometry(p1_, p2_, p3_, p4_)
        tv.setFont(QFont('Consolas', 10))
        return tv


    def gBox(self, txt_:str, p1_:int, p2_:int, p3_:int, p4_:int, wid_:QWidget) -> QGroupBox:
        r"""Cria as áreas de vizualização de gráfico personalizadas.

        ### Parameters
        ``p1_`` : int -- posição X \
        ``p2_`` : int -- posição Y \
        ``p3_`` : int -- tamanho da largura \
        ``p4_`` : int -- tamanho da altura \
        ``wid_`` : QWidget -- widget em que vai ser colocado

        ### Return
        ``QGraphicsView`` -- Área de vizualização de gráfico perzonalizada a partir dos Parameters passados.
        """
        gb = QGroupBox(txt_, wid_)
        gb.setGeometry(p1_, p2_, p3_, p4_)
        gb.setFont(QFont('Arial', 12))
        gb.setStyleSheet("QGroupBox {border: 1px solid brown;}")
        return gb