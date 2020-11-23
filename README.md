install required packages from requirements.txt file

>> pip install -r requirements.txt
----------------------------------------------------------
Create Database For Mysql
& Add your database details in settings.py file OR You can use sqlite database.
----------------------------------------------------------
Apply migrations to create tables in database

>> python manage.py makemigrations

then 
>> python manage.py migrate

----------------------------------------------------------
Run Project using : 

>> python manage.py runserver localhost:8000

Application home page: http://localhost:8000


---------------------------------------------------------

Create a super User ( admin user)

>> python manage.py createsuperuser

Login to admin panel using credentials

URL : http://127.0.0.1:8000/admin/

----------------------------------------------------------
Register URL: http://localhost:8000/admin-panel/register/

Login URL: http://localhost:8000/admin-panel/login/

----------------------------------------------------------

