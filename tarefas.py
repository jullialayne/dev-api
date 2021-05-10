from flask_restful import Resource
from flask import request
import json

tarefas = ['Aprender Java','Aprender Pytho']
class Tarefas(Resource):
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

class ListarTarefas(Resource):
    def get(self):
        return tarefas
    def post(self):
        dados = json.loads(request.data)
        posicao = len(tarefas)
        tarefas.append(dados)
        return 'resultado é ',tarefas[posicao]