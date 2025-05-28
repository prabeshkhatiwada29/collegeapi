from django.http import HttpResponse



def home_page(request):
    print("Home page accessed")
    return HttpResponse("Welcome to the College API Home Page")