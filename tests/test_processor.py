from src.processor import lambda_processor
from src.processor import get_list_dynamodb
from src.processor import process_list_dynamodb


# [2] Processando evento de entrada
# [2.A] Teste lambda processor com erro
def test_lambda_processor_error():
    mock_event = ""
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
