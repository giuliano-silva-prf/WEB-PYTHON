from app import app

print('O módulo controle foi executado\n__name__==', __name__)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
