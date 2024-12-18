from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permite CORS para todas as rotas

@app.route('/run', methods=['POST'])  # Certifique-se de que 'POST' está aqui
def run_code():
    data = request.get_json()
    code = data.get('code', '')

    # Salvar o código em um arquivo temporário
    with open('temp_code.py', 'w') as f:
        f.write(code)

    try:
        # Executar o código e capturar a saída
        output = subprocess.check_output(['python3', 'temp_code.py'], stderr=subprocess.STDOUT, timeout=5)
        result = output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        result = e.output.decode('utf-8')
    except Exception as e:
        result = str(e)

    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)