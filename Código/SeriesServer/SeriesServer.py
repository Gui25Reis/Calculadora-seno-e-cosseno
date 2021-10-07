# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


## Bibliotecas necessárias:
from flask import Flask, request
from SeriesTools import sen, cos, rad


appSeries = Flask(__name__)


@appSeries.route('/', methods=['GET', 'POST'])
def home():
    ang:int = request.args.get('ang')
    ang_type:str = request.args.get('ang_type')

    ang_rad = rad(int(ang))

    if ang_type == "sen":
        return f"{sen(ang_rad)}"
    return f"{cos(ang_rad)}"


if __name__ == '__main__':    
    appSeries.run(host='0.0.0.0', port=5000, debug=True)