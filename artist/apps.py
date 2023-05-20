from django.apps import AppConfig

class ArtistConfig(AppConfig):
    """
    AppConfig for the 'artist' app.

    :param: None
    :type: None
    :return: None
    :rtype: None
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist'
