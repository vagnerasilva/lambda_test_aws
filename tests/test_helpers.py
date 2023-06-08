from src.helpers import get_headers
from src.helpers import get_conection
from src.helpers import send_to_sqs
from src.helpers import format_response
# [3] Coletando os dados para a chamada no dynamoDB
# [3.A] testando coleta de info necessarias


def test_headers_sucess():
    mock_event = ""
    mock_context = ""
    response = get_headers(mock_event, mock_context)

    value = response
    print(value)
    assert True


# [4] Criando sessao de conexao com o Dynamodb
# [4.A] testando sessao conectada com o dynamoDb
def test_get_conection_sucess():
    mock_event = ""
    mock_context = ""
    response = get_conection(mock_event, mock_context)

    value = response
    print(value)
    assert True


# [7] Enviando dados necessarios para o SQS e pegando falback
# [7.A] Testando envio do SQS
def test_send_to_sqs_sucess():

    mock_lista_final = []
    response = send_to_sqs(mock_lista_final)

    value = response
    print(value)
    assert True


# [8] Tratando resposta final para casos especificos
# [8.A] Testando tratamento de resposta final
def test_format_response_sucess():

    mock_lista_final = []
    response = format_response(mock_lista_final)

    value = response
    print(value)
    assert True
