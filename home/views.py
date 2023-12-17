from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/index.html")

def about(request):
    return render(request,"home/about.html")

def index(request):
    return render(request,"home/index.html")

def frequently_asked_questions(request):
    return render(request,"home/faq.html")

def contact(request):
    return render(request,"home/contact.html")