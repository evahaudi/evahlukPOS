# For new environment
virtualenv venv
./venv/Scripts/activate
### pip install django
### pip install djangorestframework
### pip install psycopg2
### pip install django-postgresql
### pip install django-cors-headers

pip install django djangorestframework psycopg2 django-cors-headers
python -m pip install Pillow #added this
npm install
### npm install react-scripts --save
cd .\back-end\
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# For running front end
cd .\front-end\evahlukpos
npm start

# Random fixes