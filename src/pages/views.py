from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# a place that handle your various pages

def home_view(request, *args, **kwargs): # *args **kwargs
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")# string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args **kwargs
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args **kwargs
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 456, 789],
        "my_html": "<h1>Hello World</h1>"
    }

    # render(request, "html path", context)
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs): # *args **kwargs
    return render(request, "social.html", {})