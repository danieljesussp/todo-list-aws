import boto3
from botocore.exceptions import ClientError
import time
from todos import todoList


def update_todo(text, id, checked, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")


    timestamp = str(time.time())

    try:
        # Creacion de la variable data con los nuevos atributos
        data = {
            'text': text,
            'checked': checked
        }
        # Creacion de la variable de la PrimaryKey
        Key = {
            'id': id
        }
        # Invocacion a la clase DAO para actualizar
        # el componente con ese ID y esos nuevos datos
        response = todoList.update_item(Key, data, timestamp)

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def main():
    todo = update_todo(
        "Aprender DevOps y Cloud en la UNIR",
        "123e4567-e89b-12d3-a456-426614174000",
        "false")
    if todo:
        return todo


if __name__ == '__main__':
    main()
