from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core import serializers
from django.views import generic
from django.contrib.auth.models import User

from .models import Inventory, Item, Character


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'character/index.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        return Character.objects.all()

class HomeView(generic.ListView):
    template_name = 'character/home.html'

    def get_queryset(self):
        return User.objects.all()



class DetailView(generic.DetailView):
    model = Character
    template_name = 'character/detail.html'
