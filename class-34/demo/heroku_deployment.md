# Heroku Deployment

# Locally : 
1- go github clone the template

2- create vertual env & activate it 

3- change the name of the project

4- pip install -r requirements.txt

5- check the requirements then pip install django-cors-headers

6- change the .env name from ```.env.sample``` to ```.env```

7- python manage.py  ```makemigrations```, ```migrate```, ```createsuperuser```,```runserver```

8- go to admin panel change the email/name order from (accounts.admin)

9- SECRET_KEY -> create a new one 
 ```python -c "import secrets; print(secrets.token_urlsafe())"```

10- copy it and paste it in .env file

## Database Deployment:
1- Created an account and a database on https://api.elephantsql.com/

2- We changed the database settings to read from .env

3- We add the required information for online database connection to the .env
in URL :  // ```user``` : ```password``` @ ```host```/ ```dbname```

4- ```pip install psycopg2-binary```
5- ```pip freeze > requirements.txt```

## Server Deployment in Heroku :

1- Install Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

2- Login to Heroku on Browser

3- Login to heroku from terminal using ```heroku login```

4- Create an app on heroku using the following command ```heroku apps:create app-name```

5- Check the local repo is connected with heroku's repo using the following command ```git remote -v```

6- If you did not heroku in the remote so add it using ```heroku git:remote -a app-name```

7- Run ```heroku stack:set container``` 

8- in settings add : ```CSRF_TRUSTED_ORIGINS = tuple(env.list("ALLOWED_ORIGINS"))```
8-  add env variables in heroku settings (add them one by one). 
## collect static files

9- make sure to have this line in settings : 
```STATIC_ROOT = BASE_DIR / "staticfiles"```

8- Run ```python manage.py collectstatic```

9- git add .

10- git commit -m "message"

11- git push heroku main

12 - do A-C-P to Heroku

###  Notes:

-  if you faced ```"Bad Request (400)"``` error :  change DEBUG = True instead of False , complete the steps then return it False.
-  ```"DisallowedHost"``` error :  add the link to allowdhost in heroku env variable (without ```http://``` )
-  ```"forbidden"``` error :
   -  add this line in settings : CSRF_TRUSTED_ORIGINS = tuple(env.list("ALLOWED_ORIGINS"))
   -  add env var -> ALLOWED_ORIGINS add the same value of allowed_host