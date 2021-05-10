from flask import Flask,request
from flask_restful import Resource, Api
from tarefas import Tarefas,ListarTarefas
import json

app = Flask(__name__)
api = Api(app)

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

class Tarefa(Resource):
    def get(self,id):
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'tarefa de ID {} nao existe'.format(id)
            response = {'status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'Erro', 'Mensagem': mensagem}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        tarefas[id] = dados
        return dados
    def delete(self, id):
       tarefas.pop(id)
       return {'Status': 'Excluido com sucesso'}


class ListaTarefas(Resource):
    def get(self):
        return tarefas
    def post(self):
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return tarefas[posicao]


api.add_resource(Tarefa,'/tarefa/<int:id>')
api.add_resource(ListaTarefas,'/tarefa/')
api.add_resource(Tarefas,'/tarefas/<int:id>')
api.add_resource(ListarTarefas,'/tarefas/')

if __name__ == '__main__':
    app.run(debug=True)