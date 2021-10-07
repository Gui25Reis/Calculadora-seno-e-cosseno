# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


## Bibliotecas necessárias:
from math import factorial


def exp(num:float, exp:int) -> float:
    return pow(num, exp)


def fat(n:int) -> int: 
    return factorial(n)
    # return 1 if n == 1 else fat(n-1) * n