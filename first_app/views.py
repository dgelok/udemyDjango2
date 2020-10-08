from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    my_dict = {'insert_me': "Hello, I'm from first_app/index.html"}
    return render(request, 'first_app/index.html', context=my_dict)

# def about (request):
#     return HttpRequest("Here's our about page")

# def contact(request):
#     return HttpRequest("<h1>CONTACTS</h1>")
# Create your views here.
