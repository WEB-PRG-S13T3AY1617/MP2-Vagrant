from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Item
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


class IndexView(generic.ListView):
    model = Item
    template_name = 'items/index.html'
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = Item.objects.all()  # Default: Model.objects.all()
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        title = "All Items"
        context['title'] = title
        return context

    #def get_queryset(self):
    #    return Item.objects.all()

class DetailView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        title = "View Item Details"
        context['title'] = title
        return context

    template_name = 'items/post.html'

class ItemCreate(CreateView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data(**kwargs)
        title = "Post Secondhand Item"
        context['title'] = title
        return context

    fields = [
        'item_poster',
        'item_name',
        'item_price',
        'item_condition',
        'item_type',
        'item_academic_coursename',
        'item_quantity',
        'item_picture',
    ]



class ItemUpdate(UpdateView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemUpdate, self).get_context_data(**kwargs)
        title = "Update Item Details"
        context['title'] = title
        return context

    fields = ['item_name', 'item_price', 'item_info', 'item_condition']

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('items:index')




# Create your views here.
