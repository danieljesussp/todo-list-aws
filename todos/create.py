import json
import logging
import os
import time
import uuid
from todos import todoList


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(time.time())

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    todoList.put_item(item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    

    return response
