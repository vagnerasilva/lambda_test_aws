
import json
# [3] Coletando os dados para a chamada no dynamoDB


def get_headers(event, context):

    value = {
        "variavel": "valor"
    }

    return value


# [4] Criando sessao de conexao com o Dynamodb
def get_conection(event, context):

    value = {
        "variavel": "valor"
    }

    return value


# [7] Enviando dados necessarios para o SQS e pegando falback
def send_to_sqs(lista_final):

    value = {
        "fallback": "valor"
    }

    return value


# [8] Tratando resposta final para casos especificos
def format_response(response):

    response_output = {
        "statusCode": 200,
        "headers": "",
        "body": json.dumps(
            response
        ),
    }

    return response_output
