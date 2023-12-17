"""Aplicação web com flask - Básica.v1
   Mode debug ativado; 
   Definindo a porta de comunicação para aplicação
"""
from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/Giuliano')
def home():
    return 'Tudo nosso33333!'

if __name__ == "__main__":
    app.run(debug=True, port=8080)  