#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import request

# servicos 3 e 4
# 3. Scores de todos os departamentos em uma área
# 4. Score de um determinado departamento em uma área.

@app.route("/score")
def obterScoresAreaPorDepartamento():
	retorno = "<h1>"
	try:
		area = request.args.get("area")
		departamento = request.args.get("departamento")
		if area == None:
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
		retorno += "...</h1>"
		try:
			areaParaBusca = area.lower()
			arquivo = open("..\\data\\" + areaParaBusca + "-out-scores.csv")
			retorno += "<h2>"
			if not departamento:
				retorno += arquivo.read().replace("\n","<br />")
			else:
				retorno += "Em construção".decode("utf8")
			retorno += "</h2>"
		except FileNotFoundError:
			retorno += "<h1>Scores não encontrados para a área ".decode("utf8") + area + "</h1>"
			app.logger.exception("Exceção disparada na leitura dos arquivos!")
			raise
		except:
			app.logger.exception("Exceção disparada na leitura dos arquivos!")
			raise
		else:
			app.logger.debug("Leitura dos arquivos foi um sucesso!")
		finally:
			return retorno