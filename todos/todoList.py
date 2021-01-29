import boto3
import os

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def put_item(itemValue):
    table.put_item(Item=itemValue)

def get_item(idValue):
    result = table.get_item(Key=idValue)
    return result
    
def update_item(idValue, data, timestamp):
    result = table.update_item(
        Key=idValue,
        ExpressionAttributeNames={
          '#todo_text': 'text',
        },
        ExpressionAttributeValues={
          ':text': data['text'],
          ':checked': data['checked'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #todo_text = :text, '
                         'checked = :checked, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )
    return result
    
def delete_item(idValue):
    table.delete_item(Key=idValue)

def list_items():
    result = table.scan()
    return result