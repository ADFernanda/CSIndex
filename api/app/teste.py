from app import app

@app.route('/teste')
def teste():
    return "teste"