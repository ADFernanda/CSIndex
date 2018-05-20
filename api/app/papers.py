from app import app
from flask import request, make_response
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
        nomeArquivo = path.join("..","data", area) + "-out-papers.csv"        
        csvfile =  open(nomeArquivo)
        saida = csvfile.read()
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return (make_response(saida), 200, {"Content-Disposition": 'inline; filename="obterPapersEmArea.csv"', "Content-Type": "text/csv"})

# 8. Todos os papers de uma area em um determinado ano
@app.route('/obterPapersEmAreaEmAno')
def obterPapersEmAreaEmAno():
    area = request.args.get('area')
    ano = request.args.get('ano')

    if not area or not ano:
        return Response(status=400)

    try:
        retorno=''
        nomeArquivo = path.join("..","data", area) + "-out-papers.csv"   
        with open(nomeArquivo, 'rb') as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[0] == ano):
                    line = str(row)
                    line = line.replace("'","")
                    retorno += str(line[1:-1]) + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return (make_response(retorno), 200, {"Content-Disposition": 'inline; filename="obterPapersEmAreaEmAno.csv"', "Content-Type": "text/csv"})

# 9. Todos os papers de um departamento em uma area
@app.route('/obterPapersEmAreaEmDepartamento')
def obterPapersEmAreaEmDepartamento():
    area = request.args.get('area')
    departamento = request.args.get('departamento')

    if not area or not departamento:
        return Response(status=400)

    try:
        retorno=''
        nomeArquivo = path.join("..","data", area) + "-out-papers.csv"   
        with open(nomeArquivo, 'rb') as csvfile:
            papers = csv.reader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in papers:
                if (row[3] == departamento):
                    line = str(row)
                    line = line.replace("'","")
                    retorno += str(line[1:-1]) + '\n'
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return (make_response(retorno), 200, {"Content-Disposition": 'inline; filename="obterPapersEmAreaEmAno.csv"', "Content-Type": "text/csv"})

# 10. Todos os papers de um professor (dado o seu nome)
@app.route('/obterPapersDeProfessor')
def obterPapersDeProfessor():
    professor = request.args.get('professor')

    if not professor:
        return Response(status=400)

    try:
        nomeArquivo = path.join("..","data","profs", "search", professor) + ".csv"   
        csvfile =  open(nomeArquivo)
        saida = csvfile.read()
    except IOError:
        return Response(status=404)        
    except:
        return Response(status=500)
    return (make_response(saida), 200, {"Content-Disposition": 'inline; filename="obterPapersDeProfessor.csv"', "Content-Type": "text/csv"})