import os
import json

from todos import decimalencoder
from todos import todoList


def get(event, context):
    # Obtencion de la primary key pasada por parametro
    key={
             'id': event['pathParameters']['id']
         }
    # Invocacion a la clase DAO para obtener el componente con ese ID
    result = todoList.get_item(key)
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                          cls=decimalencoder.DecimalEncoder)
    }

    return response
    