from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict= {'insert_me': 'Now I am coming from polls/index.html '}
    return render(request,'polls/index.html',context=my_dict)
