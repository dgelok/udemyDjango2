from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

def index (request):
    my_dict = {'insert_me': "Hello, I'm from first_app/index.html. I'm passed as a value of a key in an object."}
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def about (request):
    return HttpResponse("Here's our about page")

def contact(request):
    return HttpResponse("<h1>CONTACTS</h1>")
# Create your views here.
