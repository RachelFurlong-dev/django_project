from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("The line  above on line 2 imports Django’s HttpResponse class so your view can send a response back to the browser. In addition in urls.py,  path('hello/',  index_views.index, name='index'), When you add a path like this to the urls.py file, we are telling Django that when the user inputs this specific URL, it should run the index function within the views.py linked to this path")