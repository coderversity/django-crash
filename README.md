# Django Crash Course - To-Do List app
Author: Coderversity
YouTube channel: https://youtube.com/@coderversity

This repository contains the source code for building a basic MVT app using Python with Django framework.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Other Commands](#other-commands)

## Introduction

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Getting Started

1. Download and install Python - https://python.org

2. Install Django globalls on your machine:
`pip install django`

3. Open a terminal / command prompt. Navigate to the folder where you want to create your Django project:
`cd folder-name`

4. Create a new Django project:
`django-admin startproject project_name`

5. Change current directory to the new project folder:
`cd project_name`

6. Create a virtual environment so that you can run your project in a localized scope.

If you have Python 3.x installed:
`python3 -m venv venv`

OR if that doesn't work, you can try:
`python -m venv venv`

NOTE: The "python3" command represents the Python version 3.x executable. If you're using a different version, you may need to use the "python[version]" command (e.g. python2 for Python 2.x) or just "python".

7. Activate the virtual environment:
- On a Mac/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

NOTE: If you ever need to deactivate the virtual environment, use this command:
`deactivate`

8. Install Django for this virtual environment:
`pip install django`

NOTEL We recommend running this command again even though you had installed Django globally. At this point, this command will install Django on the virtual environment (venv) to keep the project versions in sync across various devices.

9. Create a requirements.txt file to store package references:
`pip freeze > requirements.txt`

10. Run first migrations to create database tables:
`python manage.py migrate`

This ocmmand will create and update database tables based on the migration files for a particular model. Here, we're just setting up the database with the initial system-generated tables.

11. Run the server:
`python manage.py runserver`

12. Open a browser and view the app at http://localhost:8000

## Other Commands

To create a new Django project:
`django-admin startproject project_name`

To create a new Django app (you can create multiple apps in a project):
`python manage.py startapp app_name`

To build or update database tables and fields for new or updated models (models.py):
`python manage.py makemigrations` then run `python manage.py migrate`

To create a new super user (admin):
`python manage.py createsuperuser`

To open Python  shell (similar to a REPL):
`python manage.py shell`

For a full list of commands, refer to the Django documentation at https://djangoproject.com.
