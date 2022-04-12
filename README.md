# project-awwards

>[Mercy-Bore](https://github.com/macc254)  
  
# Description  
This project allows users to post their projects for other users to rate according to design, usability and content.
##  Live Link  
 Click [here](https://mercy-awwwards.herokuapp.com/) to visit the site.
  
## Screenshots 
###### Home page
![1awwward](https://user-images.githubusercontent.com/61621637/162891913-c0e3ea64-0ea4-4aee-8c72-133e73d5533a.png)


 
###### Rating of a post

![2](https://user-images.githubusercontent.com/61621637/162690309-850c6a3d-72b6-4bcc-a32b-f242b639a0b9.png)

 
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/macc254/awwwards-projects.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd awwwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
 python3 -m venv venv - source bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 ### Api Endpoints
- https://mercy-awwwards.herokuapp.com/api/projects/
- https://mercy-awwwards.herokuapp.com/api/profiles/
- https://mercy-awwwards.herokuapp.com/api/users/
 
## Technology used  
  
* [Python3.8.10](https://www.python.org/)  
* [Django 4.0.3](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
 
  
## Contact Information   
If you have any question or contributions, please email me at [mercycherotich757@gmail.com]  
  
## License 
[License](https://github.com/macc254/awwwards-projects/blob/master/LICENSE)  
* Copyright (c) 2022 **Mercy Bore**
