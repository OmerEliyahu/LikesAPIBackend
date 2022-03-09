To Run the app you have to have python3.9 installed on your computer.
Clone the git repo to your local PC.
install virtualenv via pip install virtualenv
Create new virtual environment: virtualenv environment_name -p
Open the virtual environment: source environment_name/bin/activate
Install the dependencies: pip install -r requirements.txt
To run the project first run: python manage.py migrate
Python manage.py runserver
To flush the DB and get new photos run: python manage.py migrate api zero
And :python mange.py migrate
