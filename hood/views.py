from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CreateHoodForm, BusinessForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood
# Create your views here.

def home(request):
    Neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
@login_required
def create_neighbourhood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            request.user.profile.save()
            hood.save()
            return redirect(home)
    else:
        hood_form = CreateHoodForm()
    return render(request, 'createhood.html', locals())
@login_required
def join_neighbourhood(request, neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect(home)
@login_required
def leave_neighbourhood(request, neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)
    if request.user.profile.neighbourhood == neighbourhood:
        request.user.profile.neighbourhood=None
        request.user.profile.save()
    return redirect(home)
@login_required
def user_neighbourhood(request):
    return render(request, 'userhood.html')
@login_required
def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_owner = request.user.profile
            business.neighbourhood = request.user.profile.neighbourhood
            business.save()
            return redirect(user_neighbourhood)
    else:
        form = BusinessForm()
    return render(request, 'createbusiness.html', locals())
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.neighbourhood = request.user.profile.neighbourhood
            post.save()
            return redirect(user_neighbourhood)
    else:
        form = PostForm()
    return render(request, 'createpost.html', locals())
def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhoods = Neighbourhood.search_neighbourhood(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"neighbourhoods": searched_neighbourhoods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})