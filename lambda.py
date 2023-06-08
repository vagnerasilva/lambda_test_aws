from src.processor import lambda_processor

# [1] Entrada do evento da lambda
def lambda_handler(event,context):
    """
    Lambda Entry Point
    """
    response = lambda_processor(event, context)

    return response


