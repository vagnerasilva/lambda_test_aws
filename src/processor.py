
from src.helpers import get_headers
from src.helpers import get_conection
# from helpers import get_list_dynamodb
# from helpers import process_list_dynamodb
from src.helpers import send_to_sqs
from src.helpers import format_response

# [2] Processando evento de entrada


def lambda_processor(event, context):

    try:
        # [3] Coletando os dados para a chamada no dynamoDB
        info_conection = get_headers(event, context)

        # [4] Criando sessao de conexao com o Dynamodb
        session_dynamodb = get_conection(event, context)

        # [5] coletando lista no dynamoDB
        response_list = get_list_dynamodb(info_conection, session_dynamodb)

        # [6] Processando lista em resultado esperado na chamada
        lista_final = process_list_dynamodb(response_list)

        # [7] Enviando dados necessarios para o SQS e pegando falback
        response = send_to_sqs(lista_final)

        # [8] Tratando resposta final para casos especificos
        response_output = format_response(response)
        return response_output
    except:
        print("An exception occurred")
        response = "ERRO "
        # [8] Tratando resposta final para casos especificos
        response_output = format_response(response)
        return response_output


# [6] Processando lista em resultado esperado na chamada
def get_list_dynamodb(info_conection, session_dynamodb):

    list_dynamodb = []
    return list_dynamodb


# [6] Processando lista em resultado esperado na chamada
def process_list_dynamodb(response_list):

    response_list_output = []
    return response_list_output
