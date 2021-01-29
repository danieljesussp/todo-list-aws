import os
from todos import todoList


def delete(event, context):
    
    Key={
            'id': event['pathParameters']['id']
        }

    # delete the todo from the database
    todoList.delete_item(Key)

    # create a response
    response = {
        "statusCode": 200
    }
    
    

    return response
