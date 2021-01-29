import json
import os

from todos import decimalencoder
from todos import todoList


def list(event, context):
   
    # fetch all todos from the database
    result = todoList.list_items()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
