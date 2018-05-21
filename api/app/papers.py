from app import app, util
from flask import request
from flask import Response
import csv
from os import path

# servico 7. Todos os papers de uma area (ano, titulo, deptos e autores)
@app.route('/obterPapersEmArea')
def obterPapersEmArea():
    area = request.args.get('area')

    if not area:
        return Response(status=400)

    try:
        saida = ''
        with util.abreCSVAreaOutSufixo(area,"papers")  as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                    saida +=  row[0] + ',' + row[2] + ',' + row[3] + ',' + row[4] + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return util.montaRespostaCSV(saida, "obterPapersEmArea")

# 8. Todos os papers de uma area em um determinado ano
@app.route('/obterPapersEmAreaEmAno')
def obterPapersEmAreaEmAno():
    area = request.args.get('area')
    ano = request.args.get('ano')

    if not area or not ano:
        return Response(status=400)

    try:
        retorno=''
        with util.abreCSVAreaOutSufixo(area,"papers")  as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[0] == ano):
                    retorno +=  row[0] + ',' + row[2] + ',' + row[3] + ',' + row[4] + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return util.montaRespostaCSV(retorno, "obterPapersEmAreaEmAno")

# 9. Todos os papers de um departamento em uma area
@app.route('/obterPapersEmAreaEmDepartamento')
def obterPapersEmAreaEmDepartamento():
    area = request.args.get('area')
    departamento = request.args.get('departamento')

    if not area or not departamento:
        return Response(status=400)

    try:
        retorno=''
        with util.abreCSVAreaOutSufixo(area,"papers")  as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[3] == departamento):
                    retorno +=  row[0] + ',' + row[2] + ',' + row[3] + ',' + row[4] + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return util.montaRespostaCSV(retorno, "obterPapersEmAreaEmDepartamento")

# 10. Todos os papers de um professor (dado o seu nome)
@app.route('/obterPapersDeProfessor')
def obterPapersDeProfessor():
    professor = request.args.get('professor')

    if not professor:
        return Response(status=400)

    try:
        nomeArquivo = path.join("..","data","profs", "search", professor) + ".csv"   
        csvfile =  open(nomeArquivo)
        saida = ''
        with csvfile  as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                    saida +=  row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return util.montaRespostaCSV(saida, "obterPapersDeProfessor")