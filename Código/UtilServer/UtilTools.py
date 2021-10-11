# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:
from math import factorial


def exp(num:float, exp:int) -> float:
    r"""Conta simples de exponenciação.

    ### Parameters
        ``num``: float -- Base da conta. \
        ``exp``: int -- Exposnete da conta.

    ### Return
        ``float`` -- Resultado da exponenciação.
    """
    return pow(num, exp)


def fat(n:int) -> int: 
    r"""Conta simples fatorial.

    Obs: Python limita a quantidade de recursão, por isso está
    sendo usado uma função já printa para o fatorial.

    ### Parameters
        ``n``: int -- Número a ser fatorado. \

    ### Return
        ``int`` -- Resultado da fatoração.
    """
    return factorial(n)
    # return 1 if n == 1 else fat(n-1) * n      # Função recursiva