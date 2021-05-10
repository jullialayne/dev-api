from flask import Flask,jsonify,request
import json

app = Flask(__name__)

tarefas = [
    {'id':'0',
    'Responsavel':'Jullia',
    'tarefa': ['aprender Python,aprender Flask'],
    'status':'não iniciado'
     },
    {'id':'1',
    'Responsavel':'Samanta',
    'tarefa': ['aprender Java','outras'],
    'status':'não iniciado'
    }
]

@app.route('/tarefas/',methods=['POST','GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id']=posicao
        tarefas.append(dados)
        print('tarefas[id]')
        return jsonify(tarefas[id])
    elif request.method == 'GET':
        return jsonify(tarefas)

@app.route('/tarefas/<int:id>/', methods=['GET','PUT','DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefa[id]
        except IndexError:
            mensagem = 'tarefa de ID {} nao existe'.format(id)
            response = {'status':'Erro', 'Mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'Erro', 'Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefa[id]=dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'Status':'Excluido com sucesso'})


if __name__ == '__main__':
    app.run(debug=True)