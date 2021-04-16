from django.shortcuts import render
from .models import cityinfo


# Create your views here.
def home(request):
    return render(request,'index.html')

def search(request):
    query=request.GET['query']
    if len(query)>60:
        final_content=cityinfo.objects.none()
    else:
        if len(query)>=1:
            final_content=cityinfo.objects.filter(title__icontains=query)

        else:
            final_content = cityinfo.objects.none()

    context={'cityinfo':final_content, 'query':query}
    return render(request,'search.html',context)