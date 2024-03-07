from django.shortcuts import render
from app1.models import Topic,Webpage,AccessRecord

# Create your views here.

def home(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    date_list ={"insert_content":"I am from views of app1",'access_record':Webpages_list,}
    
    my_dict = {}
    return render(request,"app1/index.html",context=date_list)