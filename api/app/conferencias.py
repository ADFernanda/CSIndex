from app import app, util
from flask import request
from flask import Response
import csv
from os import path

# servico 1: Numero de publicacoes no conjunto de conferencias de uma area
@app.route('/obterNumeroPublicacoesEmConferenciaEArea')
def obterNumeroPublicacoesEmConferenciaEArea():
    conferencia = request.args.get('conferencia')
    area = request.args.get('area')

    if not conferencia or not area:
        return Response(status=400)

    numPublicacoes = 0

    try:
        with util.abreCSVAreaOutSufixo(area,"papers")  as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[1] == conferencia.upper()):
                    numPublicacoes += 1
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)  
    return util.montaRespostaCSV(str(numPublicacoes), "obterNumeroPublicacoesEmConferenciaEArea")

# servico 2: Numero de publicacoes no conjunto de conferencias de uma area
@app.route('/obterNumeroPublicacoesEmArea')
def obterNumeroPublicacoesEmArea():
    area = request.args.get('area')

    if not area:
        return Response(status=400)

    numPublicacoes = 0

    try:
        with util.abreCSVAreaOutSufixo(area,"papers") as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                numPublicacoes += 1
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return util.montaRespostaCSV(str(numPublicacoes), "obterNumeroPublicacoesEmArea")