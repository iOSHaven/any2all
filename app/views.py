from django.shortcuts import render
from .utils import download
import secrets

# Create your views here.


def home(request):
    # assert isinstance(request, HttpRequest)
    path = download.fromUrl(
        "https://images.unsplash.com/photo-1579999284976-73d606de1161",
        "public/storage/" + secrets.token_urlsafe(32))
    return render(
        request,
        'app/index.html',
        {
            'content': path,
            }
        )


def convert(request, type1="", type2=""):
    """Renders the home page."""
    # assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/convert.html',
        {
            'from': type1,
            'to': type2
            }
        )
