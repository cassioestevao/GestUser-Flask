from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

"""
ROTA DE CLIENTES

        - /clientes/ (GET) - Listas Clientes.
        - /clientes/ (POST) - Inserir o cliente no servidor.
        - /clientes/new - Redenriza o formulario para criar o cliente.
        - /clientes/<id> (GET) - Obter os dados do cliente.
        - /clientes/<id>/edit (GET) - Renderizar formulario para um cliente.
        - /clientes/<id>/update (PUT) - Atualiza os dados do clientes.
        - /clientes/<id>/delete (DELETE) - Deleta o Registro do usuario.
   

"""

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)



@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'] ,
        "email": data['email'] ,
    }
    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html',cliente = novo_usuario)



@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')



@cliente_route.route('/<int:cliente_id>', methods=['GET'])
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')



@cliente_route.route('/<int:cliente_id>/edit', methods=['GET'])
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')




@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass




@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass
