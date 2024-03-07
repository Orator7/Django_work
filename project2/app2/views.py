from django.shortcuts import render
from app2.models import user
from app2 import forms

# Create your views here.
def home(request):
    return render(request,'app2/index.html')

def formName_view(request):
    form = forms.formName()
    return render(request,'app2/form_app.html',{'form':form})