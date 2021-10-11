# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:
from requests import get
from math import pi as math_pi

URL:str = "http://192.168.15.73:5050/"

SOMATORIA:int = 10


def cos(ang:float, n=SOMATORIA) -> float:
    r"""Pega o cosseno do ângulo.

    ### Parameters
        ``ang``: float -- Ângulo em radianos \
        ``n``: int -- Quantidade de vezes que vai fazer a somatória.

    ### Return
        ``float`` -- Ângulo cosseno.
    """
    if (n == 0):
        return conta(ang, n, 0)
    return conta(ang, n, 0) + cos(ang, n-1)


def sen(ang:float, n=SOMATORIA) -> float:
    r"""Pega o seno do ângulo.

    ### Parameters
        ``ang``: float -- Ângulo em radianos \
        ``n``: int -- Quantidade de vezes que vai fazer a somatória.

    ### Return
        ``float`` -- Ângulo seno.
    """
    if (n == 0):
        return conta(ang, n, 1)
    return conta(ang, n, 1) + sen(ang, n-1)
    

def rad(ang:int) -> float:
    r"""Transforma o ângulo em radianos (°C -> rad).

    ### Parameters
        ``ang``: float -- Ângulo em celcius \
        ``n``: int -- Quantidade de vezes que vai fazer a somatória.

    ### Return
        ``float`` -- Ângulo cosseno.
    """
    return ang*math_pi/180


def conta(ang:float, n:int, x:int) -> float:
    r"""Somatória para o calculo de seno e cosseno.

    ### Parameters
        ``ang``: float -- Ângulo em radianos \
        ``n``: int -- Momento da somatória. \
        ``x``: int -- Variável que soma na conta, diferenciando se é seno ou cosseno.

    ### Return
        ``float`` -- Valor da conta da fórmula da somatória.
    """
    fat:int = get(URL, params=param(fat=2*n+x)).json()["fat"]
    exp1:float = get(URL, params=param(base=-1, exp=n)).json()["exp"]
    exp2:float = get(URL, params=param(base=ang, exp=2*n + x)).json()["exp"]
    
    conta = exp1/fat * exp2
    return conta


def param(base:float=None, exp:float=None, fat:int=None) -> dict:
    r"""Cria um dicionário para ser passado como parâmetro na chamada da API.

    ### Parameters
        ``base``: float -- Base da exponenciação. \
        ``exp``: float -- Expoente da exponenciação. \
        ``fat``: int -- Valor para a conta do fatorial.

    ### Return
        ``Dict[str:float]`` -- Dicionário com os parâmetros passado.
    """
    return {
        'base' : base,
        'exp' : exp,
        'fat' : fat
    }