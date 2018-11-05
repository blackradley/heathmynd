# Project: Heathmynd - Culture Mapping

The museum data (including name and location) is gathered from Wikipedia.
Data is held in a Google Fusion table or KML file and displayed on a Google Map on web pages hosted on the Google App Engine.
GAE supports Python 3 but you still have to have Python 2 to run the GAE locally so there doesn't seem to be a lot of point in upgrading.

## Data Gathering Application

Uses Python 2.7 like the GAE.



## Django web_app

WARNING: If you are coming from ASP.NET or RoR, in Django views are what you call controllers and templates are what you call views.

### Creating the web_app

For reference of what was done, not what you need to do.

    django-admin startproject web_app
    cd web_app
    python manage.py startapp cheltenham
    python manage.py startapp cornwall
    python manage.py startapp southwest

### Check the django version

To remind yourself what documentation you should be reading.

    manage.py --version
        1.11.16

### Install the Requirements

So they are locally available to the Google App Engine.  The Google App Engine no longer provides packages support for 

    pip install --target ./web_app/lib/ --requirement ./web_app/requirements.txt 

### Run the dev server

    python manage.py runserver 8080
or

    web_dev_server_django.cmd

### Run Google App Engine

To run on Cloud9 use:

    ``` python ../google_appengine/dev_appserver.py ./web_app/src/ --enable_host_checking=false ```
    
To run on Cloud9 with access to the admin interface use:
    
    ``` python ../google_appengine/dev_appserver.py ./web_app/src/ --enable_host_checking=false --admin_port=8081 ```

* Check: http://heathmynd.appspot.com/
* Update Command: appcfg.py update WebApp
* Rollback Command: appcfg.py rollback WebApp

## Fusion Tables

* At: http://www.google.com/fusiontables/DataSource?dsrcid=586076
* http://www.google.com/fusiontables/DataSource?dsrcid=614442