from django.shortcuts import render

# Create your views here.
def jinjaoperations(request):
    d={'a':100,'b':200}
    return render(request,'operational_htmlpage.html',context=d)
