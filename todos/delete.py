import os
from todos import todoList


def delete(event, context):
    # Obtencion de la primary key pasada por parametro
    Key={
            'id': event['pathParameters']['id']
        }

    # Invocacion a la clase DAO para eliminar el componente con ese ID
    todoList.delete_item(Key)

    # create a response
    response = {
        "statusCode": 200
    }
    
    

    return response
