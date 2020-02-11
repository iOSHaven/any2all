from requests import get
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def fromUrl(url, path):
    """Download a file from http/s url and place the contents in a file.
    
    Arguments:
        url {string} -- the url of the file
        path {string} -- the storage path
    
    Returns:
        string -- the path of the file
    """
    response = get(url)
    file_name = default_storage.save("storage/" + path, ContentFile(response.content))
    return default_storage.url(file_name)
