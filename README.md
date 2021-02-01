# todo-list-aws

Este es un repositorio de tipo proyecto SAM. Es decir, su funcion principal es el despliegue de una infraestructura que consiste en una base de datos DynamoDB, en un API Gateway y unas funciones lambdas. 
Todo ello, debe de desplegar una aplicación que realizara un CRUD sobre la base de datos. 

## Estructura

Este repositorio consta de cuatro directorios: pipeline, terraform, tests y todos. En la ultima carpeta, se encuentran todos los ficheros cada cual contendrá una de las funciones desarrolladas. 

La estructura actual del repositorio es el siguiente:


```
├── pipeline
│   ├── ENABLE-UNIR-CREDENTIALS
│   │   └── Jenkinsfile
│   ├── PIPELINE-FULL-CD
│   │   └── Jenkinsfile
│   ├── PIPELINE-FULL-PRODUCTION
│   │   └── Jenkinsfile
│   └── PIPELINE-FULL-STAGING
│       └── Jenkinsfile
├── __init__.yml
├── CHANGELOG.md
├── README.md
├── requirements.txt
├── template.yml
├── terraform
│   ├── configure_environment.sh
│   ├── main.tf
│   ├── outputs.tf
│   ├── resources
│   │   └── get-ssh-key.sh
│   ├── variables.tf
│   └── var.tfvars
├── test
│   ├── TestToDo.py
|   ├── TestToDoClass.py
|   ├── README.md
|   ├── requirements.txt
│   ├── ToDoCreateTable.py
│   ├── ToDoDeleteItem.py
│   ├── ToDoGetItem.py
│   ├── ToDoListItems.py
│   ├── ToDoPutItem.py
│   └── ToDoUpdateItem.py
└── todos
    ├── create.py
    ├── decimalencoder.py
    ├── delete.py
    ├── get.py
    ├── list.py
    ├── requirements.txt
    ├── todoList.py
    ├── todoTable.py
    ├── __init__.py
    ├── translate.py
    └── update.py
```

Directorios a tener en cuenta:
 - pipeline: en este directorio el alumno deberá de persistir los ficheros Jenkinsfile que desarrolle durante la práctica. Si bien es cierto que es posible que no se puedan usar directamente usando los plugins de Pipeline por las limitaciones de la cuenta de AWS, si es recomendable copiar los scripts en groovy en esta carpeta para su posterior corrección. Se ha dejado el esqueleto de uno de los pipelines a modo de ayuda, concretamente el del pipeline de PIPELINE-FULL-STAGING. 
 - test: en este directorio se almacenarán las pruebas desarrolladas para el caso práctico.
 - terraform: en este directorio se almacenan los scripts necesarios para levantar la infraestructura necesaria para el apartado B de la práctica. Para desplegar el contexto de Jenkins se ha de ejecutar el script de bash desde un terminal de linux (preferiblemente en la instancia de Cloud9). Durante el despliegue de la infraestructura, se solicitará la IP del equipo desde donde se va a conectar al servidor de Jenkins. Puedes consultarla previamente aquí: [cualesmiip.com](https://cualesmiip.com)
 - todos: en este directorio se almacena el código fuente de las funciones lambda con las que se va a trabajar

## Configuración

De cara a simplificar el despliegue, simplemente habría que ejecutar

```bash
sam build
sam deploy
```

Se puede crear, lista, coger, actualizar y borrar una tarea, ejecutando los siguientes comandos `curl` desde la línea de comandos del terminal:
### Crear una tarea

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos --data '{ "text": "Learn Serverless" }'
```

No hay salida

### Listar todas las tareas

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos
```

Ejemplo de salida:
```bash
[{"text":"Deploy my first service","id":"ac90feaa11e6-9ede-afdfa051af86","checked":true,"updatedAt":1479139961304},{"text":"Learn Serverless","id":"206793aa11e6-9ede-afdfa051af86","createdAt":1479139943241,"checked":false,"updatedAt":1479139943241}]%
```

### Coger una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

Ejemplo de salida:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":false,"updatedAt":1479138570824}%
```

### Actualizar una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id> --data '{ "text": "Learn Serverless", "checked": true }'
```

Ejemplo de salida:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%
```

### Borrar una tarea

```bash
# Replace the <id> part with a real id from your todos table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

No output

## Escalado

### AWS Lambda

Por defecto, AWS Lambda limita el total de ejecuciones simultáneas en todas las funciones dentro de una región dada a 100. El límite por defecto es un límite de seguridad que le protege de los costes debidos a posibles funciones desbocadas o recursivas durante el desarrollo y las pruebas iniciales. Para aumentar este límite por encima del predeterminado, siga los pasos en [Solicitar un aumento del límite para las ejecuciones simultáneas] (http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

Cuando se crea una tabla, se especifica cuánta capacidad de rendimiento provisto se quiere reservar para lecturas y escritos. DynamoDB reservará los recursos necesarios para satisfacer sus necesidades de rendimiento mientras asegura un rendimiento consistente y de baja latencia. Usted puede cambiar el rendimiento provisto y aumentar o disminuir la capacidad según sea necesario.

Esto se puede hacer a través de los ajustes en el `serverless.yml`.
```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```
