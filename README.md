# P10

The goal of this project was to create a secure API using Django REST.


# Introduction

This project is composed of:
* A registration page + login
* JWT authentication
* Custom permissions


# Requirements

* Python3 at https://www.python.org/downloads
* ... and that's it !


# Installation

## Step 1: Acquire the codebase

### Using Git Desktop
With the desktop app, simply click on the "Code" (green button) at the top of this page and then "Open with GitHub Desktop".

Clone the file to desired location and you're done !

### Using Git Console
Navigate to desired location and use:
```
git clone https://github.com/Dhyakia/OPC_Project10.git
```

### Using the manual download
Click on the "Code" (green button) at the top of this page and then "Download Zip"

Un-zip the file into the desired location and you're done !

## Step 2: Setting up a virtual environement

For a better user experience, it is recommanded to use a virtual environnement.

1. With the console, navigate to the folder of installation.

2. Next, to create the environnement, enter this command:
    
    Windows: ```python -m venv venv ```

    MacOs/Linux: ```python -m venv venv ```

3. Now, all that's left if to activate it:

    Windows: ```venv/scripts/activate```

    MacOs/Linux: ```venv/bin/activate```

If everything is done correctly, you should now see the "venv" tag at the start of the line of the console.

## 3. Install the dependencies

Using the console, navigate to the project folder and enter:
```
pip install -r requirements.txt
```

## 4. First launch: setting up the database

Using the console, navigate inside the LITReview folder, where the manage.py file is and enter:
```
python manage.py migrate
```

Congratulation, you're now all setup for using the application !

# Usage

## Starting the server
Activate the virtual environnement.


Using the console, navigate inside the LITReview folder, and enter:

```
python manage.py runserver
```

## Navigatin the endpoints:

There is multiple ways to navigate the API, i choosed to use POSTMAN instead of the pre-integred REST tool.

Link to the POSTMAN depo can be found here : [LINK TO POSTMAN DEPO]


# Futur viewing

This is the tenth out of thirteen python project with OpenClassRoom