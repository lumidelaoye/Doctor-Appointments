# Appointment manager
A Doctor's appointment management app built with Django

## Steps to run this application
cd into the project directory 'assessment'

### Running with Docker
You will need to have Docker installed on your computer

Run the command below

docker-compose up -d

Now, application should be running on port 8000

Go to http://localhost:8000/api/v1/swagger or http://localhost:8000/api/v1/redoc on your browser to access the project's documentation. The documentation contains detailed instructions on how to test each api endpoint.

you can also access the admin interface on http://localhost:8000/admin - NB you need to create a super user first using python manage.py createsuperuser
