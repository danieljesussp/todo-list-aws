import boto3
from botocore.exceptions import ClientError
import time
from todos import todoList


def put_todo(text, id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('todoTable')
    timestamp = str(time.time())

    try:
        Item={
            'id': id,
            'text': text,
            'checked': False,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }
    
        response = todoList.put_item(Item)

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def main():
    todo = put_todo("The Big New todo task",
                    "123e4567-e89b-12d3-a456-426614174000")
    if todo:
        return todo


if __name__ == '__main__':
    main()
