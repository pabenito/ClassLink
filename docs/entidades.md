# Entidades

## Usuario 

```
user
    username* : str
    password* : str
    img : URL
    description : str 
    disponibility : schedule
    occupation : schedule
    reports : [report]
    offers : [offer]
    requests : [request] 
    categories : [category]   
```

## Foro

```
forum
    messages : [message]
```

## Chat 

```
chat
    class_id:
    users_ids* : [id]
    messages : [message]
```

## Message

```
message
    date* : datetime
    sender_id* : id
    sender_username* : str
    message* : str
    response_to
```

## Ficheros

``` 
file
    url : URL
```

## Rating

```
rating 
    rate* : int
    date* : datetime
    sender_id* : id
    sender_username* : str
    message : str
```

## Reporte

```
report
    date : date
    description : str
```

## Disponibilidad

```
schedule [
    date: date
    from: time
    to: time
]
```

## Materia

```
subject
    name*: str
    tags: [str]
    !category* 
```

## Category

```
category
    name: str
```

## Oferta

```
offer 
    !subject*
    price : float
    extra_per_student : float
```

## Clase

```
class < offer
    real_schedule : schedule
    students : [id]
    cost : float
    files :  [files]
```






