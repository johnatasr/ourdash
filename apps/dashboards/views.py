from django.shortcuts import render

def dashboard(request):
    template_name = 'dash1.html'
    return render(request,template_name)