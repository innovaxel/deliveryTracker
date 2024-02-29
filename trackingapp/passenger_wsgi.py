import os
import sys

# Assuming your Django project's directory is one level up from this file
current_directory = os.path.dirname(__file__)
project_directory = os.path.join(current_directory, 'trackingapp')

# Add the project directory to the sys.path
sys.path.append(project_directory)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'trackingapp.settings'

# Import the Django application
from django.core.wsgi import get_wsgi_application

# Create a WSGI application object
application = get_wsgi_application()