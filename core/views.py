from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/html/home.html',{'home':'active'})
def contact(request):
    return render(request, 'core/html/contact.html', {'contact':'active'})
