from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, You're at the polls index")

# detail view
def detail(request, question_id):
    return HttpResponse("youre looking at question %s." % question_id)

 