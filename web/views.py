from django.shortcuts import render, redirect
from .models import Web
from .forms import WebForm
from .models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    projects = Web.objects.all()
    return render(request, 'web/index.html', {'projects': projects})


def currentweb(request):
    form = WebForm()
    if request.method == 'POST':
        form = WebForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogweb')
    context = {'form': form}
    return render(request, 'web/currentweb.html', context)


def blogweb(request):
    blog = Blog.objects.order_by('-date')
    page = request.GET.get('page')
    results = 5
    paginator = Paginator(blog, results)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blog = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        blog = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'blogs': blog,
        'paginator': paginator,
        'custom_range': custom_range
    }

    return render(request, 'web/blogs.html', context)

def blog(request, pk):
    blogweb_obj = Blog.objects.get(Blog,id=pk)
    return render(request, 'web/blogweb.html', {'blogweb': blogweb_obj})
