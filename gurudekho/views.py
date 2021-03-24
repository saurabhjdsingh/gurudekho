def index(request):
    return render(request, 'index_new.html')


def contact(request):
    return render(request, 'contact-us.html')


def about(request):
    return render(request, 'about.html')
    

def terms(request):
    return render(request, 'terms.html')
    
    
def privacy(request):
    return render(request, 'privacy.html')
