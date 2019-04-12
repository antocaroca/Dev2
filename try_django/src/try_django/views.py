from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# def home(request):
#     my_title = "Hello There..."
#     context = {"title": my_title}
#     template_name   = "title.txt"
#     template_obj    = get_template(template_name)
#     rendered_string   = template_obj.render(context)
#     print(rendered_string)
#     return render(request, "base.html", {"title": rendered_string})

def home(request):
    my_title = "Hello There..."
    context = {"title": "my_title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5]}
    
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {"title": "About Us"})

def contact(request):
    return render(request, "contact.html", {"title": "Contact Us"})

def example_page(request):
    context         = {"title": "Exampleeee"}
    template_name   = "example.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(template_obj.render(context))