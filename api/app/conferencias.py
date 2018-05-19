from app import app
from flask import request
import csv
import numpy

# servicos 1 e 2 


@app.route('/obterNumeroPublicacoes')
def obterNumeroPublicacoes():
    conferencia = request.args.get('conferencia')
    area = request.args.get('area')

    path = '../data/'
    nomeArquivo = path + area + '-out-papers.csv'
    
    numPublicacoes = 0

    with open(nomeArquivo, 'rb') as csvfile:
        papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in papers:
            if (row[1] == conferencia):
                numPublicacoes = numPublicacoes + 1
    
    return str(numPublicacoes)