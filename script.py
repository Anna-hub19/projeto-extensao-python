from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
data = []

@app.route('/cadastro', methods=['POST'])
def cadastro():
    try:
        nome = request.json['nome']
        idade = request.json['idade']
        genero = request.json['genero']
        renda = request.json['renda']
        escolaridade = request.json['escolaridade']
        bairro = request.json['bairro']
        
        novo_membro = {
            'Nome': nome,
            'Idade': idade,
            'Gênero': genero,
            'Renda': renda,
            'Escolaridade': escolaridade,
            'Bairro': bairro
        }
        
        data.append(novo_membro)
        return jsonify({'message': 'Membro cadastrado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/visualizar', methods=['GET'])
def visualizar():
    try:
        df = pd.DataFrame(data)
        return df.to_html(), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
