from django.shortcuts import render


# Simply index html page view
def index(request):
    return render(request, 'pages/index.html')
