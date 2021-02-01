import boto3
import os

dynamodb = boto3.resource('dynamodb')

#crear recurso de acceso a la base de datos con el nombre de la tabla definida en template.yml
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

#Funcion de insertar en la BBDD. Se le pasa como valor el componente que se desea insertar
def put_item(itemValue):
    table.put_item(Item=itemValue)

#Funcion de obtencion un componente. Para ello se le pasa como valor la primaryKey (en nuestro caso el ID) y devuelve el componente entero
def get_item(idValue):
    result = table.get_item(Key=idValue)
    return result

#Funcion de actualizacion de un componente. Para ello, se le debe de pasar la primaryKey(id), variable JSON con los datos a actualizar (text, checked o ambos) y el timestamp     
#Devuelve el componente actualizado
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

# Funcion para borrar un componente. Para ello, se le pasa la PrimaryKey (ID)    
def delete_item(idValue):
    table.delete_item(Key=idValue)

#Funcion de obtencion de todos los componentes de la tabla
def list_items():
    result = table.scan()
    return result