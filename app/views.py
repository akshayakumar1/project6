from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'x':34,'y':118,'z':45}
    return render(request,'jinja.html',d)
    
