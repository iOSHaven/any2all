from django.shortcuts import render
from .utils import download

# Create your views here.

def home(request):
    #assert isinstance(request, HttpRequest)
    download.fromUrl("https://images.unsplash.com/photo-1579999284976-73d606de1161", "arandomphoto.png")
    return render(
        request,
        'app/index.html',
        {
            'content':'Home Page',
        }
    )

def convert(request, type1="", type2=""):
    """Renders the home page."""
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/convert.html',
        {
            'from': type1,
            'to': type2
        }
    )