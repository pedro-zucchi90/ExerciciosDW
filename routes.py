from flask import Flask, request
import uuid

app = Flask(__name__)

calculos = []

@app.route("/soma", methods=["POST"])
def soma():
    dados_recebido = request.get_json()
    num1 = float(dados_recebido['num1'])
    num2 = float(dados_recebido['num2'])
    resultado = num1 + num2
    calculos.append(
        {
            "id": str(uuid.uuid4()),
            "num1": num1,
            "num2": num2,
            "resultado": resultado
        }
    )
    return {'resultado': resultado}

@app.route("/calculos", methods=["GET"])
def mostrarSomas():
    return calculos

@app.route("/deletar/<id>", methods=["DELETE"])
def deletar(id):
    global calculos
    id_uuid = uuid.UUID(id)
    
    calculos = [calculo for calculo in calculos if uuid.UUID(calculo['id']) != id_uuid]
    
    return {"mensagem": "calculo removido com sucesso"}

@app.route("/editar/<id>", methods=["PUT"])
def editar_item(id):
    global calculos
    dados_recebido = request.get_json()
    num1 = float(dados_recebido['num1'])
    num2 = float(dados_recebido['num2'])
    
    id_uuid = uuid.UUID(id)

    for calculo in calculos:
        if uuid.UUID(calculo['id']) == id_uuid:
            calculo['num1'] = num1
            calculo['num2'] = num2
            calculo['resultado'] = num1 + num2
            break

    return {"mensagem": "calculo editado com sucesso"}
