from app import app
from flask import request
import csv

# servicos 1 e 2 

@app.route('/obterNumeroPublicacoes')
def obterNumeroPublicacoes():
    area = request.args.get('conferencia')
    area = request.args.get('area')

    path = '../data/'
    nomeArquivo = path + area + '-out-papers.csv'
    
    with open(nomeArquivo) as csvfile:
        papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    return 'oi'