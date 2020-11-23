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

![home page](https://user-images.githubusercontent.com/58456645/99963073-38ca9e00-2db7-11eb-9e3d-af310221b29f.PNG)

---------------------------------------------------------

Create a super User ( admin user)

>> python manage.py createsuperuser

Login to admin panel using credentials

URL : http://127.0.0.1:8000/admin/

----------------------------------------------------------
Register URL: http://localhost:8000/admin-panel/register/

![signup](https://user-images.githubusercontent.com/58456645/99963149-5c8de400-2db7-11eb-9062-a7bf7f302dde.PNG)



Login URL: http://localhost:8000/admin-panel/login/

![login manager](https://user-images.githubusercontent.com/58456645/99963252-7fb89380-2db7-11eb-9cde-45b61e9343a6.PNG)


----------------------------------------------------------
You will be redirected to : 
http://localhost:8000/admin-panel

![dashboard home](https://user-images.githubusercontent.com/58456645/99963416-c4dcc580-2db7-11eb-876c-f3e53547725f.PNG)

----------------------------------------------------------

Add Employee , View Employee, Delete Employee, Edit Employee details :

http://localhost:8000/admin-panel/emp-list/

![list](https://user-images.githubusercontent.com/58456645/99963659-19804080-2db8-11eb-8e4e-fb3000979e7e.PNG)

![update](https://user-images.githubusercontent.com/58456645/99963666-1b4a0400-2db8-11eb-8fdb-e1e4ca009b07.PNG)

![delete emp](https://user-images.githubusercontent.com/58456645/99963668-1be29a80-2db8-11eb-91ca-e6cc47ee9d92.PNG)

----------------------------------------------------------

Swagger UI : 
http://localhost:8000/s





