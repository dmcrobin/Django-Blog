from django.shortcuts import render, redirect
from django.views import generic

from .forms import PostsForm
from .models import Posts

class PostView(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by("-post_date")
    template_name = "index.html"


class DetailView(generic.DetailView):
    model = Posts
    template_name = "post_detail.html"


# def addPost(request):
#     form = PostsForm()
#     return render(request, "add.html", {'form' : form})

def index(request):
    form = PostsForm()
    if(request.method == "POST"):
        # print(request.POST)
        qry = request.POST.copy()
        print(qry['body'])
        title = qry['title']
        slug = title.lower().replace(" ", "-")
        qry['slug'] = slug
        qry['status'] = "1"
        form = PostsForm(qry)
        if(form.is_valid()):
            print("SAVED POST!")
            form.save()
            return redirect('/')
        else:
            print("ERORR", form.errors)
    return render(request, "add.html", {"form" : form})

def editPost(request, slug):
    post = Posts.objects.get(slug=slug)
    form = PostsForm()
    # print(form)
    if(request.method == "POST"):
        # print(request.POST)
        qry = request.POST.copy()
        print(qry['body'])
        title = qry['title']
        slug = title.lower().replace(" ", "-")
        qry['slug'] = slug
        qry['status'] = "1"
        form = PostsForm(instance=post, data=qry)
        print("SAVED POST!")
        form.save()
        return redirect(f'/{slug}')
    else:
        form = PostsForm(instance=post)
        print(form)
    return render(request, "edit_post.html", {"form" : form, 'post' : post})

def delPost(request, slug):
    post = Posts.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect('/')
    else:
        return render(request, "confirm.html")