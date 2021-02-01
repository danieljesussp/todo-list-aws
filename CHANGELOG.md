#Changelog 
All notable changes to this project will be documented in this file. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html). 

## [1.0.0] - 2020-08-05 
### Added
- Versión inicial de código (SAM init)
- Actualizar template.yml con los recursos a crear: funciones, API Gateway, DynamoDB, variables globales. 
- Realizar clase DAO de acceso a la BBDD
- Modificar las funciones en la carpeta "todos"
- Añadir carpetas de terraform y pipelines
- Añadir clase de pruebas TestToDoClass
- Modificar clases de pruebas para que al acceder a la BBDD, invoque a las funciones de la clase DAO