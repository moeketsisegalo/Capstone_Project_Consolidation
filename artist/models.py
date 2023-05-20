# Import the models module from Django's database library
from django.db import models

# Define the Album model
class Album(models.Model):
    # Define the title field for the Album model with a maximum length of 100 characters
    title = models.CharField(max_length=100)
    # Define the artist field for the Album model with a maximum length of 100 characters
    artist = models.CharField(max_length=100)
    # Define the release_date field for the Album model as a DateField
    release_date = models.DateField()
    # Define the description field for the Album model as a TextField
    description = models.TextField()

# Define the Tour model
class Tour(models.Model):
    # Define the title field for the Tour model with a maximum length of 100 characters
    title = models.CharField(max_length=100)
    # Define the location field for the Tour model with a maximum length of 100 characters
    location = models.CharField(max_length=100)
    # Define the start_date field for the Tour model as a DateField
    start_date = models.DateField()
    # Define the end_date field for the Tour model as a DateField
    end_date = models.DateField()
    # Define the description field for the Tour model as a TextField
    description = models.TextField()
