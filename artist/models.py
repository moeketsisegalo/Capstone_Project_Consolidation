from django.db import models

class Album(models.Model):
    """
    Album model representing an album.
    
    :param title: The title of the album.
    :type title: str
    :param artist: The artist of the album.
    :type artist: str
    :param release_date: The release date of the album.
    :type release_date: datetime.date
    :param description: The description of the album.
    :type description: str
    """
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()

class Tour(models.Model):
    """
    Tour model representing a tour.
    
    :param title: The title of the tour.
    :type title: str
    :param location: The location of the tour.
    :type location: str
    :param start_date: The start date of the tour.
    :type start_date: datetime.date
    :param end_date: The end date of the tour.
    :type end_date: datetime.date
    :param description: The description of the tour.
    :type description: str
    """
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()