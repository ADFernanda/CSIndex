from flask import Flask, request

app = Flask(__name__)

@app.after_request
def enable_cors_all_origins(response):
	response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or '*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
	return response

from app import conferencias
from app import papers
from app import departamentos
from app import professores