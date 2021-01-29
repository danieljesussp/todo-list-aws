import json
import time
import logging
import os

from todos import decimalencoder
import boto3
from todos import todoList

def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = int(time.time() * 1000)
    
    Key={
            'id': event['pathParameters']['id']
        }

    # update the todo in the database
    result = todoList.update_item(Key, data, timestamp)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
