"""Aplicação web com flask - Básica.v1
   Mode debug ativado; 
"""
from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/Giuliano')
def home():
    return 'Tudo nosso!'

if __name__ == "__main__":
    app.run(debug=True)  