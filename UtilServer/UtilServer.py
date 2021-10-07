# -*- coding: utf-8 -*-

__author__ = "Gui Reis"
__copyright__ = "COPYRIGHT © 2021 KINGS"
__version__ = "1.0"
__status__ = "Production"
__license__ = " "


## Bibliotecas necessárias:
from flask import Flask, request
from UtilTools import exp, fat


appUtil = Flask(__name__)


@appUtil.route('/', methods=['GET'])
def home() -> dict:
    try:
        fato = request.args.get('fat')

        # Exp
        if (fato == None):
            base = request.args.get('base')
            expo = request.args.get('exp')
            
            # Verifica se tem valor
            if (base == expo == None):
                return {"Error":"Um dos valores é nulo"}

            base = float(base)
            expo = float(expo)

            conta = exp(base, expo)
            return {"exp":conta}
        
        # Fat  
        fato = int(fato)
        conta = fat(fato)
        return {"fat":conta}

    except:
        return {"Error":"Teve algum erro"}


if __name__ == '__main__':
    appUtil.run(host='0.0.0.0', port=5050, debug=True)