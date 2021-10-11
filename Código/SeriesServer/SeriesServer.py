# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Entregue"
__license__ = "https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/LICENSE"


## Bibliotecas necessárias:
from flask import Flask, request
from SeriesTools import sen, cos, rad


appSeries = Flask(__name__)


@appSeries.route('/', methods=['GET', 'POST'])
def home() -> str:
    r"""Função principal que é executada assim que faz uma requisição.

    ### Return:
        ```str`` -- Ângulo seno/cosseno.
    """

    ang:int = request.args.get('ang')
    ang_type:str = request.args.get('ang_type')

    ang_rad:float = rad(int(ang))

    if ang_type == "sen":
        return f"{sen(ang_rad)}"
    return f"{cos(ang_rad)}"


if __name__ == '__main__':    
    appSeries.run(host='0.0.0.0', port=5000, debug=True)