import os
import json

from todos import decimalencoder
from todos import todoList
import boto3


def translate(event, context):
    #Obtencion del id pasado en la URL
    Key={
            'id': event['pathParameters']['id']
        }
    
    # Obtencion del componente entero
    # fetch todo from the database
    result = todoList.get_item(Key)
    
    print(result)
    itemJson = json.dumps(result['Item'],cls=decimalencoder.DecimalEncoder)
    # Invocacion de la api de comprehend
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    jsoncomprehen = json.loads(itemJson)

    langsourceJson=comprehend.detect_dominant_language(Text=jsoncomprehen['text'])
    print(langsourceJson)
    langSource=langsourceJson['Languages'][0]['LanguageCode']

    print(langSource)
    targetLanguage={
        'lang': event['pathParameters']['lang']
    }
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

    resultTranslate = translate.translate_text(Text=jsoncomprehen['text'], 
        SourceLanguageCode=langSource, TargetLanguageCode=targetLanguage['lang'])
    
    jsoncomprehen['text'] = resultTranslate['TranslatedText']

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(jsoncomprehen)
    }

    return response
