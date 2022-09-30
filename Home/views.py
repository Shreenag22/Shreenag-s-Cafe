from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    # return render(request,'about.html', context)
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    # return render(request,'services.html',services)
def contact(request):
    # return render(request,'contact.html',contact)
    return render(request,'contact.html')
