from django.shortcuts import render, get_object_or_404

from .models import BlogPost

# def blog_post_detail_page(request, slug):
#     obj = get_object_or_404(BlogPost, slug=slug)
#    # obj = BlogPost.objects.get(slug= slug)
#     template_name = 'blog_post_detail.html'
#     context = {"object": obj} # {"title": obj.title}
#     return render(request, template_name, context)

# CRUD
# GET --> Retrieve / List
# GET --> Retrieve / List
# POST --> Create / Update / Delete

# Create Retrieve Update Delete

def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all() # list of python objects
    template_name = 'blog/list.html'
    context  = { 'object_list' : qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # create objects
    # how? use a form
    template_name = 'blog/create.html'
    context = {'form' : None}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # retieve_view = detail_view
    # 1 object --> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)

