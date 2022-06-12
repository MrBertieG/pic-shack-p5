from django.shortcuts import render

def handler_not_found(request, exception):
    return render(request, 'errors/404.html')