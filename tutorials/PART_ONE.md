# Django Tutorial - Part One

✍ Arjun Adhikari, 2 Dec 2020

Steps:

1. Create a directory. 
	`mkdir '$MY_DIR_NAME'`.
2. Navigate to that directory.  
	`cd $MY_DIR_NAME`.
3. Setup a virtual environment inside the directory.
	`python -m venv .env`
	Here, `.env` is name of virtual environment. You can name it as you like. 
	But I started with period `.` so it gets listed at top in explorer view of IDEs and makes easier to explore through project files.
4. Activate the virtual environment.
	`.env\Scripts\activate`
5. Install django library.
	`pip install django`
6. Create a django project.
	`django-admin startproject my_project .`
	Here `my_project` is the name of the django project and `.` makes project files accessible in current working directory.
7. Test the installation.
	`python manage.py runserver`
8. Now you've django setup on your system. Let's start making modular apps.
Break the running server with `Ctrl + C` and type the following command:
	`python manage.py startapp blog`
	Here `blog` is name of the project.
	The project structure looks like following inside the `blog` application.
	```
	blog
	└───────├── admin.py
		├── apps.py
		├── __init__.py
		├── migrations
		│   └── __init__.py
		├── models.py
		├── tests.py
		└── views.py
	```

	Don't worry, pal. I will be guiding you through each of the files.

	Each app has a `__init__`.py file identifying it as a Python package. There are 6 new  
	files created:  
	• `admin.py` is a configuration file for the built-in Django Admin app.  
	• `apps.py` is a configuration file for the app itself.  
	• The `migrations` directory stores migrations files for database changes.  
	• `models.py` is where we define our database models.  
	• `tests.py` is for our app-specific tests.  
	• `views.py` is where we handle the request/response logic for our web app.  
	Typically developers will also create an `urls.py` file within each app too for routing.

9. Let's register the newly created app  into the `INSTALLED_APPS` inside the `settings.py`. 
	```

	# my_project/settings.py
	# ======================
	
	INSTALLED_APPS  = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'blog',
	]
	``` 
	Please take care of the indentation and don't forget to provide comma as writing comma will help to ignore error at near future.
10. After adding the app to `INSTALLED_APPS`, let's start to code some logic into the `blog` app we created earlier.
	```
	# blog/views.py
	# ==============
	
	from django.shortcuts import render

	import random

	def  guess_luck(request):
	
		guess = random.randint(3,6)
		user_guess =  4
		luck =  False
		if user_guess == guess:
		luck =  True
		context = {
			'result': luck
		}
		return render(
			request,
			'blog/index.html',
			context
		)
	```
	We've created a logic where an arbitary number `4` tries to match to with the random number from `3 to 6` and if they got matched, the luck variables is assigned to `True` else `False`.
	
11.  Notice the `'blog/index.html'` inside the render function, which refers to the template file location where this reponse will be displayed. Till now, we've not created any temlate directory nor template (HTML) file to display the response. But, first we need to tell Django where to look for our template files.
For doing so, 
```
# my_project/settings.py
#========================

TEMPLATES  = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			'templates', # Modification here
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]
```

By mentioning the folder inside `DIRS` list, we're telling django to look for templates inside `templates` directory. By default, Django looks for templates inside all the path mentioned inside `DIRS` list. So, be careful while modifying the list.

12. Now, create a `templates` directory inside `blog` directory. 
	`cd blog && mkdir templates`
13. Again, create a directory named `blog` inside `templates` directory we recently created and create a file named `index.html`  inside the `blog` directory where we will write HTML.
	`mkdir blog`
14. It's time to write some HTML, pal.
	```
	# blog/templates/blog/index.html
	#=================================
	
	<!DOCTYPE  html>
	<html  lang="en">
	<head>
		<meta  charset="UTF-8">
		<meta  name="viewport"  content="width=device-width, initial-scale=1.0">
		<title>Guess luck</title>
	</head>
	<body>
		Your luck is {{result}} today.
	</body>
	</html>
	```
	Notice the `{{result}}`  inside `<body>` tag. It is the context value passed from `blog/views.py` through `render` function.

15. Now, let's setup URL configuration for our project. 
	
	```
	# my_project/urls.py
	#====================
	
	from django.contrib import admin
	from django.urls import path, include
	  
	urlpatterns = [
		path('admin/', admin.site.urls),
		path('blog/', include('luck.urls')),
	]
	```
	For routing url routes to our app `blog`, let's include all the URL routes starting from `blog/` to the `urls.py` of `blog` app. Notice the quotes sourrounding `'luck.urls'` inside include function.
	 But, something seems fishy.
There is no `urls.py` inside `blog` app. Alright, let's create one.
After creating `urls.py` inside `blog` app. The URL request get routed to our app. Now, let's make our app handle the URL routes with the function and templates we created recently.

	```
	# blog/urls.py
	#====================
	from django.urls import path

	from .views import guess_luck

	urlpatterns = [
		path('', guess_luck)
	]
	```
	This will route `/blog/` request from browser to `guess_luck` view and that will render `blog/index.html`. So easy, right ?
Let's run the server if it works.
`python manage.py runserver`

![Output](https://i.imgur.com/UV90WXX.png)

That's what we expected. The mighty luck checker that will save the planet one day.

