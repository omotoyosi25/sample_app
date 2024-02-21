from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    name="habibat"
    courses=['backend', 'frontend', 'product design', 'data science', 'cloud development']
    context={
        'n':name,
        'course_list':courses
    }
    return render(request,  "app1/index.html", context)


# def me_page_view(request):
#     age="10yr old"
#     return render(request, "index2.html", {"age":age})

def about_page_view(request):
    return render(request, "app1/about.html")

def contact_page_view(request):
    return render(request, "app1/contact.html")

def pricing_page_view(request):
    return render(request, "app1/pricing.html")









def profile_page_view(request, username):
    text=f'welcome {username}'
    return HttpResponse(text)

# def about_page_view(request):
#     text='about page'
#     return HttpResponse(text)