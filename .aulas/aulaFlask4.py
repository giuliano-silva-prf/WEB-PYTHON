"""Aplicação web com flask - Básica.v1
   Mode debug ativado; 
   Definindo a porta de comunicação para aplicação
   Permitindo acesso de outros aplicativos da mesma rede.
"""
from dotenv import load_dotenv
load_dotenv()

from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/Giuliano')
def home():
    return 'Tudo nosso4444!'

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")  