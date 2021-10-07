# Calculadora-seno-e-cosseno
[![Versão](https://img.shields.io/badge/version-v1.0.0-orange)](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/releases/tag/1.0.0)
<!-- ![Tamanho](https://img.shields.io/badge/size-75%20MB-blue) -->
![Plataformas](https://img.shields.io/badge/plataforma-Windows-lightgrey?logo=windows)
[![Versão python](https://img.shields.io/badge/python-v3.8.5-blue?logo=python)](https://www.python.org/downloads/release/python-385/)
[![Licença](https://img.shields.io/badge/license-GNU3-brightgreen?)](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/master/LICENSE)


Prova P1 da matéria de Computação distribuída.

1. [Instalação](#instalação)
2. [Requerimentos](#requerimentos)
4. [Documentação](#documentação)
4. [Guia-Rápido](#guia-rápido)
5. [Licença](#licença)
6. [Autor](#autor)

## Instalação
Baixando o repositório você consegue ter acesso ao código. Para executar o programa precisa basta seguir esses passos:
- Precisa pegar o IPV4 da sua máquina. Para fazer isso basta digitar o comando ```ipconfig``` no terminal.

![Imagem mostrando o terminal](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/Arquivos/Imagens/rd-Ipconfig.png)



- Atualizar no arquivo [```SeriesTools.py```](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/C%C3%B2digo/SeriesServer/SeriesTools.py) na variável ```URL``` (linha 14) com o seu IPV4.


![Imagem mostrando a linha que precisa ser alterada](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/Arquivos/Imagens/rd-Url.png)


- Depois precisa executar (e deixar ligado) os dois server: [```SeriesServer.py```](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/C%C3%B2digo/SeriesServer/SeriesServer.py) e [```UtilServer.py```](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/C%C3%B2digo/UtilServer/UtilServer.py)

![Gif mostrando como ligar os servers](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/Arquivos/V%C3%ADdeos/Ligando-servers.gif)

- Por fim, para poder inserir os dados basta rodar o cliente executando o arquivo [```Main.py```](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/C%C3%B2digo/Main.py)

![Gif mostrando como iniciar o cliente](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/main/Arquivos/V%C3%ADdeos/Ligando-cliente.gif)

## Requerimentos
O programa foi feito em ```python 3.8.5``` com a adição de duas bibliotecas externa. Para instalar basta copiar o código em destaque no seu terminal.

Uma delas é para a Interface Gráfica (GUI) chamada [PyQt5](https://pypi.org/project/PyQt5/).

    pip install pyqt5-tools

A outra é para a conexão via ```get()``` entre os server, utilizando a biblioteca [Requests](https://pypi.org/project/requests/). 

    pip install requests


## Documentação
A documentação do projeto está feita na [wiki](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/wiki) do repositório.

## Licença
Este projeto é licenciado por [GNU-3 License](https://github.com/Gui25Reis/Prova-P1-Calculadora-seno-e-cosseno/blob/master/LICENSE).

## Autor
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/Gui25Reis">
                <img src="https://avatars1.githubusercontent.com/u/48360732" width="100px;" alt="Foto do Gui Reis no GitHub"/><br>
                <sub>
                    <b>Gui Reis</b>
                </sub>
            </a>
        </td>
    </tr>
</table>

