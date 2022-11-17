# Entidades

## Usuario 

```
user
    username* : str
    password* : str
    img : URL
    description : str 
    disponibility : schedule
    reports : [report]
    offers : [offer]
    requests : [subject] 
    categories : [category]   
    ratings : [rating]
    packs : [pack]
    classes : [class]
    duplicate_commission : bool
```

## Pack

```
pack
    sessions : [session] 
    !subject*
    description* : str
    price* : float
    max_students : int
```

## Sesion

```
session 
    !subject*
    !time_slot*
```

## Reporte

```
report
    date* : date
    description* : str
```

## Planificación

```
schedule 
    weekly : [weekday_slot]
    added : [time_slot]
    removed : [time_slot]
```

## Plafinicación semanal

```
weekday_slot
    week_day: int (0-7)
    from* : time
    to* : time
```

## Franja horaria

```
time_slot 
    date* : date
    from* : time
    to* : time
```

## Materia

```
subject
    name* : str
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
    max_students : int
```

## Peticion

```
request
    !subject*
    price : float
    extra_per_student : float
```

## Clase

```
class
    (!offer | !session)
    real_time_slot : time_slot
    students : [id]
    cost : float
    files :  [files]
    summary : str
    !rating
    !cancellation
```

## Cancelación

```
cancellation
    date : datetime
    user_id : id
```

## Foro

```
forum
    !category
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
    response_to : message
```

## Ficheros

``` 
file
    url : URL
```

## Rating

```
rating 
    date* : datetime
    sender_id : id
    sender_username : str
    message : str
    professionalism : int
    knowledge : int
    clarity : int
```







