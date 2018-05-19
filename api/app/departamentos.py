#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import request, make_response
from os import path

# servicos 3 e 4
# 3. Scores de todos os departamentos em uma área
# 4. Score de um determinado departamento em uma área.

@app.route("/score")
def obterScoresAreaPorDepartamento():
	retorno = "<h1>"
	try:
		area = request.args.get("area")
		departamento = request.args.get("departamento")
		if not area:
			retorno += "Especifique na url /score?area=<area>&departamento=<departamento>(opcional)"
		else:
			retorno += "Obtendo scores para a área ".decode("utf8") + area
			if not departamento:
				retorno += " de todos seus departamentos"
			else:
				retorno += " e departamento " + departamento
	except:
		app.logger.exception("Exceção disparada na leitura da URL!")
		raise
	else:
		app.logger.debug("Leitura da URL foi um sucesso!")
	finally:
		if not area:
			retorno += "</h1>"
			return retorno
		retorno += "...</h1>"
		try:
			areaParaBusca = area.lower()
			arquivo = open(path.join("..","data",areaParaBusca) + "-out-scores.csv")
			retorno += "<h2>"
			if not departamento:
				saida = arquivo.read()
				retorno = saida.replace("\n","<br />")
				saida = make_response(saida)
			else:
				saida = filter(lambda linha: linha.find(departamento+",") == 0, arquivo)
				if not saida:
					retorno += "Score não encontrado para o departamento ".decode("utf8") + departamento
				else:
					retorno += saida[0]
					saida = make_response(saida[0])
			if 'saida' in locals():
				saida = (saida, 200, {"Content-Disposition": 'inline; filename="queryScores.csv"', "Content-Type": "text/csv"})
			retorno += "</h2>"
		except IOError:
			retorno += "<h1>Scores não encontrados para a área ".decode("utf8") + area + "</h1>"
			app.logger.exception("Exceção disparada na leitura dos arquivos!")
			raise
		except:
			app.logger.exception("Exceção disparada na leitura dos arquivos!")
			raise
		else:
			app.logger.debug("Leitura dos arquivos foi um sucesso!")
		finally:
			if 'saida' in locals():
				return saida
			else:
				return retorno