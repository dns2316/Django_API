# Django-API

* install django

(for anaconda or pip)

`conda install -c anaconda django`

* create django project

`django-admin startproject mysite`

* run server

`python manage.py runserver`

===

Create model

* Write fields in app//models.py
* Then add nameapp.apps.NameappConfig to /settings.py
* Make migrations of app models

`python manage.py makemigrations polls`

* If need, can edit some in models in nameapp/migrations/0001_initial.py
* Then make SQL code follow command python manage.py sqlENGINE NAMEapp migration_NUMBER

`python manage.py sqlmigrate nameapp 0001`

* Send models/tables to database

`python manage.py migrate`

*Official doc.*

*Migrations are very powerful and let you change your models over time,*
*as you develop your project, without the need to delete your database or*
*tables and make new ones - it specializes in upgrading your database live,*
*without losing data. We’ll cover them in more depth in a later part*
*of the tutorial, but for now, remember the three-step* 
guide to making model changes:*

* Change your models (in models.py).
* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.

___

### For auth users make app


custom auth users
`https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#a-full-example`