from flask import Flask

app = Flask(__name__)

from app import conferencias
from app import papers
from app import departamentos
from app import professores