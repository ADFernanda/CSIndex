from app import app
from flask import request
from flask import Response
import csv
from os import path

# servicos 1 e 2 


@app.route('/obterNumeroPublicacoes')
def obterNumeroPublicacoes():
    conferencia = request.args.get('conferencia')
    area = request.args.get('area')

    if not conferencia or not area:
        return Response(status=400)

    numPublicacoes = 0

    try:
        nomeArquivo = path.join("..","data", area) + "-out-papers.csv"        

        with open(nomeArquivo, 'rb') as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[1] == conferencia):
                    numPublicacoes += 1
    except FileNotFoundError:
        return Response(status=404)
        raise
    except:
        return Response(status=500)
        raise
    finally:
        return str(numPublicacoes)