# Base-Template

The Base Template is a Django project template that serves as a starting point for your web application. This readme file provides instructions on how to set up and run the Base Template. Please follow the steps below:

## Prerequisites
- Python (version 3.6 or higher) and pip installed on your system.
- Django framework (version 3.2 or higher) installed.

## Installation and Setup

1. Clone the repository to your local machine:
git clone https://github.com/your-username/base-template.git


2. Navigate to the project's root directory:
cd base-template

3. Install the project dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py makemigrations home
python manage.py migrate

5. Fill data in the SuscriptorType and SocialApp tables:

python fill_data.py

6. Create a superuser for administrative access:

python manage.py createsuperuser


7. Add a localhost site to the database:

python manage.py shell

Once the Django shell opens, enter the following commands:
from django.contrib.sites.models import Site

Site.objects.create(domain='localhost', name='localhost')
exit

## Running the Application

To start the Base Template server, use the following command:

python .\manage.py runserver 0.0.0.0:7777

You can now access the application by opening your web browser and navigating to http://localhost:7777/.

## Administration

To access the admin panel, open your web browser and go to http://localhost:7777/admin/. Log in using the superuser credentials you created earlier.

That's it! You have successfully set up and launched the Base Template. Feel free to modify the code and customize the project according to your needs.

## To start an app
Following the project structure you need to place the apps inside the folder mf6. For example if i want to create the app called hatariutils, i need to first create the sub folder hatariutils inside mf6:

mkdir mf6/hatariutils

Then i have to run the following command

python manage.py startapp hatariutils mf6/hatariutils

