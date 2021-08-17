from flask import Flask, jsonify, request
import json
app = Flask(__name__)
desenvolvedores = [
    {
    'id':0,
    'nome':'Fernando',
    'habilidades':['python','flask']
    },
    {
    'id':1,
    'nome':'Rafael',
    'habilidades':['python','django']
    }
]
#- Devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])#@app.route('/dev/<int:id>', methods='GET')
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            #desenvolvedor = desenvolvedores[id]
            #return jsonify(desenvolvedor)
            print(desenvolvedores[0]['habilidades'])
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'statur':'Erro','mensagem':mensagem}
        return jsonify(response)

        #return jsonify({'nome':'Fernando'})
    elif request.method == 'PUT':
        dados = json.loads(request.data) # Pega os dados passados no corpo do request no POSTMAN
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensaem':'Registro excluído.'})

#- Lista os desenvolvedores e inclui um novo desenvolvedor.
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id']=posicao # O parametro id do dicionario recebe o indice
        desenvolvedores.append(dados)
       # return jsonify({'status':'sucesso', 'mensagem':'registro inserido.'})
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
if __name__ == '__main__':
    app.run(debug=True)
