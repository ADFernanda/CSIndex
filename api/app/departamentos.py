from app import app, util
from flask import request, Response

# servicos 3 e 4
# 3. Scores de todos os departamentos em uma area
# 4. Score de um determinado departamento em uma area.

@app.route("/obterScoresEmArea")
def obterScoresEmArea():
	area = request.args.get("area")
	if not area:
		return Response(status=400)
	try:
		arquivo = util.abreCSVAreaOutSufixo(area,"scores")
	except IOError:
		return Response(status=404)
	conteudoArquivo = arquivo.read()
	arquivo.close()
	return util.montaRespostaCSV(conteudoArquivo, "obterScoresEmArea")


@app.route("/obterScoreEmAreaEDepartamento")
def obterScoreEmAreaEDepartamento():
	area = request.args.get("area")
	departamento = request.args.get("departamento")
	if not area or not departamento:
		return Response(status=400)
	try:
		arquivo = util.abreCSVAreaOutSufixo(area,"scores")
	except IOError:
		return Response(status=404)
	achaDepartamento = filter(lambda linha: linha.find(departamento+",") == 0, arquivo)
	if not achaDepartamento:
		return Response(status=404)
	arquivo.close()
	return util.montaRespostaCSV(achaDepartamento[0], "obterScoreEmAreaEDepartamento")