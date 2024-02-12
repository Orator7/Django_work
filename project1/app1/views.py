from django.shortcuts import render

# Create your views here.

def home(request):
    my_dict = {"insert_content":"I am from views of app1"}
    return render(request,"app1/index.html",context=my_dict)