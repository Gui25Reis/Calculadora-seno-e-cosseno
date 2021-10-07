# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


## Bibliotecas necessárias:
from requests import get
from math import pi as math_pi

URL = "http://192.168.15.73:5050/"

SOMATORIA = 10


def cos(ang:float, n=SOMATORIA) -> float:
    if (n == 0):
        return conta(ang, n, 0)
    return conta(ang, n, 0) + cos(ang, n-1)


def sen(ang:float, n=SOMATORIA) -> float:
    if (n == 0):
        return conta(ang, n, 1)
    return conta(ang, n, 1) + sen(ang, n-1)
    

def rad(ang:int) -> float:
    return ang*math_pi/180


def conta(ang:float, n:int, x:int) -> float:
    fat:int = get(URL, params=param(fat=2*n+x)).json()["fat"]
    exp1:float = get(URL, params=param(base=-1, exp=n)).json()["exp"]
    exp2:float = get(URL, params=param(base=ang, exp=2*n + x)).json()["exp"]
    
    conta = exp1/fat * exp2
    return conta


def param(base:float=None, exp:float=None, fat:int=None) -> dict:
    return {
        'base' : base,
        'exp' : exp,
        'fat' : fat
    }