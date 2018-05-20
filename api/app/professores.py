from app import app, util
from flask import request, Response

# servicos 5 e 6
# 5. Numero de professores que publicam em uma determinada area (organizados por departamentos)
# 6. Numero de professores de um determinado departamento que publicam em uma area

@app.route("/obterNumerosProfessoresEmArea")
def obterNumerosProfessoresEmArea():
	area = request.args.get("area")
	if not area:
		return Response(status=400)
	try:
		arquivo = util.abreCSVAreaOutSufixo(area,"profs")
	except IOError:
		return Response(status=404)
	conteudoArquivo = arquivo.read()
	arquivo.close()
	return util.montaRespostaCSV(conteudoArquivo, "obterNumerosProfessoresEmArea")


@app.route("/obterNumeroProfessoresEmAreaEDepartamento")
def obterNumeroProfessoresEmAreaEDepartamento():
	area = request.args.get("area")
	departamento = request.args.get("departamento")
	if not area or not departamento:
		return Response(status=400)
	try:
		arquivo = util.abreCSVAreaOutSufixo(area,"profs")
	except IOError:
		return Response(status=404)
	achaDepartamento = filter(lambda linha: linha.find(departamento+",") == 0, arquivo)
	if not achaDepartamento:
		return Response(status=404)
	arquivo.close()
	return util.montaRespostaCSV(achaDepartamento[0], "obterNumeroProfessoresEmAreaEDepartamento")