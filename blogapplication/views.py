from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from .form import *
from django.contrib.auth import logout

# def register_view(request):
#     return render(request, 'register.html')
#
# #function for login page
# def login_view(request):
#     return render(request, 'login.html')
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')
#

#This function will show an error page if the user is not logged in to view the page
def login_required_function(request):
    return render(request, 'login_required.html')

#...........................................................................................................................................
def home(request):
    context = {
    'blogs': BlogModel.objects.all(),
    }
    return render(request, 'home.html', context)

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def see_blog(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blog.html', context)

#login_required decorator will not allow any user that is not logged in this website
@login_required(login_url='login_required_exp')
def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)

@login_required
def blog_update(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        #initial_dict = {'content': blog_obj.content, 'title' : blog_obj.title}
        form = BlogForm(instance=blog_obj)
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog_obj)
            print(request.FILES['image'])
            # image_dir = request.FILES['image']
            # image = image_dir
            blog_obj.title = request.POST.get('title')
            blog_obj.image = request.FILES['image']
            user = request.user

            if form.is_valid():
                # content = form.cleaned_data['content']
                form.save()

            # blog_obj = BlogModel.objects.update(
            #     user=user, title=title,
            #     content=content, image=image
            # )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'update_blog.html', context)

@login_required
def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)
    return redirect('/see-blog/')
#.......................................................................................................................................


# def verify(request, token):
#     try:
#         profile_obj = Profile.objects.filter(token=token).first()
#
#         if profile_obj:
#             profile_obj.is_verified = True
#             profile_obj.save()
#         return redirect('/login/')
#
#     except Exception as e:
#         print(e)
#
#     return redirect('/')
