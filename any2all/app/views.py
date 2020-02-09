from django.shortcuts import render

# Create your views here.

def home(request):
    #assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'content':'Home Pages',
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