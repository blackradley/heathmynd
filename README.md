# Project: Heathmynd - Culture Mapping

The museum data (including name and location) is gathered from Wikipedia
Data is held in a Google Fusion table or KML file and displayed on a Google
Map on web pages hosted on the Google App Engine.

## To set up

* Delete .c9 and README.md
* git clone https://github.com/blackradley/heathmynd.git ./
* gem install jekyll bundler
* bundle install

## Install or Update GAE on C9

* Alt-T
* cd ..
* rm -r google_appengine
* wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.65.zip
* unzip google_appengine_1.9.65.zip
* rm google_appengine_1.9.65.zip 

## Run Google App Engine

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

## Django web_app

### Starting the web_app

django-admin startproject web_app
cd web_app
python manage.py startapp cheltenham
python manage.py startapp cornwall
python manage.py startapp southwest

### Check the django version

manage.py --version

    1.11.16

### Run the Django server

python manage.py runserver 8080

