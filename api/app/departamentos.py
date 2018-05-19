#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import request

# servicos 3 e 4
# 3. Scores de todos os departamentos em uma área
# 4. Score de um determinado departamento em uma área.

@app.route('/score')
def obterScoresAreaPorDepartamento():
	area = request.args.get('area')
	departamento = request.args.get('departamento')
	retorno = "<h1>"
	if area == None:
		retorno += "Especifique na url /score?area=<area>&departamento=<departamento>(opcional)"
	else:
		retorno += "Obtendo scores para a área ".decode('utf8') + area
		if departamento == None:
			retorno += " de todos seus departamentos"
		else:
			retorno += " e departamento " + departamento
	retorno += "...</h1>"
	return retorno