from app import app
from flask import make_response
from os import path

def montaRespostaCSV(conteudo,nomeArquivo):
	return (make_response(conteudo), 200, {\
		"Content-Disposition"	: 'inline; filename="' + nomeArquivo + '.csv"',\
		"Content-Type"			: "text/csv"\
	})

def abreCSVAreaOutSufixo(area,sufixo):
	return open(path.join("..","data",area.lower()) + "-out-" + sufixo + ".csv")