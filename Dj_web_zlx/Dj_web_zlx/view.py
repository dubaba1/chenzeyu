from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello !'
    return render(request, 'hello.html')
def base(request):
    context = {}
    context['hello'] = 'Hello !'
    return render(request, 'base.html')

