from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


###Models###
from accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer







from django.shortcuts import redirect, reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login

from accounts.forms import RegistrationForm, EditProfileForm


def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect(reverse('profiles:create'))
        else:
            return redirect('accounts:index')
    else:
        registration_form = RegistrationForm()
        args = {'registration_form': registration_form}
        return render(request, 'accounts/index.html', args)


def edit_account(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return redirect('/accounts/edit/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'accounts/edit_account.html', args)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('homepage')
        else:
            return redirect('accounts/change_password/')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('homepage')

    else:
        registration_form = RegistrationForm()
        args = {'invalid': True, 'registration_form': registration_form}
        return render(request, 'accounts/index.html', args)
