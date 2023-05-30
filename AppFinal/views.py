from django.shortcuts import render

from distutils.log import info
from email import message
from django.shortcuts import render, HttpResponse
from AppFinal.models import *
from django.template import loader
from AppFinal.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


def index(request):
    blogposts = BlogPost.objects.all()
    if blogposts:
        return render(request, 'index.html', {'blogposts':blogposts})
    else:
        return render(request, 'index.html', {'message':"No hay post publicados aun"})


def blogpost(request):
    return HttpResponse("Blog Post")

@login_required
def addblogpost(request):
    if request.method == 'POST':
        myForm = BlogPostForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            title=info['title']
            subtitle=info['subtitle']
            content=info['content']
            category=info['category']
            blogpost = BlogPost(title=title, subtitle=subtitle, content=content, category=category)
            blogpost.save()
            return render(request,"index.html", {'message': "New post were added"})
    else:
        myForm=BlogPostForm()
    return render(request,'addblogpost.html', {'myForm':myForm})


def searchpostsite(request):
    return render(request, 'searchpostsite.html')

def AboutUs(request):
    return render(request, 'acercade.html')


def searchpost(request):
    if request.GET['title']:
        title = request.GET['title']
        blogposts = BlogPost.objects.filter(title__contains=title)
        return render(request, 'blogpost.html', {'blogposts':blogposts})
    else:
        response = "No information added"
    return HttpResponse(response)

@login_required
def deletepost(request, post_id):
    blogpost = BlogPost.objects.get(id=post_id)
    blogpost.delete()

    blogpost = BlogPost.objects.all()
    blogposts = {'blogpost':blogpost}

    return render(request, 'index.html', {'message':"The post has been deleted."})

def register (request):
    if request.method == 'POST':
        myForm = UserRegisterForm(request.POST)
        if myForm.is_valid():

            username=myForm.cleaned_data['username']
            myForm.save()
            return render(request,"index.html", {"message":"El nuevo usuario fue creado exitosamente!"})
    else:
        myForm=UserRegisterForm()
    return render(request,'register.html', {'myForm':myForm})
   

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)
                return render (request, 'index.html', {'message':f"Bienvenido {usuario}!!"})
            else:
                return render (request, 'index.html', {'message':"Ups, datos incorrectos."})
        else:
            return render (request, 'index.html', {'message':"Error, formulario incorrecto."})
    
    form = AuthenticationForm()
    return render (request, 'login.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'subtitle', "content", "category"]
    template_name = 'updatepost.html'
    def dispatch(self, request, *args, **kwargs):
        BlogPost = BlogPost.get_object()
        if BlogPost.id != request.user:
           return render(request,"index.html", {'message': "No tienes permiso para eso"})
        return super().dispatch(request, *args, **kwargs)


def updatepost(request, post_id):
    blogpost = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        myForm = BlogPostForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            blogpost.title=info['title']
            blogpost.subtitle=info['subtitle']
            blogpost.content=info['content']
            blogpost.category=info['category']
            blogpost.save()
            return render(request,"index.html", {'message': "El post ha sido actualizado."})
    else:  
        initial_data={'title':blogpost.title, 'subtitle':blogpost.subtitle, 'content':blogpost.content, 'category':blogpost.category}
        myForm=BlogPostForm(initial=initial_data)
        return render (request, 'updatepost.html', {'myForm':myForm})

def updateprofile(request):
    usuario = request.user
    if request.method == 'POST':
        myForm = UserUpdateForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            usuario.email = info['email']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            return render(request,"index.html", {'message': "The user has been updated."})
    else:

        inicial_data={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name}
  
        myForm = UserUpdateForm(initial=inicial_data)
        return render (request, 'updateprofile.html', {'myForm':myForm})
    

def SendMessage(request):
    if request.method == 'POST':
        myForm = MessageForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            name=info['name']
            message=info['message']
            contactmessage = Message(name=name,message=message)
            contactmessage.save()
            return render(request,"message.html")
    else:
        myForm=MessageForm()
    return render(request,'message.html', {'myForm':myForm})