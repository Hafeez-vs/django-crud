from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import Movieform
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

class HomeView(ListView):
    model=Movie
    template_name='home.html'
    context_object_name='m'

# def detail(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request,'detail.html',{'m':m})

class Detail(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name='m'

# def update(request,n):
#     m=Movie.objects.get(id=n)
#     if(request.method=='POST'):
#         form=Movieform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#
#
#     form=Movieform(instance=m)
#     return render(request,'addmovie.html',{'form':form})

class Update(UpdateView):
    model = Movie
    template_name = 'addmovie.html'
    fields=['name','desc','year','image']
    success_url = reverse_lazy('movieapp:home')

# def delete(request,n):
#     m=Movie.objects.get(id=n)
#     m.delete()
#     return home(request)

class Delete(DeleteView):
    model=Movie
    template_name ='delete.html'
    success_url=reverse_lazy('movieapp:home')

# def addmovie(request):
#     if(request.method=='POST'):
#         form=Movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form=Movieform()
#     return render(request,'addmovie.html',{'form':form})

class AddMovie(CreateView):
    model=Movie
    template_name = 'addmovie.html'
    fields=['name','desc','year','image']
    success_url = reverse_lazy('movieapp:home')
