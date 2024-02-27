from django.shortcuts import render

# Create your views here.

def server(request):
    return render(request, 'hello_world.html', {})