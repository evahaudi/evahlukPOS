# For new environment
virtualenv venv
./venv/Scripts/activate
pip install django
pip install djangorestframework
pip install psycopg2
python -m pip install Pillow #added thes
# pip install django-postgresql
pip install django-cors-headers
# npm install
npm install react-scripts --force
# or pip install django djangorestframework psycopg2 django-cors-headers
cd .\back-end\
python manage.py makemigrations
python manage.py migrate
cd ..



# For running front end
cd .\front-end\evahlukpos\
npm start

# For running back end
cd .\back-end\
python manage.py runserver

# Random fixes