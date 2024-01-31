# Terra Tracer Backend

## Virtual Environment

Python 3.8

## Install dependencies

`python -m pip install -r requirements.txt`

## Deploy

`python manage.py runserver`

The command will start the server on port 8000.
Then you can access the admin page (localhost:8000/admin) to manage the database using username **admin** and password **terratracer**

APIs available:

```
    /map/add-location/      map.views.AddLocation   
    /map/get-locations/<int:uid>/   map.views.LocationList  
    /user/<int:pk>/ user.view.UserDetail    user-detail
    /user/list/     user.view.UserList      user-list
```


## Migrate Tables

- `python manage.py makemigrations [app name]`

if *app name* is not specified, all models in every apps will be migrated.

- `python manage.py migrate`

## Related Documentations

[Django](https://docs.djangoproject.com/en/4.2/)

[Django Rest Framework](https://www.django-rest-framework.org)




