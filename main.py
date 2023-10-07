from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def get_json():
    # Especifique o caminho para o arquivo JSON externo
    arquivo_json = 'cosmeticos.json'  # Substitua pelo caminho real do seu arquivo JSON

    try:
        # Use send_file para enviar o arquivo JSON como resposta
        return send_file(arquivo_json, mimetype='application/json')
    except FileNotFoundError:
        return "Arquivo não encontrado", 404

app.run(host='0.0.0.0', port=81)
