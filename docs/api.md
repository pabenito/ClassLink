# API

De cada llamada a la API se especificará su funcionalidad y argumentos, si los tiene.

## Sintaxis

Los argumentos seguirán la siguiente notación:

- argumento del body
- {argumento del path}
- ?argumento query
- argumento opcional~valor por defecto (argumento~ = argumento~None)
- argumento (tipo de dato)

## Tipos

Hay dos tipos de datos, datos básicos y compuestos (objetos).

Los tipos básicos usados son:

- **str**: Cadena de texto.
- **int**: Número entero.
- **date**: Fecha (año, mes y día).
- **time**: Tiempo (hora, minuto y segundo).

Los tipos compuestos (el resto) se pueden consultar en [entidades](entidades.md).

## Entidiades

**Raiz**: localhost:8000

### Usuarios

**Endpoint** /users
**URL**:  http://localhost:8000/users

- **GET /users**: Devuelve los usuario que cumplen con los filtros especificados.
    - ?_username_(str): El nombre de usuario.
    - ?_classes_(str): Mínimo número de clases impartidad como profesor.
    - ?_category_(str): Categoría en la que ofrece clases.
    - ?_score_(float): Mínimo score del profesor.
- **POST /users**: Añade un nuevo usuario.
    - _username_(str): Nombre de usuario con el que se identificará.
    - _password_(str): Contraseña con la que iniciará sesión.
    - _first\_name_(str): Nombre de la persona.
    _ _last\_name_(str): Contraseña con la que iniciará sesión.
- **PUT /users**: Actualiza al usuario con nuevos datos.
    - _img_(URL)~: Foto de perfil del usuario. 
    - _description_(str)~: Descripción del usuario. 
    - _disponibility_(schedule)~: Disponibilidad para impartir/recibir clases. 
    - reports : [report]
    - offers : [offer]
    - requests : [subject] 
    - categories : [category]   
    - ratings : [rating]
    - packs : [pack]
    - classes_as_student : [class]
    - classes_as_teacher : [class]
    - duplicate_commission : bool


