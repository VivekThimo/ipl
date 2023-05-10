from django.shortcuts import render

# Create your views here.
def rile(request):
    return render(request,'CSK/index.html')