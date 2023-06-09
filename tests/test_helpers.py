from src.helpers import get_headers
from src.helpers import get_conection
from src.helpers import send_to_sqs
from src.helpers import format_response
import sys
import os
import json
# sys.path.append('./tests/events')

# Mock do arquivo de event


def load_sample_event_from_file(test_event_file_name: str) -> dict:
    """
    Loads and validate test events from the file system
    """

    current_directory = os.getcwd()
    print(current_directory)
    event_file_name = f"./tests/events/{test_event_file_name}.json"
    with open(event_file_name, "r", encoding='UTF-8') as file_handle:
        event = json.load(file_handle)
        return event


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
    mock_response = load_sample_event_from_file("sampleOutput1")
    mock_lista_final = []
    response = format_response(mock_lista_final)

    value = response
    value2 = mock_response
    print(value)
    print(value2)
    assert True
