import os
import json

from todos import decimalencoder
from todos import todoList


def get(event, context):
    
    key={
             'id': event['pathParameters']['id']
         }
    
    result = todoList.get_item(key)
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                          cls=decimalencoder.DecimalEncoder)
    }

    return response
    