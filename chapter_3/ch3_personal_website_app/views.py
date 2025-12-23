from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello world!")

def about_page_view(request):
    return render(request, "personal_website_app/about.html")

def context_page_view(request):
    context = {"name": "Daniel",
               "job": "Successful indie game dev and business owner"}
    return render(request, "personal_website_app/context.html", context)