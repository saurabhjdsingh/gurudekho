from django.shortcuts import render
from dashboard.models import faq

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact-us.html')


def about(request):
    faqs = faq.objects.all().order_by('-id')
    if faqs:
        return render(request, 'about.html', {'faq':faqs})
    else:
        return render(request, 'about.html')
    

def terms(request):
    return render(request, 'terms.html')
    
    
def privacy(request):
    return render(request, 'privacy.html')

def error_404(request, exception):
    data = {}
    return render(request, 'error/error_404.html', data)
    
def error_403(request, exception):
    data = {}
    return render(request, 'error/error_403.html', data)
    
def error_400(request, exception):
    data = {}
    return render(request, 'error/error_400.html', data)
 