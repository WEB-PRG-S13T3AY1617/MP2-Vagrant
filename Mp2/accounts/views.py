from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from django.views.generic import RedirectView
from django.views import generic
from items.models import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


User = get_user_model()
def login_view(request):
    title = "Log In"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/item")
    return render(request, "accounts/accounts_form.html", context)

def logout_view(request):
    logout(request)

def user_profile(request, user_name):
    all_items = Item.objects.filter(item_poster__pk=user_name)
    objects = all_items
    page = request.GET.get('page', 1)
    paginator = Paginator(objects, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    all_users = User.objects.filter(pk=user_name)
    title = "User Profile"
    context =  {
        'all_items': all_items,
        'all_users': all_users,
        'title': title,
        'users': users,
    }
    return render(request, 'accounts/user_profile.html', context)


def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if form.is_valid() and profile.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        degoff = form.save(commit=False)
        user.set_password(password)
        user.save()
        degoff.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/item")
    context = {
        'form': form,
        'title': title,
        'profile': profile,
    }
    return render(request, "accounts/accounts_form.html", context)




# Create your views here.
