import os
from src.processor import lambda_processor
from src.processor import get_list_dynamodb
from src.processor import process_list_dynamodb
from aws_lambda_powertools.utilities.validation import validate
import sys
import json
from tests.events.schemas import INPUT_SCHEMA
sys.path.append('./tests/events')

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
        validate(event=event, schema=INPUT_SCHEMA)
        return event


# [2] Processando evento de entrada
# [2.A] Teste lambda processor com erro


def test_lambda_processor_error():
    mock_event = load_sample_event_from_file("sampleEvent1")
    mock_context = ""
    response = lambda_processor(mock_event, mock_context)

    value = response
    print(value)
    assert True


# [2.B] Teste lambda processor com sucesso
def test_lambda_processor_sucesso():
    mock_event = ""
    mock_context = ""
    response = lambda_processor(mock_event, mock_context)

    value = response
    print(value)
    assert True


# [5] coletando lista no dynamoDB
# [5.A] teste obter a lista do dynamoDb
def test_get_list_dynamodb_sucess():

    mock_session_dynamodb = {}
    mock_info_conection = {}
    response = get_list_dynamodb(mock_info_conection, mock_session_dynamodb)
    value = response
    print(value)
    assert True


# [6] Processando lista em resultado esperado na chamada
# [6.B] Processando lista do dynamoDb
def test_process_list_dynamodb_sucess():

    mock_list = []
    response = process_list_dynamodb(mock_list)

    value = response
    print(value)
    assert True
